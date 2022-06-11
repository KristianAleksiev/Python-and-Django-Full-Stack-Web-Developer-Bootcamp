// OBJECTS IN JAVASCRIPT - DICTIONARIES

var carInfo = {make: "Toyota",
 year: 1990,
  model: "Camry"
};
console.log(carInfo);
carInfo["make"]
carInfo["year"]
carInfo["year"] = 2006;
carInfo["year"] += 1;

var myNewObj = {a:"hello", b:[1, 2, 3], c:{inside:["a", "b"]}};

myNewObj["a"]
myNewObj["b"][0]
myNewObj["c"]["inside"][0]


console.dir(carInfo); // Getting object elements in browser

//Itterating through object
for (key in carInfo){// NO SPECIFIC ORDER
  console.log(key); // key
  console.log(carInfo[key]); // value
}
