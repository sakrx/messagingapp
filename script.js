function myFunction() {
  var x = document.getElementById("email");
  
  var text = "";
  var i;
  for (i = 0; i < x.length ;i++) {
    text += x.elements[i].value + "<br>";
  }

  document.getElementById("demo").innerHTML = text;
}