import { useState } from "react"

export function Parent(){
    const [count, setCount] = useState(0);
    return(
        <>
        <ChildA count={count}/>
        <ChildB setCount={setCount}></ChildB>
       <ChildC count={count}/>
        </>
    )
}
function ChildA({count}){
    return (
        <h1>Count : {count}</h1>
    )
}
function ChildB({setCount}){
    return (
        <button onClick={()=>setCount((prev)=>prev+1)}>Increment Value</button>
    )
}
function ChildC({count}){
    return(
        <>
        <h1>Cont : {count}</h1>
        </>
    )
}