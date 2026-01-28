import React from "react";
export class ConditionlRendering1 extends React.Component{
constructor(){
    super();
    this.state={
        ismorning:true
    }
}
    render(){
    return(
        <>
        {
            this.state.ismorning? "goodmorning": "goog evenging"
        }
        </>
    )
}
}