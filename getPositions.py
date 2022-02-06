import urllib.request
import json
import time
from datetime import datetime, timedelta
import requests
import pandas as pd
from pandas import json_normalize
import numpy as np

#Lista de criptos para manter no radar (Problemas para rodar ETC e CRV - AVAX, SHIB, SOL, TRX, VET)
listaCriptos = ['ADA-USDT','ATOM-USDT','BCH-USDT','BSV-USDT','BTC-USDT','DOGE-USDT','DOT-USDT',
                'ETH-USDT','ENJ-USDT','EOS-USDT','LUNA-USDT','LTC-USDT','LINK-USDT','MATIC-USDT','OMG-USDT']
pnlTot = 0
pnlTotPos = 0
pnlTotNeg = 0
contPos = 0
msgBalance = ''
for i in listaCriptos:
    par = i
    pegaPosicao =  getPositions(par)    
    pegaPosicaoJs = json.loads(pegaPosicao)
    JsonpegaPosicao = pegaPosicaoJs['data']['positions'] 
    if JsonpegaPosicao != None:
        lucro = JsonpegaPosicao[0]['pnlRate']
        side = JsonpegaPosicao[0]['positionSide']
        print (par, '-', side,': ', lucro, '%')
        if lucro > 0:
            pnlTotPos = pnlTotPos + lucro
            contPos = contPos + 1
        if lucro < 0:
            pnlTotNeg = pnlTotNeg + lucro
            contPos = contPos + 1
balance =  getBalance()
balanceJs = json.loads(balance)
JsonAval = balanceJs['data']['account']
balanceX = JsonAval['equity']
if contPos > 0:
    print(contPos, 'ordens em aberto - Pnl médio:', round(pnlTotPos/contPos, 2) + round(pnlTotNeg/contPos, 2), '% - Balance: ', balanceX)
    msgBalance = str(contPos), 'ordens em aberto - Pnl médio:', str(round(pnlTotPos/contPos, 2)) + str(round(pnlTotNeg/contPos, 2)), '% - Balance: ', balanceX
    msgBalance = msgBalance + ('/n ' + str(contPos), 'ordens em aberto - Pnl médio:', str(round(pnlTotPos/contPos, 2)) + str(round(pnlTotNeg/contPos, 2)), '% - Balance: ', balanceX,)
else:
    print ('Nenhuma posição em aberto. Balance:', balanceX)
    msgBalance = 'Nenhuma posição em aberto. Balance:', balanceX
