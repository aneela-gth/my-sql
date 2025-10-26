//  Task 1: Character Finder
// 1.The character at index 4
// let str="javascript"
// console.log(str.charAt(4));

// 2.The ASCII value of the character at index 2
// let str="javascript"
// console.log(str.charCodeAt(2))

// 3.The last character using a negative index with .at()
// let str="javascript"
// console.log(str.at(-1))

//  Task 2: Combine & Search

// 1.Combines 'Hello' and 'World' using concat()
// let str="hello"
// let  str1="world"
// console.log(str.concat(str1))

//  2.Checks if the final string includes 'lo'
// let str="hello"
// console.log(str.includes("lo"))

//  3.Finds the first and last index of 'l'
// let str="hello"
// console.log(str.indexOf("l"))
// console.log(str.lastIndexOf("l"))

//  Task 3: Text Formatting
// let str="    javascript methods     "
// console.log(str.trim())
// console.log(str.trimStart())
// console.log(str.trimEnd())
// console.log(str.toUpperCase())

//  Task 4: Extract Substrings
// let str="learning javascript is fun!"
// console.log(str.slice(9,19))
// console.log(str.substring(0,8))

//  Task 5: Padding Magic
// let str="50"
// console.log(str.padStart(5,"0"))
// console.log(str.padEnd(10,"*"))

//  Task 6: Replace & Compare
// let str='I love JavaScript, JavaScript is powerful!'
// console.log(str.replace("JavaScript","js"))
// console.log(str.localeCompare("JavaScript","JS"))
// console.log(str.replaceAll('I love JavaScript, JavaScript is powerful!',"i love js,js is powerful"))


// 🎯 Task 7: Mixed Operations (Mini Project)
// function string(str){
//     let s=str.trim();
//     return{
//         length:s.length,
//         firstChar: trimmedStr[0],  
//         lastChar:trimmedSt[s.length - 1], 
//     }

// }
// console.log(analyzeString("   I am learning JS with fun!   "));


// startsswith:
var str="warangal"
console.log(str.startsWith("w"))
console.log(str.startsWith("a"))
// endswith
var str1="goa"
console.log(str1.endsWith("a"))
console.log(str1.endsWith("g"))
// repeat
var str2="aneela"
console.log(str2.repeat(2))
// split
var str3="1,2,3"
console.log(str3.split(" ,"))