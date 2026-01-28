import React from "react";
export class ConditionalStyling3 extends React.Component{
    constructor(){
        super();
        this.state={
            hadlunch:true
        }
    }
    render(){
          return(
            <>
            {
                this.state.hadlunch && "healthy"
            }
            </>
          )
    }
}