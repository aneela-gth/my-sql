
// 1.ifcondicton:

// 1.Check if a number is positive .
var num=12
if(num>0){
    console.log("the number is positve")
}
// 2.Check if a number is even
var num=24
if (num%2==0){
console.log("this number is evven")
}

// Check if a number is greater than 10.
var num2=30
if(num2>10){
console.log("the number is greater than 10")
}

// 2.ifelse:
// Check if a number is even or odd.
var num1=23
if(num1%2==0){
    console.log("the number is evven")
}
else{
    console.log("the number is odd")
}

// Check if a user is eligible to vote (age ≥ 18).
var age=21
if(age>=18){
    console.log("person eligible to vote")
}
else{
    console.log("person not eligible to vote")
}

// Check if a number is greater than 10.
var num2=30
if(num2>10){
console.log("the number is greater than 10")
}
else{
    console.log("the number is not grater then 10")
}

// 3.elseif condiction:

let markes=85
if(markes>=90){
    consolr.log("grade:A")
}
else if(markes>=75){
    console.log("grade:B")
}
else if(markes>=60){
    console.log("grade:C")
}
else{
    console.log("grade:d")
}

//  1. Write a program that takes time (24-hour format) and prints “Good Morning”, “Good Afternoon”, or “Good Evening”

let time = parseInt(prompt("Enter time in 24-hour format (0-23):"));
if(time>=0 & time<12){
    console.log("good morning")
}
else if(time>=12 & time<17){
    console.log("good afternoon")
}
else if(time>=17 & time<23){
    console.log("good evening")
}
else {
    console.log("invalid time entered")
}

// switch:
var grade = 'B';
switch (grade) 
{
    case 'A':
        console.log("Excellent!");
        break;
    case 'B':
        console.log("Good job!");
        break;
    case 'C':
        console.log("Well done!");
        break;
    case 'D':
        console.log("You passed.");
        break;
    case 'F':
        console.log("Better luck next time.");
        break;
    default:
        console.log("Invalid grade.");
}

// task1:
var m=20
if (m>=90 & m<=100){
    console.log("grade is" + A)
}
else if(m<=90 & m>=85){
    console.log("grade is" +B)
}
else if(m<85 & m>=60){
    console.log("grade is" +c)
}
else if(m<60 & m>=35){
    console.log("grade is" +c)
}else {
    console.log("failed")
}


function garde(m){
    
if (m>=90 & m<=100){
    console.log("grade is A")
}
else if(m<=90 & m>=85){
    console.log("grade is B")
}
else if(m<85 & m>60){
    console.log("grade is c")
}
else if(m<60 & m>=35){
    console.log("grade is d")
}else {
    console.log("failed")
}

}
garde(100)


var m=prompt("Enter your marks: ")
    if (m>=90 & m<=100){
       document.write("grade is A")
    }
    else if(m<=90 & m>=85){
       document.write("grade is B")
    }
    else if(m<85 & m>60){
       document.write("grade is c")
    }
    else if(m<60 & m>=35){
       document.write("grade is d")
    }else{
      document.write("failed")
    }

task2
var trafficlight="yellow"
switch(trafficlight){
    case"red":
    console.log("stop")
    brake;
    case"yellow":
    console.log("get ready")
    brake;
    case"green":
    console.log("go")
    brake;
    default:
    console.log("invalid signal")  
}


var trafficlight=prompt("entear trafficlights: ")
switch(trafficlight){
    case"red":
    document.write("stop")
    brake;
    case"yellow":
     document.write("get ready")
    brake;
    case"green":
     document.write("go")
    brake;
    default:
     document.write("invalid signal")  
}

function checksignal(trafficlight){
   switch(trafficlight){
    case"red":
       console.log("stop");
       brake;
    case"yellow":
       console.log("get ready");
       brake;
    case"green":
        console.log("go");
        brake;
    default:
       console.log("invalid signal") ; 
}
}
checksignal("yellow");