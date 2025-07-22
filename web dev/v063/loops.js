let a = [1, 93, 5, 6, 88]

/*
for (let index = 0; index < a.length; index++) {
    const element = a[index];
    console.log(element) // prints array 
}
*/

a.forEach((value, index)=>{
    console.log(value, index) // prints array elements in key value pairs
})

let obj = {
    a : 1,
    b : 2,
    c : 3
}


for (const key in obj){     // This is for-in loop
    if (Object.hasOwnProperty.call(obj, key)) {
        const element = obj[key]; 
        console.log(key, element)
    }
}


for (const value of a) {   // This is for-of loop
    console.log(value)
}






