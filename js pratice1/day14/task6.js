/////asynchronous function////

// console.log("step1 done");
// setTimeout(()=>{
//     console.log("step2 donye")
// },200)
// console.log("step3 done")


// console.log("step1")
// console.log("set2")
// console.log("set3")


/callback///

function homework(subject,callback){
    setTimeout(()=>console.log("subject"+subject+"home worke is finished"),200)
    callback()

}
function finish(){
    console.log("homework finished")
}
homework("math",finish)


setTimeout(()=>{
    console.log("step one done")
    setTimeout(()=>{
        console.log("step2 is done")
        setTimeout(()=>{
            console.log("step3 is done")
            setTimeout(()=>{
                console.log("step4 is done")
            })
        },200)
    },200)
},200)



function boilwater(callback){
    setTimeout(()=>{
        console.log("boil the water");
        callback()
    },5000)
    
}
function addmaggei(callback){
    setTimeout(()=>{
        console.log("add the maggei");
        callback()

    },2000)

}
function addmasala(callback){
    setTimeout(()=>{
        console.log("add the masala");
        callback()
    },2000)
}
function served(){
    setTimeout(()=>{
        console.log("to serve the everyone")
    })

}
boilwater(()=>{
    addmaggei(()=>{
        addmasala(()=>{
            served()
        })
    })
})