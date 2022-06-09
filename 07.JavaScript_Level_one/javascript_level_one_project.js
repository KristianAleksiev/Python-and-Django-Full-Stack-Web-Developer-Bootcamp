var nameCondition = null;
var ageCondition = null;
var heightCondition = null;
var petCondition = null;

var firstName = prompt("Enter your first name: ")
var lastName = prompt("Enter your last name? :")
var age = prompt("How old are you? ")
var petName = prompt("What's your pet name? ")
var height = prompt("How tall are you? ")

alert("Thank you so much for the information!")

if (firstName[0] === lastName[0]){
  nameCondition = true;
}else{
  nameCondition = false;
}

if (age > 20 && age < 30){
  ageCondition = true;
}else{
  ageCondition = false;
}
if (height >= 170){
  heightCondition = true;
}else{
  heightCondition = false;
}
if (petName[petName.length-1] == "y"){
  petCondition = true;
}else {
  petCondition = false;
}

if (nameCondition && ageCondition && heightCondition && petCondition){
  console.log("Welcome Spy");
}else{
  console.log("You are not a spy. That's unfortunate comrade!");
}
