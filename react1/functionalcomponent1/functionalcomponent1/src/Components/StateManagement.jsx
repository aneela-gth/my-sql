import { useState } from "react"

export function StateManagement(){
    const [count,setcount]=useState(0);
    return(
        <>
       <h1>the count :{count}</h1>
       <button onClick={()=>{setcount(count+1)}}>increment</button>
       <button onClick={()=>{setcount(count-1)}}>decrement</button>
        </>
    )
}