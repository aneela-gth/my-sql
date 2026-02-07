import { UserContext } from "./ContextAPI";

export function Children(){
    return(
        <>
        <UserContext.Consumer >
            {({user})=><h1>Hello, {user}</h1>}
        </UserContext.Consumer>

        </>
    )
}