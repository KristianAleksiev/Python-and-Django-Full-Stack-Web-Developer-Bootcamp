var paragraph = document.querySelector("p");

paragraph.textContent = "new text"; // Manipulating the raw text, without styling
paragraph.innerHTML = "<strong>I'm bold now</strong>"// Manipulating text WITH styling

var special = document.querySelector("#link");
var specialAnchor = special.querySelector("a");


specialAnchor.getAttribute("href"); // getting the attribute
specialAnchor.setAttribute("href", "https://facebook.com") // changing the attribute
