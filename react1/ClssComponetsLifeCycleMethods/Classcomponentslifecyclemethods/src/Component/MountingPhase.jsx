import React from "react";

export class MountingPhase extends React.Component {
  constructor() {
    super();
    this.state = {
      message: "hello here"
    };
    console.log("constructor : whenever component is created");
  }
componentDidMount(){
    console.log("componentdidMount Phase:Executing")
    setTimeout(()=>{
        this.setState({message:"hello there"})
    },200)
}
  render() {
    console.log("render: updating UI");

    return (
      <div>
        <h2>{this.state.message}</h2>
      </div>
    );
  }
}

