//**Find e to the Nth Digit** - 
// Just like the previous problem, but with e instead of PI. 
// Enter a number and have the program generate e up to that many decimal places.
//  Keep a limit to how far the program will go.


let e = "2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274"

let digitNumber = Math.floor(Math.random() * 100);

let eToDigit = e.slice(0, digitNumber);

console.log(digitNumber)
console.log(eToDigit);