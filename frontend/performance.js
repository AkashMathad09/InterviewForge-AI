/* SCORE TREND CHART */

const scoreChart = new Chart(
document.getElementById('scoreChart'),
{
type: 'line',
data: {

labels: ['Interview 1','Interview 2','Interview 3','Interview 4','Interview 5'],

datasets: [{
label: 'Score',

data: [55, 65, 60, 75, 82],

borderColor: '#6366f1',

backgroundColor: 'rgba(99,102,241,0.2)',

fill:true,

tension:0.4
}]
},

options:{
responsive:true,
plugins:{
legend:{display:false}
},
scales:{
y:{
beginAtZero:true,
max:100
}
}
}
}
);


/* SKILL PERFORMANCE */

const skillChart = new Chart(
document.getElementById('skillChart'),
{
type: 'radar',

data:{

labels:[
'Technical',
'Problem Solving',
'Communication',
'Confidence',
'System Design'
],

datasets:[{

label:'Skill Level',

data:[80,70,65,75,60],

backgroundColor:'rgba(34,197,94,0.2)',

borderColor:'#22c55e'

}]

},

options:{
responsive:true,
plugins:{
legend:{display:false}
}
}

}
);