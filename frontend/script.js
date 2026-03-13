/* wait for page to load */

window.onload = function(){

/* ================= PARTICLE BACKGROUND ================= */

const particleCanvas = document.createElement("canvas")
particleCanvas.id = "particles"
document.body.appendChild(particleCanvas)

const pctx = particleCanvas.getContext("2d")

particleCanvas.width = window.innerWidth
particleCanvas.height = window.innerHeight

let particles = []

for(let i=0;i<80;i++){

particles.push({
x:Math.random()*particleCanvas.width,
y:Math.random()*particleCanvas.height,
size:Math.random()*2,
speedX:(Math.random()-0.5)*0.5,
speedY:(Math.random()-0.5)*0.5
})

}

function animateParticles(){

pctx.clearRect(0,0,particleCanvas.width,particleCanvas.height)

particles.forEach(p=>{

p.x += p.speedX
p.y += p.speedY

if(p.x < 0 || p.x > particleCanvas.width) p.speedX *= -1
if(p.y < 0 || p.y > particleCanvas.height) p.speedY *= -1

pctx.beginPath()
pctx.arc(p.x,p.y,p.size,0,Math.PI*2)
pctx.fillStyle="rgba(255,255,255,0.7)"
pctx.fill()

})

requestAnimationFrame(animateParticles)

}

animateParticles()


/* ================= NEURAL NETWORK BACKGROUND ================= */

const neuralCanvas = document.getElementById("neural-network")

if(neuralCanvas){

const nctx = neuralCanvas.getContext("2d")

neuralCanvas.width = window.innerWidth
neuralCanvas.height = window.innerHeight

let nodes = []

const nodeCount = 70

for(let i=0;i<nodeCount;i++){

nodes.push({
x:Math.random()*neuralCanvas.width,
y:Math.random()*neuralCanvas.height,
vx:(Math.random()-0.5)*0.6,
vy:(Math.random()-0.5)*0.6
})

}

function drawNetwork(){

nctx.clearRect(0,0,neuralCanvas.width,neuralCanvas.height)

for(let i=0;i<nodes.length;i++){

let node = nodes[i]

node.x += node.vx
node.y += node.vy

if(node.x < 0 || node.x > neuralCanvas.width) node.vx *= -1
if(node.y < 0 || node.y > neuralCanvas.height) node.vy *= -1

nctx.beginPath()
nctx.arc(node.x,node.y,2,0,Math.PI*2)
nctx.fillStyle="rgba(255,255,255,0.7)"
nctx.fill()

for(let j=i+1;j<nodes.length;j++){

let dx = node.x - nodes[j].x
let dy = node.y - nodes[j].y
let distance = Math.sqrt(dx*dx + dy*dy)

if(distance < 120){

nctx.beginPath()
nctx.moveTo(node.x,node.y)
nctx.lineTo(nodes[j].x,nodes[j].y)
nctx.strokeStyle="rgba(255,255,255,0.08)"
nctx.stroke()

}

}

}

requestAnimationFrame(drawNetwork)

}

drawNetwork()

}


/* ================= TYPING TEXT ================= */

const typingElement = document.getElementById("typing-text")

if(typingElement){

const text = "AI Powered Mock Interview Platform."

let index = 0
const speed = 40

function typeText(){

if(index < text.length){

typingElement.innerHTML += text.charAt(index)

index++

setTimeout(typeText,speed)

}

}

typeText()

}

}


/* ================= PASSWORD TOGGLE ================= */

function togglePassword(){

const password = document.getElementById("password")

if(password.type === "password"){
password.type = "text"
}else{
password.type = "password"
}

}


/* ================= LOGIN TRANSITION ================= */

function openLogin(){

document.querySelector(".left-panel").style.display="none"

const login = document.querySelector(".login-card")

login.style.display="block"

document.querySelector(".main-container").style.justifyContent="center"

}
function showLogin(){

const login = document.querySelector(".login-card")
const signup = document.querySelector(".signup-card")

login.style.transform = "translateX(0)"
login.style.opacity = "1"

signup.style.transform = "translateX(120%)"
signup.style.opacity = "0"

}

function showSignup(){

document.querySelector(".login-card").style.display="none";

const signup = document.querySelector(".signup-card");
signup.style.display="block";

}

function showLogin(){

document.querySelector(".signup-card").style.display="none";

const login = document.querySelector(".login-card");
login.style.display="block";

}
/* ================= RESIZE FIX ================= */

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
function createAccount(){

const email = document.querySelector('.signup-card input[type="email"]').value
const password = document.querySelector('.signup-card input[type="password"]').value

if(email === "" || password === ""){
alert("Please fill all fields")
return
}

const user = {
email: email,
password: password
}

localStorage.setItem("mockmateUser", JSON.stringify(user))

alert("Account created successfully! Please login.")

showLogin()

}


function goDashboard(){

const email = document.querySelector('.login-card input[type="email"]').value
const password = document.querySelector('#password').value

const storedUser = JSON.parse(localStorage.getItem("mockmateUser"))

if(!storedUser){
alert("No account found. Please create an account first.")
return
}

if(email === storedUser.email && password === storedUser.password){

window.location.href = "dashboard.html"

}else{

alert("Invalid email or password")

}

}