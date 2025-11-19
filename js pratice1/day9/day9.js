
// 1.globalscope:
var a=86;
function fun_name(){
  console.log(a);  //value inside the  function
  if(true){
    console.log(a)  //value inside the block
  }
}
console.log(a)
fun_name();  


// 2.localscope:

function add(){
  var name="sunny";
    console.log(`the boy name is: ${name}`);
if(20==20){
    console.log(`the boy name is:${name}`);
  }
  console.log(name)
}
add();

// 3.blockscope:

function number(){
  if(true){
    var name="naveen"
    console.log("naveen likes mysore bonda")
  }
}
// number();

function number(){
  if(true){
    var name="naveen"
    console.log(name+"likes mysore bonda")
  }
  console.log(name+"likes mysore bonda")
}
number();


// 4.lexical scope:

function parent(){
  var a=96;
  function child(){
    var b=24;
    var c=a+b;
    console.log(c)
  }
  child()
}
parent()


// problem statement:
// // ----------------------------------------------------------------------
// 1.given 3 int values a,b,c returns their sum.
// condiction1:if  any one value of addEventListener a,b,c is 13 then it should not return their sum
// condiction2:if a value is 13 then return 0 as sum.
// condiction3:if b is 13, then return a value.

function add(a,b,c){
 
    if(a==13){
    return0
    }
    else if(b==13){
        return a;
    }
    else if(a==13||b==13||c==13){
      return" add 13 is not avilable"
    }
}
console.log(add(1,13,13))

// clousers:
// its accessing the variables from the outer function inside the inner function
function outer(){
  var a=10;
  function inner(){
    console.log(a)
  }
  return inner;
}
var result=outer();
result


// even after thr confirmmpletion of the outerfunction execution, it will be holding the variable DataTransfer.