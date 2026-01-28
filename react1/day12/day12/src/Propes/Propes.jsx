import React from "react";

export class Propes extends React.Component {
  render() {
    const containerStyle = {
      width: "420px",
      margin: "30px auto",
      padding: "20px",
      borderRadius: "12px",
      backgroundColor: "#f5f7fa",
      boxShadow: "0 6px 15px rgba(0, 0, 0, 0.15)",
      fontFamily: "Arial, sans-serif"
    };

    const headingStyle = {
      textAlign: "center",
      color: "#2c3e50",
      marginBottom: "15px"
    };

    const textStyle = {
      fontSize: "16px",
      margin: "8px 0",
      color: "#34495e"
    };

    return (
      <div style={containerStyle}>
        <h1 style={headingStyle}>Employee Details</h1>

        <p style={textStyle}>EId: {this.props.eid}</p>
        <p style={textStyle}>EName: {this.props.ename}</p>
        <p style={textStyle}>ESalary: ₹{this.props.esalary}</p>
        <p style={textStyle}>EDepartment: {this.props.edepartement}</p>
        <p style={textStyle}>EEmail: {this.props.eemail}</p>
        <p style={textStyle}>
          EActive: {this.props.eate ? "Active" : "Not Active"}
        </p>
        <p style={textStyle}>
          ESkills: {this.props.eskills.join(", ")}
        </p>
      </div>
    );
  }
}
