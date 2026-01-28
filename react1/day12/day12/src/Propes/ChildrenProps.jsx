import React from "react"
 export class ChildrenProps extends React.Component{
    render(){
        return(
            <>
            <div    style={{ border: "2px solid #333", width: "300px", padding: "15px",
            margin: "20px auto",backgroundColor: "#e6eb4bff",borderRadius: "8px",textAlign: "center"
          }}>
            <h2>{this.props.name}</h2>
            <h2>{this.props.age}</h2>
            <h2>{this.props.place}</h2>
            <h2>{this.props.salary}</h2>
            {/* <h2>{this.props.skills}</h2> */}
            <ul>
            {
                this.props.skills.map((item,index)=>(
                    // <p key={index}>{item}</p>
                    <li key={index}>{item}</li>
                ))
            }
            </ul>
            <h2 style={{color:"black",fountsize:"10px",backgroundColor:"pink"}}>{this.props.children}</h2>
            
            </div>
            </>
        )
    }
}