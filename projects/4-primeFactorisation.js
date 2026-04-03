// **Prime Factorization** - 
// Have the user enter a number and find all Prime Factors 
// (if there are any) and display them.

function primeFactors(n) {
    let factors = [];                           
    for (let i = 2; i <= n; i++) {
        while (n % i === 0) {                    
            factors.push(i);
            n /= i;
        }
    }
    return factors;
}

// Example usage:
let number = 10
console.log(`Prime factors of ${number}: ${primeFactors(number)}`); // Prime factors of 60: [2, 2, 3, 5]


