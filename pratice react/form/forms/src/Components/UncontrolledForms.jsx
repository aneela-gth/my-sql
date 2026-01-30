import { useRef } from "react"

 export function UncontrolledForms(){
    const inputRef=useRef();
    const handleDate=()=>{
        alert(`Hello, I'm From,$(inputRef.current.value)`)
    }
    return(
        <>
        <input type="text" placeholder="Enter your place" ref={inputRef}></input><br></br><br></br>
        <button onClick={handleDate}>Submit</button>
        </>
    )
}