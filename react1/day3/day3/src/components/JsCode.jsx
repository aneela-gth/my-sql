// var name="aneela";
// var age=22;
// var city="khammam";
import "./JsCode.css"
function JsCode(){
    // var name="akhila";
    // var age=21;
    // var city="khammam";
    var person={
         name:"akhila",
         age:21,
         city:"khammam",
         study:"betch"
    }
    return(
        <div>
           <h1 className="header1">hello everyone</h1>
           <h2 className="para1">{person.name} is{person.age}, staying in {person.city},study {person.study}</h2>
           <div>
            <h2 style={{color:"white", backgroundColor:"purple",textAlign:"center", }}>Today is monday, sunday already completed</h2>
            <h3 style={{textAlign:"center",color:"black",backgroundColor:"blueviolet"}}>tomorrow is tuesday</h3>
           </div>
        </div>
       
        
    )
}
export default JsCode;