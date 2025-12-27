import React from "react";

export class Statemanagement extends React.Component {
  constructor() {
    super();
    this.state = {
      greeting: "Good Morning"
    };
    

    // binding
    this.handleevent = this.handleevent.bind(this);
  }

  handleevent() {
    this.setState({
      greeting: "Good Afternoon"
    });
  }

  render() {
    return (
      <>
        <h1>{this.state.greeting}</h1>
        <button onClick={this.handleevent}>Click me</button>
      </>
    );
  }
}
