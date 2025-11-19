// 1.Create an object named student with properties: name, age, course, and marks.
// let student={name:"aneela",age:23,course:"pythonfullstack",marks:70}
// console.log(student)

// 2.Add a new property grade and modify the marks value.
// const student={name:"aneela",age:23,course:"pythonfullstack",marks:70}
// student.grade="A";
// student.marks=85;
// console.log(student);

// 3.Use Object.keys() and Object.values() to display all property names and their values separately
// const student={name:"aneela",age:23,course:"pythonfullstack",marks:70};
// console.log(Object.keys(student));
// console.log(Object.values(student));

// 4.Use Object.entries() to print key–value pairs together in array format.
// const student={name:"aneela",age:23,course:"pythonfullstack",marks:70};
// const entries=Object.entries(student);
// console.log(entries)

// 5.Create another object extraDetails with properties like city and rollNo,
//  and merge it into the student object using Object.assign().
// const student1={name:"aneela",age:23,course:"pythonfullstack",marks:70};
// const student2={city:"hyd",rollno:102};
// Object.assign(student1,student2);
// console.log(student1);

// 6.Use Object.hasOwnProperty() to check if the student object has the property course and address.
// const student1={name:"aneela",age:23,course:"pythonfullstack",marks:70};
// console.log(student1.hasOwnProperty("course"));
// console.log(student1.hasOwnProperty("address"));

// udent object and apply Object.freeze() on it. Try adding or modifying properties and observe that no changes happen.7.Make a copy of the st
// const student={
//     name:"aneela",
//     age:23,
//     course:"python",
//     marks:70
// }
// const frozenStudent = { ...student };
// Object.freeze(frozenStudent);
// frozenStudent.marks = 90;  
// frozenStudent.grade = "A";  
// delete frozenStudent.course; 
// console.log("Frozen Student:", frozenStudent);
// console.log("Is object frozen?", Object.isFrozen(frozenStudent));



// Apply Object.seal() on another copy of the object and verify that:
// You cannot add or delete properties,
// But you can modify existing values.
const student = {
  name: "Aneela",
  age: 23,
  course: "Python Full Stack",
  marks: 70
};
const sealedStudent = {student };
Object.seal(sealedStudent);
sealedStudent.grade = "A";
delete sealedStudent.course;
sealedStudent.marks = 85;
console.log(sealedStudent);