<html>
<head>  
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="style.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <link href='https://fonts.googleapis.com/css?family=Titillium+Web:400,300,600' rel='stylesheet' type='text/css'>  
  <link href='https://fonts.googleapis.com/css?family=Titillium+Web:400,300,600' rel='stylesheet' type='text/css'>  
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.1/css/all.css" integrity="sha384-vp86vTRFVJgpjF9jiIGPEEqYqlDwgyBgEF109VFjmqGmIY/Y4HV4d3Gp2irVfcrp" crossorigin="anonymous">
</head>

<body class="body">
  <header>
    
  </header>              
  <p><h2>root@avesraras:~/TEOLOGIA_EM_INVESTIMENTOS#</h2></p>
          <h3>botavesraras@gmail.com</h3>    
    <form> 
        <div class="login-page">
          <center><h2>Faça seu login</h2></center>
            <div class="form">                  
                  <input type="text" placeholder="Usuário"/>
                  <input type="password" id="password" placeholder="Senha"/>
                  <i class="fas fa-eye" onclick="show()"></i> 
                  <br>
                  <br>
                  <button type="button" onclick="window.location.href='igomorf.html'">LOGIN</button>      
                  <p class="message"></p>    

                  <form class="login-form">
                      <button type="button" onclick="window.location.href='signup.html'">Contrate um Plano</button>
                  </form>
            </div>
        </div>
    </form>
    <script>
        function show(){
            var password = document.getElementById("password");
            var icon = document.querySelector(".fas")
            // ========== Checking type of password ===========
            if(password.type === "password"){
                password.type = "text";
            }
            else {
                password.type = "password";
            }
        };
    </script>
  
<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <div class="tradingview-widget-copyright"><a href="https://br.tradingview.com" rel="noopener" target="_blank"><span class="blue-text">Tape de Cotações</span></a> por TradingView</div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>
  {
  "symbols": [
    {
      "description": "BTC-USDT",
      "proName": "BINGX:BTCUSDT"
    },
    {
      "description": "AXS-USDT",
      "proName": "BINGX:AXSUSDT"
    },
    {
      "description": "BAL-USDT",
      "proName": "BINGX:BALUSDT"
    },
    {
      "description": "ATOM-USDT",
      "proName": "BINGX:ATOMUSDT"
    },
    {
      "description": "BCH-USDT",
      "proName": "BINGX:BCHUSDT"
    },
    {
      "description": "BSV-USDT",
      "proName": "BINGX:BSVUSDT"
    },
    {
      "description": "DOT-USDT",
      "proName": "BINGX:DOTUSDT"
    },
    {
      "description": "ENJ-USDT",
      "proName": "BINGX:ENJUSDT"
    },
    {
      "description": "EOS-USDT",
      "proName": "BINGX:EOSUSDT"
    },
    {
      "description": "ETH-USDT",
      "proName": "BINGX:ETHUSDT"
    },
    {
      "description": "LINK-USDT",
      "proName": "BINGX:LINKUSDT"
    },
    {
      "description": "LTC-USDT",
      "proName": "BINGX:LTCUSDT"
    },
    {
      "description": "LUNA-USDT",
      "proName": "BINGX:LUNAUSDT"
    },
    {
      "description": "MATIC-USDT",
      "proName": "BINGX:MATICUSDT"
    },
    {
      "description": "OMG-USDT",
      "proName": "BINGX:OMGUSDT"
    }
  ],
  "showSymbolLogo": true,
  "colorTheme": "dark",
  "isTransparent": false,
  "displayMode": "adaptive",
  "locale": "br"
}
  </script>
</div>
<!-- TradingView Widget END -->  
  
</body>
</html>

