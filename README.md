![@avesraras](logo.png)  # AVES_RARAS_TECNOLOGIA_EM_INVESTIMENTOS

botavesraras@gmail.com
<html lang="pt" >
<html>
<head>
  
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="login_style.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <link href='https://fonts.googleapis.com/css?family=Titillium+Web:400,300,600' rel='stylesheet' type='text/css'>  
  <link href='https://fonts.googleapis.com/css?family=Titillium+Web:400,300,600' rel='stylesheet' type='text/css'>  
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.1/css/all.css" integrity="sha384-vp86vTRFVJgpjF9jiIGPEEqYqlDwgyBgEF109VFjmqGmIY/Y4HV4d3Gp2irVfcrp" crossorigin="anonymous">
</head>

<body class="body">  

    <form> 
      <div class="login-page">
      <div class="form">
      
      <input type="text" placeholder="Usuário"/>
      <input type="password" id="password" placeholder="Senha"/>
      <i class="fas fa-eye" onclick="show()"></i> 
      <br>
      <br>
      <button type="button" onclick="window.location.href='igomorf.html'">LOGIN</button>      
      <p class="message"></p>    

    <form class="login-form">
      <button type="button" onclick="window.location.href='signup.html'">NOVO USUÁRIO</button>
    </form>
  </div>
</div>

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
</body>
</html>

