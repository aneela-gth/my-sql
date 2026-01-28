import './Styling.css'
export function CondStyling(){
    const isloggedIn = true;
    return(
        <div>
            {
                isloggedIn ? <p className = {isloggedIn ? "login" : "logout"}>Successfully LoggedIn</p> : <p>Failed To Login</p>
            }
        </div>
    )
}