//document - Gets the HTML of the page
// console.dir(document) - Gets the objects of the document

// IMPORTANT DOCUMENT ATTRIUBUTES
document.URL // URL or Local location
document.body
document.head
document.links

// // METHODS FOR GRABBING ELEMENTS FROM THE DOM
document.getElementById()
document.getElementByClassName()
document.getElementsByTagName()
document.querySelector() // Returns the first object matching the CSS style selector
document.querySelectorAll() // Returns all the matching CSS style selectors

document.querySelector("#ID")

// INTERACTING WITH THE OBJECTS // Console code

var myHeader = document.querySelector("h1")

myHeader.style.color = "red";

// INTERACTING WITH TEXT, HTML, ATTRIBUTES
myVariable.textContent // Returns text
myVariable.innerHTML // Returns the HTML
myVariable.getAttribute() // Returns the original attriibute
myVariable.setAttribute() // Setting an attribute


// EVENT LISTENER
var variable = document.querySelector("h1");
variable.addEventListener("event", function);
