//**Find PI to the Nth Digit** - 
// Enter a number and have the program generate PI
//  up to that many decimal places.
//  Keep a limit to how far the program will go.

let pi="3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

let digitNumber = Math.floor(Math.random() * 100);

let piToDigit = pi.slice(0, digitNumber);

console.log(piToDigit);


