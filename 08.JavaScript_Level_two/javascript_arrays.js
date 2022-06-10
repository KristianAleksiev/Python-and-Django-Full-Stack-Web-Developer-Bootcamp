var countryOne = "USA";
var countryTwo = "Germany";
var countryThree = "China";


var countries = ["USA", "Germany", "China"]


// Accessing the array elements
countries[0] //-> First elements
//Reassigning elements
countries[2] = "France";


// Immutable vs mutable
//strings = Immutable

//Mixed data types
var mixed = [true, 200, "string"];
mixed.length

// Array methods
var myArray = ["one", "two", "three"];
var lastItem = myArray.pop(); // Removes last item and returns it
var addItem = myArray.push("new_item"); // Adds an item at the back of the array
var lastIndex = myArray[myArray.length - 1]; // Index of last item in array
var nestedArray = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

// Array itteration
var arr = ["A", "B", "C"];
for (var i = 0; i < arr.length; i++){
  console.log(arr[i]); // getting the elements
}

for (element of arr){
  console.log(element);
}

// Passing the elements of an array into a function
for (letter of arr){
  alert(letter);
}

arr.forEach(alert()); // Same as upper
/////////////////
function addAwesome(name){
  console.log(name + " is awesome!");
}

var topics = ["python", "django", "science"];
topics.forEach(addAwesome);
