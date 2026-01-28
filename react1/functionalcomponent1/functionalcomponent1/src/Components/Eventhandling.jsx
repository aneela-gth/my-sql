import { useState } from "react"

export default function EventHandling(){
    const[name,setname]=useState("");
    const handlename=(event)=>{
        setname(event.target.value);
    }
    return(
        <>
        {/* <button onClick={()=>{alert("hiii, hello everybody")}}>click here </button> */}

            <input type="text" placeholder="enter your name" onChange={handlename}></input>
            <h1>{name}</h1>
       
        </>
    )
}