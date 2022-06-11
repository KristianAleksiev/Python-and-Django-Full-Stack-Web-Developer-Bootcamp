// OBJECT METHODS - Functions inside the object

var carInfo = {
  make: "Toyota",
  year: 1990,
  model: "Camry",
  carAlert: function(){
    alert("We've got a car here!")
  }
};
///////////////////
var myObj = {
  prop: 37,
  reportProp: function(){
    return this.prop;
  }
};
///////////////////

var simple = {
  property: "Hello",
  myMethod: function(){
    console.log("The myMethod was called")
  }
};
console.log(simple); // No methods visible
console.dir(simple); //
simple.myMethod // Returns what the function is
simple.myMethod() // Executes the method
///////////////////
// Method uses the property of the current object
var myObj = {
  name: "Kristian",
  greet: function(){
    console.log("Hello " + this.name);
  }
};
myObj.greet()
