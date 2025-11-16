// // // Intermediate Level

// // 1.Write a program that swaps the values of two variables without using a third variable.
// a=10
// b=20
// a=a+b
// b=a-b
// a=a-b
// console.log("a=",a)
// console.log("b=",b)

// -------------------------------------------------------------------------------------------

// 2.What happens if you use a variable before declaring it with let?
// console.log(x)
// let x=5
// ReferenceError: Cannot access 'x' before initialization
// Variables declared with let (and const) are hoisted,
// but placed in the Temporal Dead Zone (TDZ)
//  — a phase before declaration where the variable exists but is not accessible.
// You can’t use the variable before the line it’s declared on.

// --------------------------------------------------------------------------------------------

// 3.Write code to demonstrate block scope of let and function scope of var.

// function testscope(){
//     if(true){
//         var x=10;
//         let y=20;
//         console.log("inside block:",x,y);
//     }
//     console.log("outside block:",x);
// }
// testscope()

// 4.Explain and show an example of global scope vs local scope variables.

// let globalvar="i am global"; //out side the functions,accessible everywhere.
// function showscope(){
//     let localvar="i am local";  //declared inside a function ,accessible only inside that function
//     console.log(globalvar);
//     console.log(localvar)
// }
// showscope();
// console.log(globalvar)

// 5.What will be the output?

// console.log(a);
// var a=5;
// console.log(a);

// // 1. Declare variables using var, let, and const
// var name = "Aneela";   // can be redeclared & updated
// let age = 22;           // can be updated, not redeclared
// const city = "Khammam"; // cannot be changed or redeclared

// // 2. Swap two variables without using a third variable
// var a=5;
// var b=10;
// [a,b]=[b,a];
// console.log(a,b);

// // 3. Check type of values using typeof
// console.log(typeof "hello");
// console.log(typeof 10);
// console.log(typeof true);
// console.log(typeof 10.2);
// console.log(typeof {});
// console.log(typeof []);

// // 4. Check if a number is even or odd
// var num=10;
// if (num % 2 ==0){
//     console.log("even");
// }else{
//     console.log("odd");
// }



// // 7. Find the biggest of three numbers
// var a=12;
// var b=23;
// var c=2;
// var biggest = (a > b && a > c) ? a : (b > c ? b : c);
// console.log("biggest:", biggest);

// // 8. Find the largest of three numbers
// var a=12;
// var b=23;
// var c=2;
// var largest=(a<b && a<c)? a :(b<c ? b:c);
// console.log("largest:", largest);


// // 9.Convert Celsius to Fahrenheit
// // Formula: °F = (°C × 9/5) + 32
// function celsiusToFahrenheit(celsius) {
//     var fahrenheit = (celsius * 9/5) + 32;
//     return fahrenheit;
// }

// var celsius = 25;
// var fahrenheit = celsiusToFahrenheit(celsius);
// console.log(`${celsius}°C = ${fahrenheit}°F`);

// // 10.Find the sum of digits of a number.
// function sumofdigits(num){
//     var sum=0
//     while (num>0){
//         var digit=num%10;
//         sum+=digit;
//         num=Math.floor(num/10);
//     }
//     return sum;

// }
// var num=123;
// var result=sumofdigits(num);
// console.log(`sum of digits of ${num}=${result}`)

// 🔹 Strings

//1. Reverse a string.

// function reverseString(str) {
//     if (str === "") return "";
//     return reverseString(str.substr(1)) + str.charAt(0);
// }

// console.log("Reversed string:", reverseString("hello"));

// 2.Count vowels in a string.

