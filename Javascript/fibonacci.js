
// 'fibonacci' is a function that takes an integer as an input and returns the nth element from the Fibonacci sequence

const fibonacci = n => n <= 1 ? n : fibonacci(n - 1) + fibonacci(n - 2);

console.log(fibonacci(10));