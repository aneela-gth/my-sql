import React from "react";

export class EventBinding2 extends React.Component {
  constructor() {
    super();
    this.state = {
      name: "mani",
      gf: "bhavani"
    };
  }

  newgf = () => {
    this.setState({ name: "rani" });
  };

  oldgf = () => {
    this.setState({ name: "mani" });
  };

  naveengf() {
    this.setState({
      gf: "lakshmi"
    });
  }

  render() {
    return (
      <>
        <h1>ram girlfriend name is: {this.state.name}</h1>
        <button onClick={this.newgf}>new girlfriend</button>
        <button onClick={this.oldgf}>old girlfriend</button>

        <h1>naveen girlfriend: {this.state.gf}</h1>
        <button onClick={this.naveengf.bind(this)}>second girlfriend</button>
      </>
    );
  }
}
