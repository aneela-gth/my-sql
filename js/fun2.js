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