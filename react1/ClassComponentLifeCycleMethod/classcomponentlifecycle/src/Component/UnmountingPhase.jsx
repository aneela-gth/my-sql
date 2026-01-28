import React from "react";

export class Unmounting extends React.Component{
    componentDidMount(){
        this.timer=setInterval(() => {
            console.log("timer running");
        }, 1000);
    }
    componentWillUnmount(){
        console.log("unmounting phase executing");
        clearInterval(this.timer)
    }
    render(){
        return(
            <>
            <h1>component unmountig phase</h1>
            </>
        )
    }
}