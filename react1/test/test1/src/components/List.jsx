export function Listrendering(){
    const students=["Arya","Rahul","suppu","shannu"]
    return(
        <>
        
            <h1 style={{backgroundColor:"black",color:"white",textAlign:"center"}}>Students list</h1>
         <ul type="none" style={{backgroundColor:"pink",color:"blue",textAlign:"center"}}>   
            {
               students.map((name)=>(
                    <li>{name}</li>

                ))
               
            }
        </ul>
        </>
    )}
