// function function_name(a,b){
//     var a=10
//     var b=20
//     console.log(a+b);
//     var c=a-b
//     return c

// }
// function_name()
// console.log(function_name)


// function area(length,height){
//   console.log(length*height)
// }
// area(2,4)


// 1.arrowfunction:
var name=()=>{
    console.log("aneela")
}
name()

// //2. parametize arrow function
var name1=(a,b)=>{
console.log(a+b)
}
name1(2,3)

// 3.returned arrow function
var name2=()=>{
    var a=1
    var b=2
    var c=a+b
    console.log(c)
    var d=a*b
    return d
}
console.log(name2())

// 4.parametrized arrow return function
var name3=(a,b)=>{
console.log(a+b)
var d=a*b
return d
}
console.log(name3(2,3))
