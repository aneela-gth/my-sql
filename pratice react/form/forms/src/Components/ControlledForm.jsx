import { useState } from "react"

export function ControlledFrom(){
    const[name,setname]=useState("");
    const handleDate=(e)=>{
        e.preventDefault;
        alert(`Hello,${name}`);
    }
    return(
        <>
        <form onsubmit={handleDate}>
             <input type="text" value={name} onChange={(e)=>setname(e.target.value)} placeholder={(e)=>setname(e.target.value)}></input><br></br><br></br>
             <button>submit</button>
        </form>
      
        </>
    )
}

