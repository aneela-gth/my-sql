export function CondictionalRendering({ isloggedIn }) {
//   if (isloggedIn) {
//     return <h1>Welcome to web page!!!</h1>;
//   } else {
//     return <h1>Please login!!!</h1>;
//   }

return(
    <>
    {/* {isloggedIn ? "welcome to the web page":"please login"} */}
    {isloggedIn && <h2><i><b>welcome to web page</b></i></h2>}
    </>
)
}