---
layout: default
title: Reading raw data from post
---

# Reading raw data from post

Sometimes, the client send a lot of data by post method. In webpy, you can handle it like this.
<html>
<body>
     // ajax request
     function ajaxFunction()
{
var xmlhttp;
if (window.XMLHttpRequest)
  {
  // code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {
  // code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
xmlhttp.onreadystatechange=function()
{
if(xmlhttp.readyState==4)
  {
  document.myForm.time.value=xmlhttp.responseText;
  }
}
xmlhttp.open("POST","posttest.py",true);
var data ="test data";
//Send the proper header information along with the request
http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
http.setRequestHeader("Content-length", params.length);
http.setRequestHeader("Connection", "close");
xmlhttp.send(data);
}
</body>
</html>

class RequestHandler():
     def POST():
         data = web.data()// you can just get the data like this