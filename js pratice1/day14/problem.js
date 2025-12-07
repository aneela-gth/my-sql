// for (let i = 1; i <= 3; i++) {       // outer
//   for (let j = 1; j <= 2; j++) {     // inner
//     console.log(`i=${i}, j=${j}`);
//   }
// }


// for (let i=1; i<=5; i++){
//     let row="";
//     for (let j=1; j<=5; j++ ){
//         row+="*";
//     }
//     console.log(row);
// }

// const matrix = [
//   [1, 2, 3],
//   [4, 5, 6],
//   [7, 8, 9]
// ];

// let s="hello"
// let d=""
// for (let i of s ){
//     d=i+d;
// }
// console.log(d)

// let arr=[10,4,50,30]
// // let larger=Math.max(...arr);
// let c=Math.min(...arr)
// console.log(c)

// let str="madam"
// let ispalindrom=true;

// for(let i=0; i<str.length/2; i++){
//   if(str[i]!==str[str.length-1-i]){
//     ispalindrom=false;
//     break;
//   }
// }

// console.log(ispalindrom); // true


// for (let i=0; i<=5; i++){
//     console.log(i);
// }

// let i=1;
// while(i<=5){
//     console.log(i);
//     i++;
// }
// let arr = [10,20,30];

// for(let value of arr){
//   console.log(value);
// }
// let obj = {name:"Aneela", age:20};

// for(let key in obj){
//   console.log(key, obj[key]);
// }


// let arr=[10,20,30,40]
// arr.sort((a,b)=>b-a);
// console.log(arr[1])

// let arr=[1,2,3,4,5]
// let sum=0;
// for (let i=0; i<arr.length; i++){
//     sum+=arr[i];
// }
// console.log(sum);

// let a=10, b=2;
// [a,b]=[b,a];
// console.log(a,b)

// let a=[1,2,3]
// let b=[5,6,7]
// let merged=[...a,...b].sort((x,y)=>x-y);
// console.log(merged)