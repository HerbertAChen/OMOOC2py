<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Easynote-WEB</title>

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="//cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css">

    <style>
    body {
      padding-top: 50px;
      background-color: #eee;
    }
    .new-note {
      padding: 40px 50px;
      margin-top: 60px;
    }
    .note-form {
      max-width: 600px;
      padding: 1px;
      margin: 0 auto;
    }
    .note-form .form-control {
      position: relative;
      height: auto;
      -webkit-box-sizing: border-box;
         -moz-box-sizing: border-box;
              box-sizing: border-box;
      padding: 10px;
      font-size: 16px;
      size:40;
    }
    .note-history {
      padding: 10px 10px;
      text-align: center;
    }
    .note-history .note-content{
      font-size: 21px;
      margin-top: 20px;
      margin-bottom: 5px;

    }
    .note-history .note-time{
      font-size: 14px;
      color: Grey;
    }

    </style>

  </head>

  <body>

    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/">EASYNOTE</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/contact">Contact</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>

    <div class="container">

      <div class="new-note">
        <form action="/" method="post" class="note-form">
        <input type="text" name="newnote" class="form-control" placeholder="add new note" autofocus/>
        </form>
      </div>

      <div class="note-history">
        % for note in notes:
        <p class='note-content'> {{note.get('content','')}}</p>
        <p class='note-time'> {{note.get('time','')[:16]}}</p>
        % end
      </div>

    </div><!-- /.container -->

  </body>
</html>
