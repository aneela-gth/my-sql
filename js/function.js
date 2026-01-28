// //1. greeting function:
// function greetUser(name, times){
// if(times < 1){
//     console.log("warning: times should be at least 1")
// }else{
//     for (let i = 0; i < times; i++){
//         console.log('hello,${"aneela}!');
//     }
// }
// }
// greetUser("aneela",2)

// // 2.Rectangle Area & Perimeter Function
// function retungle(width,height){
//     if(width <0 || height <=0){
//         return "error: width and height must be positive numbers";
//     }
//     const area=width * height;
//     const perimeter=2 * (width + height);
//     return { area:area, perimeter:perimeter};
// }
// console.log(retungle(5,3))

// 3.Flexible String Repeater Function:
// function repeatstring(str,count,separator=""){
//     if(count < 1){
//         return "Error: count should be at least 1.";
//     }
    
//     return Array(count).fill(str).join(separator);
// }
// console.log(repeatString("ha", 3, "-")); 

// function filterByLength(wordList, minLen, maxLen) {
//     if (minLen > maxLen) {
//         let temp = minLen;
//         minLen = maxLen;
//         maxLen = temp;
//     }
//     return wordList.filter(word => word.length >= minLen && word.length <= maxLen);
// }
// const words = ["apple", "cat", "banana", "dog", "elephant", "pen"];
// console.log(filterByLength(words, 3, 6));

// // Parameterized Calculator Function
// function calculate(a,b,operation){
//     switch 
// }
 let arr1=[1,2,3,4]
 let arr2=[5,6,7,8]
 let res= arr1.concate(arr2)
 console.log(res)