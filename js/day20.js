// 1. Math.abs()
var num = -10;
console.log(Math.abs(num));


// 2. Math.ceil()
var num1=5.4;
console.log(Math.ceil(num1))

// 3. Math.floor()
var num2=6.7;
console.log(Math.floor(num2))

// 4. Math.round()
var num3=3.3
var num4=5.4
console.log(Math.round(num3))
console.log(Math.round(num4))

// 5. Math.trunc()
var num5=7.9
console.log(Math.trunc(num5))

// 6. Math.max() & Math.min()
var num6=(1,45,7,24,66,346,23,2,8)
console.log(Math.max(1,45,7,24,66,346,23,2,8))
console.log(Math.min(1,45,7,24,66,346,23,2,8))

// 7. Math.pow()
console.log(Math.pow(2,3))

// 8. Math.sqrt()
var num10=4
console.log(Math.sqrt(4))

// 9. Math.random()
console.log(Math.random())

//number methods:
// 1.tofixed:
var num=56.9876543
console.log(num.toFixed(4))

// 2.parseint:
var num1="123abc"
console.log(Number.parseInt(num1))
var num2="3.45"
console.log(Number.parseInt(num2))

// 3. parseFloat()
var num3="123.44gh"
console.log(Number.parseFloat(num3))
var num4="le4"
console.log(Number.parseFloat(num4))

// 4. isNaN()
var num5="hello"
console.log(isNaN(num5))
var num6=34
console.log(isNaN(num6))
var number="56"
console.log(isNaN(number))

// 5. Number()
var num="345"
console.log(Number(num))
console.log(Number.isNaN(NaN))

// 6.Number.isFinite:
var num10=123
console.log(Number.isFinite(num10))
