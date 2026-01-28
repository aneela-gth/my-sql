import React from "react";

export class MountigPhase extends React.Component{
    constructor(){
        super();
        this.state={
            message:"hello here"
        }
        console.log("constructor:whenrver component is created")
    }
     componentDidMount(){
        console.log("ComponentDidMount Phase:Executing")
        setTimeout(()=>{
            this.setState({message:"hello there"})
        },2000)
     }
    render(){
        console.log("render:updating UI")
        return(
            <>
            {this.state.message}
            </>
        )
    }
}