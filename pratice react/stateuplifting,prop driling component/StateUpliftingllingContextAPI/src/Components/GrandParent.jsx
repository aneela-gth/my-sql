export function GrandParent(){
    const name = "Bunty";
    return <Parent name = {name}/>
}
function Parent({name}){
    return <Child name={name}/>
}
function Child({name}){
    return <GrandChild name = {name}/>
}
function GrandChild({name}){
    return(
        <>
        <h1>Name: {name}</h1>
        </>
    )
}
