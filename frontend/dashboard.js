function openInterviewModal(){

document.getElementById("interviewModal").style.display="flex"

}

function closeInterviewModal(){

document.getElementById("interviewModal").style.display="none"

}

function startInterview(type){

alert("Starting " + type + " Interview")

closeInterviewModal()

}
window.addEventListener("scroll",function(){

const navbar = document.querySelector(".navbar")

if(window.scrollY > 10){
navbar.classList.add("scrolled")
}else{
navbar.classList.remove("scrolled")
}

})

window.addEventListener("resize",()=>{

const canvas = document.getElementById("particles")
if(canvas){
canvas.width = window.innerWidth
canvas.height = window.innerHeight
}

const neural = document.getElementById("neural-network")
if(neural){
neural.width = window.innerWidth
neural.height = window.innerHeight
}

})
function goPerformance(){

window.location.href = "performance.html"

}