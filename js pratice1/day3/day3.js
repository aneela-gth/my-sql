
var arr=[1,2,3,4,5,]
arr.push(20)
console.log(arr)

// var arr1=[10,20,30,40,50]
// arr1.pop()
// console.log(arr1)

// var arr2=["aneela","akhila","nani","vani"]
// arr2.unshift("suppu")
// console.log(arr2)

// var arr3=["aneela","akhila","nani","vani"]
// arr3.shift()
// console.log(arr3)

// var arr4=["aneela","akhila","nani","vani"]
// console.log(arr4.length)

// var arr5=["aneela","akhila","nani","vani"]
// var index=arr5.indexOf("aneela")
// console.log(index)

// var arr6=["aneela","akhila","nani","nari","mani","vasu"]
// console.log(arr6.slice(1,4))

//  var arr7=[10,20,30,40,50]
//  arr7.splice(2,1,35)
//  console.log(arr7)

// var arr7=["aneela","nari","akhila","ram"]
// arr7.splice(2,1,"navi")
// console.log(arr7)

// var arr8=[1,2,3,4,5,6,7,9,8]
// var op=arr8.map(function(x){return x*2;})
// console.log(op)

// var arr9=[1,2,3,4,5]
// var arr10=[6,7,8,9,10]
// console.log(arr9.concat(arr10))

// var arr1=[1,9,2,3,4,5,6,7,8]
// arr1.toString()
// console.log(arr1.toString())

// var arr2=[9,8,3,5,2,1,4,6,7]
// console.log(arr2.join('-'))

// var arr3=[9,8,3,5,2,1,4,6,7]
// console.log(arr3.includes(0))

// var arr4=[9,8,3,5,2,1,4,6,7]
// var result=arr4.find(function(x){return x>3;});
// console.log(result)

// var arr5=[9,8,3,5,2,1,4,6,7]
// var index=arr5.findIndex(function(x){return x>3;});
// console.log(index)



// 1. Array Basics
//  1. Create an array of 5 colors and print the second and last color.
// var arr=["blue","red","green","pink","black"]
// console.log(arr)
// console.log(arr[1]);
// console.log(arr[4]);

//2. Create an array of numbers and replace the first element with 100.
// arr.unshift(100);
// console.log(arr);

// 3. Create an array with mixed data types (string, number, boolean). Print the type of each element using a loop.
// var arr=["aneela",23,true]
// for()
// console.log(type(arr));


// 4. Create a nested array and print the inner array’s second element
// let nested_arr=[
//     [1,2,3,4,5],
//     ["apple","banana","mango"],
//     ["aneela",23,5.6,"true"]
// ]
// console.log(nested_arr[2]);
// console.log(nested_arr[1]);

//5. Create an array using the Array constructor and display its length.
// var arr=[40,50,60,70,80]
// console.log(arr)

// push(), pop(), shift(), unshift()

//  6. Create an array of fruits and add one fruit at the end using push().
// var fruitrs=["apple","mango","cherry","banana"];
// fruitrs.push("pineapple");
// console.log(fruitrs);

//7. Remove the last element from the array using pop() and display the updated array.
// let arr=["aneela","neru","megi","suppu","sree"]
// arr.pop();
// console.log(arr)

// 8. Add two new fruits at the beginning using unshift().
// let arr=["ram","anu","vani","manu"]
// arr.push("raju","mani");
// console.log(arr)

// 9. Remove the first element using shift() and print the new array.
// let arr=["ram","anu","raju","anju","vani"]
// arr.shift();
// console.log(arr);

// 10. Use a combination of push() and pop() to keep only 3 elements in your array.
// arr=["apple","banana","mango","cherry"]
// arr.push("pineaple");
// arr.pop();
// console.log(arr)

// 3. slice() and splice()
// 11. Create an array [10, 20, 30, 40, 50] and use slice() to extract [20, 30].
//  var array=[10,20,30,40,50]
//  console.log(array.slice(1,3))

// 12. Using the same array, use splice() to replace 30 with 35.
//    var array=[10,20,30,40,50]
//    array.splice(2,1,35)
//    console.log(array)

// 13. Insert 25 before 30 using splice().
// array=[10,20,30,40,50]
// array.splice(2,0,25);
// console.log(array)

// 14. Remove the last two elements using splice().
// array=[10,20,30,40,50]
// console.log(array.splice(0,3));

//   15. Use slice() to copy the first three elements into a new array.
// var arr=[10,20,30,40,50]
// new_arr=[];
// new_arr.splice(0,3);
// console.log(new_arr);

//  concat(), join(), toString()
// 16. Create two arrays [1,2,3] and [4,5,6] and merge them using concat().
// var arr1=[1,2,3]
// var arr2=[4,5,6]
// console.log(arr1.concat(arr2));

//  17. Convert an array of names into a string separated by commas using join().
// var arr=[10,20,30,40,50]
// console.log(arr.join('-'));

//  18. Use toString() on an array and display the output.
// var arr=[1,2,3,4,5,6]
// console.log(arr.toString())

//  19. Merge three arrays using concat() and find the length of the new array.
// var arr1=["apple","banana","pineaple"]
// var arr2=["ramu","vani","gopi"]
// console.log(arr1.concat(arr2));

// 20. Create an array of city names and join them using ' - ' as a separator.
// var arr=[1,2,3,4,5,6,7,8]
// console.log(arr.join('-'));

// 5. Search Methods (indexOf, lastIndexOf, includes)
//21. Create an array ['apple', 'banana', 'orange', 'banana', 'grape'] and find the first index of 'banana'.
// var array =['apple', 'banana', 'orange', 'banana', 'grape']
// console.log(array.indexOf('banana'));

//  22. Find the last index of 'banana' using lastIndexOf().

// var array =['apple', 'banana', 'orange', 'banana', 'grape']
// console.log(array.lastIndexOf('banana'));

// 23. Check if 'mango' exists in the array using includes().
// arr=["apple","banana","oreange"]
// console.log(arr.includes("mango"));

//  24. Write code to check if a specific number exists in an array, if not, push it.
//  25. Use includes() to verify if 'kiwi' is present in your fruit array and print a message accordingly.
//  var arr=["apple","banana","oreange"]
// console.log(arr.inciudes("kiwi"));

// find() and findIndex()
//  26. Create an array [5, 12, 8, 130, 44] and find the first number greater than 10.
// var numbers=[5,12,8,130,44]
// let result = numbers.find(num => num > 10);
// console.log(result);

// 27. Use findIndex() to locate the position of the first element greater than 50.
// let numbers=[5,12,8,130,44]
// let result=numbers.findIndex(num=>num>50);
// console.log(result);
