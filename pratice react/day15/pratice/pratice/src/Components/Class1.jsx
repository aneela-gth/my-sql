import React from "react";

// export class Class1 extends React.Component {
//   name = "aneela";

//   render() {
//     return (
//       <>
//         <h1>Hello</h1>
//         <h2>My name is {this.name}</h2>
//       </>
//     );
//   }
// }


/////// Using state in a Class Component (important 🔥)///////

class Class1 extends React.Component {
  constructor() {
    super();
    this.state = {
      name: "Aneela"
    };
  }

  render() {
    return (
      <>
        <h1>Hello</h1>
        <h2>My name is {this.state.name}</h2>
      </>
    );
  }
}

export default Class1;
