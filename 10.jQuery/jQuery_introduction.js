// Vanilla JS
var divs = document.querySelectorAll("div");
el.style.borderWidth = "20px";


function ready(fn){
  if(document.readyState != "loading"){
    fn();
  }else{
    document.addEventListener("DOMContentLoaded", fn)
  }
}

// jQuery
var divs = $("div"); // grabbing all the elements
$(el).css("border-width", "20px");


$(document).ready(function(){//code});



  
