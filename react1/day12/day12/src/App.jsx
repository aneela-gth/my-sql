import React from "react";
import { ChildrenProps } from "./Propes/ChildrenProps";
import { Props1 } from "./Propes/Props1";
// import { Propes } from "./Propes/Propes";
// import CounterApp from "./Components/CounterApp";

function App() {
  const student=["53r","aneela","khammam","MCA"];
  return (
    <>
    {/* <CounterApp/> */}
      {/* <Propes
        eid="120" ename="rani" esalary={25000} edepartement="React Developer" eemail="rani@gmail.com" eate={true}
        eskills={["HTML", "CSS", "JSON", "React"]}
      />
      <Propes eid="121" ename="vani" esalary={30000} edepartement="backend Developer" eemail="vani@gmail.com" eate={true}
        eskills={["python","django"]} ></Propes> */}
      {/* <ChildrenProps name="sundri" age={99} place="chicago" salary="2000" skills={["HTML","CSS","AWS","python"]}></ChildrenProps> */}
      {/* <ChildrenProps name="rani" age={94} place="hyd" salary="2060"><div><h1>ChildrenProps</h1></div></ChildrenProps> */}
      <Props1 student={student} />
    </>
  );
}

export default App;

