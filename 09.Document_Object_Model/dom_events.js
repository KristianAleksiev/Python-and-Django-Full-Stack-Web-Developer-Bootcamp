// EVENT LISTENER

var headOne = document.querySelector("#one");
var headTwo = document.querySelector("#two");
var headThree = document.querySelector("#three");

headOne.addEventListener("mouseover",function(){
  headOne.textContent = "Mouse is on me";
  headOne.style.color = "red";
})

headOne.addEventListener("mouseout", function(){
  headOne.textContent = "HOVER OVER ME";
  headOne.style.color = "black";
})

headTwo.addEventListener("click", function(){
  headTwo.textContent = "THANK";
  headTwo.style.color = "blue";
})

headThree.addEventListener("dblclick", function() {
  headThree.textContent = "YOU";
  headThree.style.color = "darkgreen";
})
