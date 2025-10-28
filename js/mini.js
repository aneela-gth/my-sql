let hr=document.getElementById('hour');
let min=document.getElementById('min');
let sec=document.getElementById('sec');

function displayTime(){
let hh=Data.gethours();
let mm=Date.getminutes();
let ss=Date.getseconds();

let hrotation=30*hh + mm/2;
let mrotation=6*mm;
let srotation=6*ss;

hr.style.transform="rotate(${hrrotation}deg)";
min.style.transform="rotate(${mrrotation}deg)";
sec.style.transform="rotate(${srrotation}deg)";
}
setinterval(displayTime,100)