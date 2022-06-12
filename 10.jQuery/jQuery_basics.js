// Selecting with jQuery

$("a") // Selecting all anchor tags
$(".container") // Selecting all elements from class container
$("#ID") // Selecting the element with the ID

var header = $("h1");
header.css("color", "red");
header.css("background", blue;)

// var newCss = {
//   color: "white";
//   background: "green";
//   border: "20px solid red"
// }
// header.css(newCss)

var listItems = $("li");
listItems.css("color", "blue")

listItems.eq(0).css("color", "orange") // Getting an element from all by index
listItems.eq(-1).css("color", "green")// Getting the last item

// Modifying text
$("h1").text() // Return the text of h1
$("h1").text("New text to the h1")
//Changing the html
$("h1").html("<strong>new</strong>")

// Attributes

$("input").eq(0).attr("type", "checkbox")


$("input").eq(1).val("new value")

// CSS Classes
$("h1").addClass("turnRed");
$("h1").removeClass("turnRed");
$("h1").toggleClass("turnBlue");// Toggling on and off
