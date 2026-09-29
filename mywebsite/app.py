from flask import Flask, render_template_string, abort

app = Flask(__name__)

players = {
    # ================= KBM =================

    "Peterbot": {
        "input": "KBM",
        "dpi": "800", "x": "6.4%", "y": "6.4%",
        "target": "45%", "scope": "45%",
        "wall": "T", "floor": "Y", "stairs": "F",
        "roof": "V", "edit": "G / Mouse Wheel Down"
    },

    "Pollo": {
        "input": "KBM",
        "dpi": "800", "x": "6.4%", "y": "6.4%",
        "target": "30%", "scope": "30%",
        "wall": "—", "floor": "—", "stairs": "—",
        "roof": "—", "edit": "—"
    },

    "Veno": {
        "input": "KBM",
        "dpi": "800", "x": "6.3%", "y": "6.3%",
        "target": "45%", "scope": "45%",
        "wall": "Mouse 5", "floor": "Q",
        "stairs": "Mouse 4", "roof": "C", "edit": "F"
    },

    "Queasy": {
        "input": "KBM",
        "dpi": "800", "x": "6.6%", "y": "6.6%",
        "target": "29%", "scope": "32%",
        "wall": "Q", "floor": "R", "stairs": "T",
        "roof": "Mouse 5", "edit": "F / Mouse Wheel Up"
    },

    "Clix": {
        "input": "KBM",
        "dpi": "800", "x": "8.7%", "y": "6.3%",
        "target": "60%", "scope": "35%",
        "wall": "—", "floor": "—", "stairs": "—",
        "roof": "—", "edit": "—"
    },

    "Bugha": {
        "input": "KBM",
        "dpi": "800", "x": "6.4%", "y": "6.4%",
        "target": "45%", "scope": "45%",
        "wall": "X", "floor": "V", "stairs": "C",
        "roof": "L-Shift", "edit": "F / Mouse Wheel Down"
    },

    "Mongraal": {
        "input": "KBM",
        "dpi": "1600", "x": "3.2%", "y": "3.2%",
        "target": "27.5%", "scope": "27.5%",
        "wall": "Mouse 5", "floor": "Q",
        "stairs": "Mouse 4", "roof": "L-Shift",
        "edit": "F / Mouse Wheel Down"
    },

    "MrSavage": {
        "input": "KBM",
        "dpi": "800", "x": "9.1%", "y": "9.1%",
        "target": "49%", "scope": "49%",
        "wall": "F", "floor": "G", "stairs": "T",
        "roof": "L-Shift", "edit": "R"
    },

    

    "Acorn": {
        "input": "KBM",
        "dpi": "1600", "x": "3.4%", "y": "3.4%",
        "target": "50%", "scope": "50%",
        "wall": "Mouse 4", "floor": "X",
        "stairs": "Mouse 5", "roof": "Q",
        "edit": "F / Mouse Wheel Down"
    },

    "Cold": {
        "input": "KBM",
        "dpi": "800", "x": "6.4%", "y": "6.4%",
        "target": "34.9%", "scope": "34.9%",
        "wall": "Mouse 5", "floor": "Q",
        "stairs": "Mouse 4", "roof": "X",
        "edit": "F / Mouse Wheel Down"
    },

    "Khanada": {
        "input": "KBM",
        "dpi": "800", "x": "7.0%", "y": "7.0%",
        "target": "40%", "scope": "40.1%",
        "wall": "F1 / C", "floor": "F2 / X",
        "stairs": "F3 / V", "roof": "Mouse 5", "edit": "F"
    },

    "vico": {
    "input": "KBM",
    "dpi": "800", "x": "5.5%", "y": "5.5%",
    "target": "35%", "scope": "35%",
    "wall": "C", "floor": "X",
    "stairs": "Mouse 5", "roof": "L-Shift",
    "edit": "E / Mouse Wheel Down"
},

    "Setty": {
        "input": "KBM",
        "dpi": "800", "x": "6.4%", "y": "6.4%",
        "target": "40%", "scope": "40%",
        "wall": "Mouse 5", "floor": "V",
        "stairs": "Mouse 4", "roof": "L-Shift", "edit": "F"
    },

    "Malibuca": {
        "input": "KBM",
        "dpi": "1600", "x": "3.5%", "y": "3.5%",
        "target": "50.1%", "scope": "50.1%",
        "wall": "Q", "floor": "V",
        "stairs": "F", "roof": "L-Shift", "edit": "E"
    },

    "Merstach": {
        "input": "KBM",
        "dpi": "1600", "x": "3.3%", "y": "3.3%",
        "target": "48%", "scope": "48%",
        "wall": "Mouse 5", "floor": "Mouse 4",
        "stairs": "Q", "roof": "V",
        "edit": "F / Mouse Wheel Down"
    },

    "Swizzy": {
        "input": "KBM",
        "dpi": "1600", "x": "3.5%", "y": "3.5%",
        "target": "54.5%", "scope": "54.6%",
        "wall": "Q", "floor": "X",
        "stairs": "C", "roof": "V", "edit": "F"
    },

    "Th0masHD": {
        "input": "KBM",
        "dpi": "1600", "x": "5.0%", "y": "3.0%",
        "target": "37%", "scope": "37%",
        "wall": "Q", "floor": "F",
        "stairs": "V", "roof": "X", "edit": "G"
    },

    "Shark": {
        "input": "KBM",
        "dpi": "800", "x": "6.8%", "y": "6.8%",
        "target": "41%", "scope": "41.5%",
        "wall": "Mouse 4", "floor": "C",
        "stairs": "E", "roof": "Mouse 5",
        "edit": "G / Mouse Wheel Up"
    },

   

    # ================= CONTROLLER =================

    "Reet": {
        "input": "Controller",
        "look_h": "47%", "look_v": "57%",
        "ads_h": "16%", "ads_v": "16%",
        "build": "1.8x", "edit_mult": "1.8x",
        "curve": "Exponential",
        "left_deadzone": "6%", "right_deadzone": "6%",
        "edit_button": "View Button",
        "jump": "A",
        "switch": "B"
    },

    "Mero": {
        "input": "Controller",
        "look_h": "43%", "look_v": "43%",
        "ads_h": "7%", "ads_v": "8%",
        "build": "2.0x", "edit_mult": "1.9x",
        "curve": "Linear",
        "left_deadzone": "7%", "right_deadzone": "8%",
        "edit_button": "Touchpad",
        "jump": "Cross",
        "switch": "L3"
    },

    "t3eny": {
        "input": "Controller",
        "look_h": "38%", "look_v": "35%",
        "ads_h": "16%", "ads_v": "24%",
        "build": "2.6x", "edit_mult": "2.5x",
        "curve": "Linear",
        "left_deadzone": "15%", "right_deadzone": "7%",
        "edit_button": "L3",
        "jump": "Cross",
        "switch": "Triangle"
    },

    "Minori": {
        "input": "Controller",
        "look_h": "40%", "look_v": "40%",
        "ads_h": "2%", "ads_v": "2%",
        "build": "2.1x", "edit_mult": "2.1x",
        "curve": "Linear",
        "left_deadzone": "7%", "right_deadzone": "7%",
        "edit_button": "L3",
        "jump": "Cross",
        "switch": "Circle"
    },

    "Nxthan": {
        "input": "Controller",
        "look_h": "44%", "look_v": "44%",
        "ads_h": "9%", "ads_v": "9%",
        "build": "1.9x", "edit_mult": "1.8x",
        "curve": "Linear",
        "left_deadzone": "9%", "right_deadzone": "9%",
        "edit_button": "—",
        "jump": "—",
        "switch": "—"
    },
"Curve": {
    "input": "Controller",
    "look_h": "—", "look_v": "—",
    "ads_h": "—", "ads_v": "—",
    "build": "1.9x", "edit_mult": "2.0x",
    "curve": "Linear",
    "left_deadzone": "6%", "right_deadzone": "6%",
    "edit_button": "—",
    "jump": "—",
    "switch": "—"
},
}


HOME = """
<!DOCTYPE html>
<html>
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-G0TC7KF319"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-G0TC7KF319');
</script>
<meta charset="UTF-8">
<title>Fortnite Pro Settings</title>

<style>

*{
    box-sizing:border-box;
}

body{
    margin:0;
    background:
    radial-gradient(circle at top,#101a38 0%,#070b17 42%,#050710 100%);
    color:white;
    font-family:Arial,sans-serif;
    min-height:100vh;
}

header{
    text-align:center;
    padding:45px 20px 20px;
}

h1{
    font-size:48px;
    margin:0 0 8px;
}

.blue{
    color:#5368ff;
}

.subtitle{
    color:#9ca6bf;
    font-size:18px;
}

.tabs{
    display:flex;
    justify-content:center;
    gap:15px;
    margin:28px auto 20px;
}

.tab{
    width:250px;
    padding:17px;
    border-radius:13px;
    font-size:19px;
    color:white;
    background:#141a2c;
    border:1px solid #303a5d;
    cursor:pointer;
    transition:.2s;
}

.tab:hover{
    transform:translateY(-2px);
}

.tab.active-kbm{
    background:#304cff;
    box-shadow:0 0 25px #304cff55;
}

.tab.active-controller{
    background:#b3133b;
    box-shadow:0 0 25px #ff174d44;
}

#search{
    width:550px;
    max-width:90%;
    padding:16px 20px;
    border-radius:13px;
    border:1px solid #303a5d;
    background:#11182b;
    color:white;
    font-size:17px;
    outline:none;
}

.main{
    max-width:1450px;
    margin:auto;
    padding:10px 25px 60px;
}

.section-title{
    font-size:28px;
    margin:20px 0;
    padding-top:15px;
    border-top:1px solid #28314c;
}

.players{
    display:grid;
    grid-template-columns:repeat(auto-fill,minmax(190px,1fr));
    gap:17px;
}

.player{
    background:#101629;
    border:1px solid #283862;
    border-radius:14px;
    overflow:hidden;
    text-align:center;
    transition:.2s;
}

.player:hover{
    transform:translateY(-5px);
}

.player.controller{
    border-color:#672039;
}
.photo{
    width:100%;
    height:145px;
    object-fit:cover;
    object-position:center center;
    display:block;
}
    height:145px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:55px;
    font-weight:bold;
    background:
    radial-gradient(circle,#233669,#0b1020);
}

.controller .photo{
    background:
    radial-gradient(circle,#5a1830,#150b14);
}

.player h2{
    margin:13px 5px 4px;
    font-size:20px;
}

.type{
    color:#8993aa;
    font-size:13px;
    margin-bottom:12px;
}

.view{
    display:block;
    margin:10px;
    padding:11px;
    border-radius:9px;
    color:white;
    font-weight:bold;
    text-decoration:none;
    background:#304cff;
}

.controller .view{
    background:#d61f48;
}

.hidden{
    display:none;
}

</style>
</head>

<body>

<header>

<h1>🎯 Fortnite Pro <span class="blue">Settings</span></h1>
<div class="subtitle">Settings, Keybinds & Gear from Fortnite Pros</div>

<div class="tabs">
<button id="kbmButton" class="tab active-kbm"
onclick="showType('KBM')">
⌨️🖱️ KBM
</button>

<button id="controllerButton" class="tab"
onclick="showType('Controller')">
🎮 Controller
</button>
</div>

<input
id="search"
placeholder="🔎 Search player..."
onkeyup="filterPlayers()">

</header>

<div class="main">

<h2 id="sectionTitle" class="section-title">
⌨️🖱️ KBM Pros
</h2>

<div class="players">

{% for name,p in players.items() %}

<div
class="player {% if p.input == 'Controller' %}controller{% endif %}"
data-input="{{p.input}}"
data-name="{{name|lower}}">

{% if name == "Peterbot" %}
<img class="photo" src="/static/peterbot.jpeg">
{% elif name == "Pollo" %}
<img class="photo" src="/static/pollo.jpeg">
{% elif name == "Veno" %}
<img class="photo" src="/static/veno.jpeg">{% elif name == "Queasy" %}
<img class="photo" src="/static/queasy.jpeg">{% elif name == "Clix" %}
<img class="photo" src="/static/clix.jpeg">{% elif name == "Bugha" %}
<img class="photo" src="/static/bugha.jpeg">{% elif name == "Mongraal" %}
<img class="photo" src="/static/mongraal.jpeg">{% elif name == "MrSavage" %}
<img class="photo" src="/static/mrsavage.jpeg">{% elif name == "Acorn" %}
<img class="photo" src="/static/acorn.jpeg">{% elif name == "Cold" %}
<img class="photo" src="/static/cold.jpeg">{% elif name == "Khanada" %}
<img class="photo" src="/static/khanada.jpeg">{% elif name == "Kami" %}
<img class="photo" src="/static/kami.jpeg">{% elif name == "Setty" %}
<img class="photo" src="/static/setty.jpeg">{% elif name == "Malibuca" %}
<img class="photo" src="/static/malibuca.jpeg">{% elif name == "Merstach" %}
<img class="photo" src="/static/merstach.jpeg">{% elif name == "Swizzy" %}
<img class="photo" src="/static/swizzy.jpeg">{% elif name == "Th0masHD" %}
<img class="photo" src="/static/th0mashd.jpeg">{% elif name == "Shark" %}
<img class="photo" src="/static/shxrk.jpeg">{% elif name == "vico" %}
<img class="photo" src="/static/vico.jpeg">{% elif name == "Reet" %}
<img class="photo" src="/static/reet.jpeg">{% elif name == "Mero" %}
<img class="photo" src="/static/mero.jpeg">{% elif name == "t3eny" %}
<img class="photo" src="/static/t3eny.jpeg">{% elif name == "Minori" %}
<img class="photo" src="/static/minori.jpeg">{% elif name == "Nxthan" %}
<img class="photo" src="/static/nxthan.jpeg">{% elif name == "Curve" %}
<img class="photo" src="/static/curve.jpeg">
{% else %}
<div class="photo">{{name[0]}}</div>
{% endif %}

<h2>{{name}}</h2>
<div class="type">{{p.input}} Pro</div>

<a class="view" href="/player/{{name}}">
View Settings
</a>

</div>

{% endfor %}

</div>
</div>


<script>

let currentType = "KBM";

function showType(type){

    currentType = type;

    const kbm =
    document.getElementById("kbmButton");

    const controller =
    document.getElementById("controllerButton");

    const title =
    document.getElementById("sectionTitle");

    kbm.className = "tab";
    controller.className = "tab";

    if(type === "KBM"){
        kbm.classList.add("active-kbm");
        title.innerHTML = "⌨️🖱️ KBM Pros";
    }else{
        controller.classList.add("active-controller");
        title.innerHTML = "🎮 Controller Pros";
    }

    filterPlayers();
}


function filterPlayers(){

    const search =
    document.getElementById("search")
    .value.toLowerCase();

    document.querySelectorAll(".player")
    .forEach(card => {

        const correctType =
        card.dataset.input === currentType;

        const correctSearch =
        card.dataset.name.includes(search);

        if(correctType && correctSearch){
            card.classList.remove("hidden");
        }else{
            card.classList.add("hidden");
        }

    });
}

showType("KBM");

</script>

</body>
</html>
"""


PLAYER = """
<!DOCTYPE html>
<html>
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-G0TC7KF319"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-G0TC7KF319');
</script>
<meta charset="UTF-8">
<title>{{name}} Settings</title>

<style>

body{
    margin:0;
    background:#070b17;
    color:white;
    font-family:Arial,sans-serif;
}

.container{
    max-width:1000px;
    margin:auto;
    padding:45px 25px;
}

.back{
    display:inline-block;
    color:white;
    text-decoration:none;
    background:#304cff;
    padding:10px 16px;
    border-radius:10px;
    font-weight:bold;
}

.hero{
    text-align:center;
    margin:25px 0 35px;
    padding:25px;
    background:#101629;
    border:1px solid #293352;
    border-radius:18px;
}

.avatar{
    width:150px;
    height:150px;
    border-radius:50%;
    margin:auto;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:65px;
    font-weight:bold;
    background:radial-gradient(circle,#304cff,#11182b);
}

.controller-avatar{
    background:radial-gradient(circle,#d61f48,#1b0b13);
}   
.avatar-img{
    width:100%;
    height:100%;
    object-fit:cover;
    border-radius:50%;
}
h1{
    font-size:45px;
    margin:15px 0 5px;
}

.type{
    color:#929bb2;
}

.grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
    gap:18px;
}

.card{
    background:#12182a;
    border:1px solid #293352;
    border-radius:16px;
    padding:22px;
}

.card h2{
    margin-top:0;
}

.row{
    display:flex;
    justify-content:space-between;
    border-bottom:1px solid #28304a;
    padding:11px 0;
    gap:15px;
}

.value{
    font-weight:bold;
    text-align:right;
}

</style>

</head>

<body>

<div class="container">

<a class="back" href="/">
← Back to players
</a>

<div class="hero">

<div class="avatar {% if p.input == 'Controller' %}controller-avatar{% endif %}">
<img src="/static/{{name|lower}}.jpeg" class="avatar-img">
</div>

<h1>{{name}}</h1>
<div class="type">
{% if p.input == "Controller" %}
🎮 Controller Pro
{% else %}
⌨️🖱️ KBM Pro
{% endif %}
</div>

</div>


{% if p.input == "KBM" %}

<div class="grid">

<div class="card">
<h2>🖱️ Sensitivity</h2>

<div class="row"><span>DPI</span><span class="value">{{p.dpi}}</span></div>
<div class="row"><span>X Sensitivity</span><span class="value">{{p.x}}</span></div>
<div class="row"><span>Y Sensitivity</span><span class="value">{{p.y}}</span></div>
<div class="row"><span>Targeting</span><span class="value">{{p.target}}</span></div>
<div class="row"><span>Scope</span><span class="value">{{p.scope}}</span></div>

</div>


<div class="card">
<h2>⌨️ Keybinds</h2>

<div class="row"><span>Wall</span><span class="value">{{p.wall}}</span></div>
<div class="row"><span>Floor</span><span class="value">{{p.floor}}</span></div>
<div class="row"><span>Stairs</span><span class="value">{{p.stairs}}</span></div>
<div class="row"><span>Roof</span><span class="value">{{p.roof}}</span></div>
<div class="row"><span>Edit</span><span class="value">{{p.edit}}</span></div>

</div>

</div>


{% else %}

<div class="grid">

<div class="card">

<h2>🎮 Look Sensitivity</h2>

<div class="row"><span>Horizontal</span><span class="value">{{p.look_h}}</span></div>
<div class="row"><span>Vertical</span><span class="value">{{p.look_v}}</span></div>
<div class="row"><span>ADS Horizontal</span><span class="value">{{p.ads_h}}</span></div>
<div class="row"><span>ADS Vertical</span><span class="value">{{p.ads_v}}</span></div>

</div>


<div class="card">

<h2>⚡ Build & Edit</h2>

<div class="row"><span>Build Multiplier</span><span class="value">{{p.build}}</span></div>
<div class="row"><span>Edit Multiplier</span><span class="value">{{p.edit_mult}}</span></div>
<div class="row"><span>Input Curve</span><span class="value">{{p.curve}}</span></div>

</div>


<div class="card">

<h2>🕹️ Deadzone</h2>

<div class="row"><span>Left Stick</span><span class="value">{{p.left_deadzone}}</span></div>
<div class="row"><span>Right Stick</span><span class="value">{{p.right_deadzone}}</span></div>

</div>


<div class="card">

<h2>🎯 Binds</h2>

<div class="row"><span>Edit</span><span class="value">{{p.edit_button}}</span></div>
<div class="row"><span>Jump</span><span class="value">{{p.jump}}</span></div>
<div class="row"><span>Switch Mode</span><span class="value">{{p.switch}}</span></div>

</div>

</div>

{% endif %}

</div>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(
        HOME,
        players=players
    )


@app.route("/player/<name>")
def player(name):

    if name not in players:
        abort(404)

    return render_template_string(
        PLAYER,
        name=name,
        p=players[name]
    )


if __name__ == "__main__":
    app.run(debug=True)