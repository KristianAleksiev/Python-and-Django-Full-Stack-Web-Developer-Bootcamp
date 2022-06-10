// FUNCTIONS IN JAVASCRIPT

// function name(param1, param2){
//   //code block
// }

function hello(){
  console.log("Hello world!");
}
hello()

var inputName = prompt("Enter your name, please!")
function helloYou(name){
  console.log("Hello " + name);
}
helloYou(inputName)


function addNum(num1, num2){
  console.log(num1 + num2);
}

function helloSomeone(name="Frank"){ // Default parameter
  console.log("Hello " + name);
}

// Returning values
function formal(name="Sam", title="Sir"){
  return title + " " + name
}
var output = formal()


function timesFive(numInput){
  var result = numInput * 5
  return result
}
timesFive(4)


// Scope of variable
var v = "GLOBAL VARIABLE";
var something = "GLOBAL AGAIN";
function fun(something){
  console.log(v);
  something = "Reassigning inside function"
  console.log(something);
}
fun()
console.log(something);
