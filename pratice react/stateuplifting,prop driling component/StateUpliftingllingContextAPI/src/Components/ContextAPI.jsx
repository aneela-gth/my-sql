
import { createContext, useState } from "react"
import { Child } from "./Child";
import { Children } from "./Children";
//Create an object w.r.t createContext Hook
export const UserContext = createContext();
export function ContextAPI(){
    const [user, setUser] = useState("Bunty");
    return(
        <>
        <UserContext.Provider value = {{user}}>
        {/* <Child /> */}
        <Children />

        </UserContext.Provider>
        </>
    )
}