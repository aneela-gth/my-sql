import { useEffect, useState } from "react"

export function UpdatingPhase(){
    const[count,setcount]=useState(0);
    // updating phase
    useEffect(()=>{
        console.log("count updating :",)
    },[count])
    // unmounting phase
    useEffect(()=>{
        return()=>{
    console.log("unmounting phase - 3")
        }
},[])
return(
    <>
    <h2>updating - phase 2</h2>
    <h2>count:{count}</h2>
    <button onClick={()=>setcount(count+1)}>increment</button>
    </>
)
}