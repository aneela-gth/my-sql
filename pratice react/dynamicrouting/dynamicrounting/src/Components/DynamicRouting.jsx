import { useParams } from "react-router-dom"

export function DynamicRouting(){
    const {id} = useParams();
    return(
        <>
        <h1>User Profile</h1>
        <p>The serial number of the User is {id}</p>
        </>
    )
}