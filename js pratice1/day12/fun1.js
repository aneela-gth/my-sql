// // named function
// function fun_name(){
// console.log("my name is aneela")
// console.log("good")
// }
// fun_name()
// // paramitrizedfunction
// function fun_name1(name,age,place){
// console.log(name,age,place)
// }
// fun_name1("akhila",22,"khammam")
// // arrow function
// var name=()=>{
// console.log("rebbavaram")
// }
// name()


// async function fetchData(){
//     var response=await fetch('https://fakestoreapi.com/products/1')
//     var result=await response.json();
//     console.log(result);
// }
// fetchData();

// var i=5
// while(i<=10){
//     console.log(i)
//     i++;
// }

// // 1.anonymous function
// var res=function(){
//  console.log("hello every one");
//  console.log("my name is aneela")
// }
// res();
// var hem=function(){
//     console.log("hello from an anonymous function");
// }
// hem()
// // 2.callback function
// function print(){
//     console.log("printing numbers");
    
// }
// function sum(a,b){
//     var c=a+b;
//     console.log(c);
// }
// function fun(f){
//     console.log(f);
// }
// fun(print(),sum(14,12))


// function greet(){
//     console.log("good morning")
// }
// function execute(callback){
//     callback();
// }
// execute(greet);


// // 3.higher order function

// function welcome(){
//     console.log("welcome!");
// }
// function higherOrder(callback){
//     callback();
// }
// higherOrder(welocme);


// function hig(){
//     return function(){
//         console.log("returned from higher_order function");
//     };
// }
// let result=hig();
// result();


// // 4.IIFE(immediately invoked function expression)

// (function(){
//     console.log("iife executed");
// })();

// (function(name){
//     console.log("what are you doing")
// })("aneela");



// // 4.async function
// async function fetchData(){
//     let response=await fetch('https://fakestoreapi.com/products/1')
//     let data=await response.json();
//     console.log(data);
// }
// fetchData();
