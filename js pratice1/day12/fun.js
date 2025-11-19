//                                             //    **function-->function is ablock of code ,used to perfom a specific tack
// // 1.namedfunction
// function fun_name(){
//     var a=4;                                //1.named function-->function with the name is known as named function//
//     var b=5;
//     var c=a*b;
//     console.log(c);
// }
// fun_name();


// // *2.// paramterfunction                   
// function place1(a,b){                  //2.paramterfunction-->the function by passing the parameter//
// console.log(a+b)                         
// }
// place(2,4)

// // // 3.returned function:
// function myfunction(){
//     console.log("hello every one")               
//     var a=50;                            
//     var b=20;
//     var c=a-b;                            //returnedfunction--->the function which returns is known as return function
//     console.log(c);                          //return----->keyword,it should be the last executable statement//
//     var d=a+b; 
//     return d;
// }
// console.log(myfunction());


// // //1. arrow function                  // arrowfunction---->the function without a function name and 
// var name=()=>{                                         // a function keyword//
//     var a=10
//     var b=2
//     var c=a+b
//     console.log(c)
// }
// name()
// // arrow function 
// var place=()=>{
//     console.log("my name is aneela")
//     var a=2
//     var b=5
//     var c=a*b
//     console.log(c)
//     var d=a+b
//     return d
// }
// console.log(place())

// // // 2.prametrized arrow function
// var place2=(name,age)=>{
//     console.log(name+age)
// }
// place2("aneela",23)

// // //3.returned arrowfunction
// var num=()=>{
// console.log("aneela")
// return "akhila"
// }
// console.log(num());

// // //4. parametrize returnfunction
// var number=(name,age)=>{
// console.log(name);
// return age;
// }
// console.log(number("suppu",23))



// task:
// function employee(id,name,age,salary,location){
//   console.log(id)
//   console.log(name)
//   console.log(age)
//   console.log(salary)
//   console.log(location)
// }
// employee(101,"raju",23,50000,"khammam")

var res=function(){
  console.log("yes,jan feeling good");
}
res();


var aki=function(){
  console.log("my name is aneela");
}
aki();

// 2.parameterized anonymous function
var man=function(a,b){
    console.log(a+b)
}
man(2,3)

// 3.returned anonymous function

 var ane=function(a,b){
    console.log(a+b)
    return a-b
}
console.log(ane(5,2))

// 4.anonymous arrow function
var ane=((a,b)=>{
 var a
 var b
 console.log(a*b)
 
})
ane(2,3)

// 5.parameterized arrow anonymous function
var place2=(name,age)=>{
    console.log(name+age)
}
place2("aneela",23)