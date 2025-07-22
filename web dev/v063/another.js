let arr = [1, 13, 5 ,7, 11];
/*
let newArray = []
for (let index = 0; index < arr.length; index++) {
    const element = arr[index];
    newArray.push(element**2)   
}
*/


let newArray = arr.map((e, index, arr)=>{
    return e**2
})
console.log(newArray) // Prints squared result [ 1, 169, 25, 49, 121 ]




const greaterThanSeven = (e)=>{
    if(e>7){
        return true
    }
    false
}
console.log(arr.filter(greaterThanSeven)) // Prints [ 13, 11 ]




let arr2 = [1, 2, 3, 4, 5, 6]
const red = (a, b)=>{
    return a+b
}
console.log(arr2.reduce(red)) // Prints 21 ......adds the elements of arr2
