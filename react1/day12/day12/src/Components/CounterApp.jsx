import React from "react";

export default class CounterApp extends React.Component {
  constructor() {
    super();
    this.state = {
      count: 0
    };
    this.reset = this.reset.bind(this);
  }

  increment = () => {
    this.setState({
      count: this.state.count + 1
    });
  };

  decrement = () => {
    this.setState({
      count: this.state.count - 1
    });
  };

  reset = () => {
    this.setState({
      count: 0
    });
  };

  render() {
    return (
      <>
        <div
          style={{
            textAlign: "center",
            marginTop: "50px",
            background: "#c8e987ff",
            padding: "30px",
            borderRadius: "10px",
            width: "300px",
            margin: "auto",
         
            
          }}
        >
          <h1 style={{ color: "blue" }}>Counter: {this.state.count}</h1>

          <button
            onClick={this.increment}
            style={{
              padding: "10px 20px",
              margin: "10px",
              background: "green",
              color: "white",
              border: "none",
              borderRadius: "5px",
              cursor: "pointer"
            }}
          >
            Increment
          </button>

          <button
            onClick={this.decrement}
            style={{
              padding: "10px 20px",
              margin: "10px",
              background: "red",
              color: "white",
              border: "none",
              borderRadius: "5px",
              cursor: "pointer"
            }}
          >
            Decrement
          </button>

          <button onClick={this.reset} style={{padding: "10px 20px",margin: "10px", background: "orange",
              color: "white",
              border: "none",
              borderRadius: "5px",
              cursor: "pointer"
            }}
          >
            Reset
          </button>
        </div>
      </>
    );
  }
}
