// Write a program to calculate factorial of a number using reduce and using for loops

let a = 5
function factorial(number){
    let arr = Array.from(Array(number+1).keys())   // without for loop
    let c = arr.slice(1,).reduce((a,b)=>a*b)
    return c
}

function factFor(number){   // using for loop
    let fact = 1
    for (let index = 1; index <= number; index++) {
        fact = fact * index   
    }
    return fact
}


console.log(factorial(a))
console.log(factFor(a))