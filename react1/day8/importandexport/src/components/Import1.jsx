 
//  default export//
 export default function Import1(){
   return(
    <div>
        <h1 style={{backgroundColor:"yellow", color:"brown",textAlign:"center"}}>
           Lorem, ipsum dolor sit amet consectetur adipisicing elit.
            Culpa ex fugit provident sed dolorum mollitia veritatis,
             dolore voluptatem ad ipsam a in sint corporis praesentium,
              nobis tempore facilis, eius voluptatibus.
        </h1>
        <h3 style={{color:"white", backgroundColor:"black",textAlign:"center",padding:"10px"}}>i love my mom and dad</h3>
        <Import2></Import2>
    </div>
   ) 
}
function Import2(){
    return(
        <h1 style={{color:"blue",backgroundColor:"pink",textAlign:"center"}}>welcome to react class </h1>
    )
}
// --------------------------------------------------
// variable components//

export const Box=()=>{
    return(
        <marquee scrollamount="30px" direction="right" behavior="alternate"style={{backgroundColor:"aqua",textAlign:"center" ,color:"black",padding:"10px",margin:"10px",fontSize:"50px"}}>products are available in the box</marquee>
    )
}
// ----------------------------------------------------
// named export///
export function Content(){
     return(
        <div >
            <h1 style={{backgroundColor:"greenyellow",color:"",textAlign:"center"}}>hello</h1>
            <Footer/>
            </div>
        
     )
}
export function Footer(){
     return(
        <h1 style={{backgroundColor:"blue",color:"pink",textAlign:"center"}}>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates voluptatum sed excepturi quod veritatis iusto iure, sequi porro ad maiores magni delectus inventore, sapiente ducimus aspernatur pariatur, repellat sit quos.</h1>
     )
}
