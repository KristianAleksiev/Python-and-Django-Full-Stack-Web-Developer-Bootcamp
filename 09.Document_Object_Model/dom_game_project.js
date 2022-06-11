// Button functionality
var restart = document.querySelector("#button")
// Getting the squares
var squares = document.querySelectorAll("td")
// Clear the squares
function clearBoard() {
  for (var i = 0; i < squares.length; i++){
    squares[i].textContent = "";
  }
}
// Checks if X or O
function changeMarker(){
  if(this.textContent === ""){
    this.textContent = "X";
  }else if (this.textContent === "X") {
    this.textContent = "O";
  }else {
    this.textContent = "";
  }
}

for(var i = 0; i < squares.length; i++){
  squares[i].addEventListener("click", changeMarker)
}

// Adding event listeners to the squares
restart.addEventListener("click", clearBoard);
