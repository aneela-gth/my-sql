const products=[{
        name:"smartphone",price:"20k",description:"iphone"
    }
]
    return(
        <>
        <h1 className="head" style={{backgroundColor:"purple",color:"white",textAlign:"center"}}>Prodcut-List</h1>
        <ul className="card">
        {
            
            products.map((product)=>(
                
                <h1 style={{textAlign:"center",color:"aqua"}}>name:{product.name} price:{product.price} description:{product.description}</h1>

            ))
        }
        </ul>
        </>
    )


              