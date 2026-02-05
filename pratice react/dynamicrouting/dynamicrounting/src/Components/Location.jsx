import { useLocation } from "react-router-dom"

function Location(){
    const location = useLocation()
    return(
        <>
            <h1>Location of the Page : {location.pathname}</h1>
        </>
    )
}
export default Location