<html>
<head><title>Easynote-web</title></head>
<body>
<h2>Easynote-Web版 v0</h2>
<h3>添加笔记</h3>
<form action="/eznote" method="post">
	> <input name="newnote" type="text" />
	<input value="Add" type="submit" />
</form>
<br />
<h3>历史笔记</h3>
<ul>
  % for note in notes:
    <li>{{note}}</li>
  % end
</ul>
</body>
</html>