// JS OBJECTS EXERCISE

var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  nameLength: function(){
    console.log(this.name.length);
  }
};

//////////////////
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  alert: function(){
    alert("Name is " + this.name + ", Job is" + this.job + ", Age is" + this.age)
  }
};
/////////////////
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  lastName: function(){
    console.log(this.name.split(" ")[1]) // Splitting in JS
  }
};
