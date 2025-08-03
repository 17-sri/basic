let arr = [1, 4, 2, 6, 7, 9]
// index   0  1  2  3  4  5  
 arr[0] = 90
 console.log(arr) // prints [ 90, 4, 2, 6, 7, 9 ]
 console.log(" the type of array is  --> " +typeof arr) // object
 console.log("The length of array is  --> " + arr.length) // 6
 console.log(arr[0]) // prints 90
 console.log(arr[6]) // undefined

 console.log(arr.toString()) // prints 90,4,2,6,7,9    //prints without square braces
 console.log(arr.join(" and ")) // prints 90 and 4 and 2 and 6 and 7 and 9

 let numbers = [1, 2, 3, 4, 5]
console.log(numbers.splice(1, 3, 12, 21)) 
console.log(numbers)// prints [1, 12, 5]






