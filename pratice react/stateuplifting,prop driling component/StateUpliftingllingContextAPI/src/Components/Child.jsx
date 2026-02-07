import { useContext } from "react"
import { UserContext } from "./ContextAPI"

export function Child(){
   const {user, setUser} = useContext(UserContext);

    return(
        <>
        <h1>Hello, {user}</h1>
         <button onClick={()=>setUser("React Developer")}>Change Name</button>
        {/* <button onClick={()=>setUser("React Developer")}>Change Name</button> */}

        </>
    )
}