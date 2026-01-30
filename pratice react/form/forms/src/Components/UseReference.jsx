import { useRef } from "react"

export function UseReference(){
   const inputRef= useRef(null)
   const handleDate=()=>{
    inputRef.current.focus();
   }
    return(
        <>
        <input type="text" ref={inputRef}></input><br></br><br></br>
        <button onClick={handleDate}>submit</button>
        </>
    )
}