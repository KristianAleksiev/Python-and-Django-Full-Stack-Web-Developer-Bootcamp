//COMPARISON OPERATORS

x1 > x2;
x1 < x2;
x1 <= x2;
x1 >= x2;
x1 == x2;
x1 != x2;

"2" == 2 // True, type converting to similar types
"2" === 2 // False, different data type

"2" !== 2 // True, different data types
"2" != 2 // False, converting to similar types

null == undefined // True
null === undefined // False

NaN == NaN // False

//LOGICAL OPERATORS

1 === 1 && 2 === 2; // And operator
1 === 1 || 1 === 1; // Or operator


// Exercise

var x = 1;
var y = 2;

"2" == y && x === 1; //True
x >= 0 || y === "2"; //True
y !== "2" && x < 10; //True
y !== x || y == "2" || x === 3; //True
