

let randomNumber = Math.floor(Math.random() * 100) + 1;
console.log(`Random number between 1 and 100: ${randomNumber}`);

function fibonacci(n) {
    if (n <= 0) return [];
    if (n === 1) return [0];
    
    let sequence = [0, 1];
    for (let i = 2; i < n; i++) {
        sequence.push(sequence[i - 1] + sequence[i - 2]);
    }
    return sequence;
}


console.log(fibonacci(randomNumber));