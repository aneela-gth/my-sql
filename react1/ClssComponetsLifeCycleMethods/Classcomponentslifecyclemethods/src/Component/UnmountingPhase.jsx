import React from "react";

export class Unmounting extends React.Component {
  componentDidMount() {
    this.timer = setInterval(() => {
      console.log("Timer running...");
    }, 1000);
  }

  componentWillUnmount() {
    clearInterval(this.timer);
    console.log("Component unmounted, timer cleared");
  }

  render() {
    return (
      <div>
        <h2>Unmounting Phase Component</h2>
      </div>
    );
  }
}

