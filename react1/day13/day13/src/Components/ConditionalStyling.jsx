import React from "react";
export class ConditionalStyling extends React.Component{
constructor(){
    super();
    this.state={
        isloggedIn:false
    }
}
    render(){
        if(this.state.isloggedIn){
            return <h1>loggedin succefully</h1>
        }
        else{
            return <h2>plese login as a new user!!!</h2>
        }
   
}
}