import { useState } from "react"

export function EventBinding(){
    // const [count,setcount]=useState(0);
    // const decrement=()=>{
    //     setcount(count-1);
    const greet=(name)=>alert(`hello,${name}`)
    // }
    return(
        <>
          {/* <h1>the count:{count}</h1> */}
           {/* <button onClick={()=>setcount(count+1)}>click here</button> */}
           {/* <button onClick={decrement}>decrement</button> */}
           <h1>the name is {}</h1>
           <button onClick={()=>{greet("aneela")}}>display</button>
        </>
    )
} 