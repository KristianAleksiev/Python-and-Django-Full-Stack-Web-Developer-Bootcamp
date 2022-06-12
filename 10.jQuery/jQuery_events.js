$("h1").click(function(){
  $(this).text("I was changed")

})

$("li").click(function(){
  console.log("Any li was clicked!")
})

// Key press, Event Object (which - ASCII input)
$("input").eq(1).keypress(function(event){
  console.log(event);
})

$("input").eq(1).keypress(function(event){
  if (event.which === 13){
    $("h3").toggleClass("turnRed");
  }
})

// on() - on doubleclick call this function - "this" reffers to h1
$("h1").on("dblclick", function(){
  $(this).toggleClass("turnBlue");
})

$("h1").on("mouseenter", function(){
  $(this).toggleClass("turnBlue");
})

// ANIMATIONS
// $("input").eq(0).on("click", function(){
//   $(".container").fadeOut(3000)
// })


$("input").eq(0).on("click", function(){
  $(".container").slideUp(3000)
})
