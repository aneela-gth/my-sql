import React from "react";

export class Props1 extends React.Component {
  render() {
    return (
      <>
        <h2>Student Details</h2>
        {this.props.student.map((item, index) => (
          <p key={index}>{item}</p>
        ))}
      </>
    );
  }
}
8