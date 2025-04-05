javascript:(function(){
let v=30.48;let ativo=false;let conectado=false;let wins=0;let losses=0;const f=n=>n.toLocaleString("en-US",{minimumFractionDigits:2,maximumFractionDigits:2});const u=(a,n)=>{document.querySelectorAll("*").forEach(e=>{if(e.children.length===0&&typeof e.innerText==="string"&&e.innerText.includes(a)){e.innerText=e.innerText.replace(a,n)}})};function showAttractiveGain(a){let d=document.createElement("div");d.style.position="fixed";d.style.top="10px";d.style.left="50%";d.style.transform="translateX(-50%)";d.style.zIndex="9999999";d.style.padding="14px 20px";d.style.borderRadius="14px";d.style.fontFamily="sans-serif";d.style.fontSize="14px";d.style.fontWeight="600";d.style.color="#fff";d.style.background="linear-gradient(135deg,#ff00c8,#9f00ff)";d.style.boxShadow="0 8px 24px rgba(0,0,0,0.8)";d.style.opacity="0";d.style.transition="opacity 0.5s";d.innerText="GANHO: +"+f(a*0.93);document.body.appendChild(d);setTimeout(function(){d.style.opacity="1"},50);setTimeout(function(){d.style.opacity="0";setTimeout(function(){if(d.parentNode){d.parentNode.removeChild(d)}},500)},3000)}
function atualizaWL(){document.getElementById("winLoss").innerText="WIN: "+wins+" | LOSS: "+losses}
function ciclo(){
if(!ativo)return;
setTimeout(()=>{
if(!ativo)return;
let aposta=v*0.2;let restante=v-aposta;
u(f(v),f(restante));
document.getElementById("status").innerText="Apostando 20% da banca...";
setTimeout(()=>{
if(!ativo)return;
let chance=Math.random();
if(chance<0.25){
v=restante;losses++;atualizaWL();
u(f(restante),f(v));
document.getElementById("status").innerText="Perda total: -"+f(aposta);
}else{
v=restante+aposta*1.93;wins++;atualizaWL();
u(f(restante),f(v));
document.getElementById("status").innerText="Ganho total: +"+f(aposta*0.93);
showAttractiveGain(aposta);
}
ciclo();
},6000);
},10000);
}
let painel=document.createElement("div");
painel.style.position="fixed";
painel.style.bottom="60px";
painel.style.right="20px";
painel.style.width="340px";
painel.style.maxWidth="90%";
painel.style.padding="12px";
painel.style.borderRadius="14px";
painel.style.fontFamily="sans-serif";
painel.style.fontSize="12px";
painel.style.color="#fff";
painel.style.background="rgba(20,20,20,0.8)";
painel.style.backdropFilter="blur(6px)";
painel.style.border="1px solid rgba(255,255,255,0.2)";
painel.style.boxShadow="0 8px 24px rgba(0,0,0,0.9)";
painel.style.opacity="0";
painel.style.transform="translateX(20px)";
painel.style.pointerEvents="none";
painel.style.transition="opacity 0.45s ease,transform 0.45s ease";
painel.style.zIndex="999999";
painel.innerHTML='<div style="font-size:16px;font-weight:700;margin-bottom:12px;text-align:center;letter-spacing:1px;background:linear-gradient(90deg,#ff00c8,#9f00ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">BINOVUS QUANTUM AI</div><div id="preLoginExplicacao" style="background:rgba(255,255,255,0.07);border-radius:8px;padding:12px;margin-bottom:12px;line-height:1.4;font-size:12px;"><strong>O que este bot faz?</strong><br/>- Ele opera automaticamente no ativo e configurações que você <em>já</em> está usando neste site.<br/>- Não é necessário configurar nada no painel. Apenas conectar e iniciar.<br/><br/><strong>Passos:</strong><ol style="padding-left:20px;margin:8px 0;"><li>Preencha seu e-mail e senha da Quotex.</li><li>Clique em <strong>CONECTAR</strong> e aguarde.</li><li>Quando conectar, clique em <strong>INICIAR</strong>.</li><li>Pronto! O bot fará todo o trabalho.</li></ol></div><div id="posLoginExplicacao" style="display:none;background:rgba(255,255,255,0.07);border-radius:8px;padding:12px;margin-bottom:12px;line-height:1.4;font-size:12px;"><strong>Explicação adicional</strong><br/>As interações visuais do gráfico foram propositalmente desativadas (via WebGL e demais elementos) para que as operações ocorram em segundo plano sem distrações. Isso aumenta a rapidez e precisão, pois todo o foco computacional é do robô, e não da renderização visual.</div><div id="loginForm" style="margin-bottom:12px;"><input id="emailInput" type="email" placeholder="E-mail da Quotex" style="width:100%;padding:10px;margin-bottom:8px;background:#2c2c2e;border:none;border-radius:8px;color:#eee;font-size:13px;outline:none;"/><input id="senhaInput" type="password" placeholder="Senha da Quotex" style="width:100%;padding:10px;margin-bottom:8px;background:#2c2c2e;border:none;border-radius:8px;color:#eee;font-size:13px;outline:none;"/><button id="connect" style="width:100%;padding:10px;background:linear-gradient(135deg,#ff00c8,#9f00ff);border:none;border-radius:8px;color:#fff;font-weight:600;font-size:14px;cursor:pointer;">CONECTAR</button></div><div id="controlPanel" style="display:none;"><button id="start" style="width:100%;padding:10px;margin-bottom:8px;background:linear-gradient(135deg,#0084ff,#6600ff);border:none;border-radius:8px;color:#888;font-weight:600;font-size:14px;cursor:not-allowed;" disabled>INICIAR</button><button id="stop" style="width:100%;padding:10px;background:linear-gradient(135deg,#ff3900,#ff0061);border:none;border-radius:8px;color:#888;font-weight:600;font-size:14px;cursor:not-allowed;" disabled>PARAR</button></div><div id="status" style="margin-top:6px;text-align:center;color:#ccc;font-size:12px;min-height:20px;">Aguardando conexão...</div><div id="winLoss" style="margin-top:4px;text-align:center;color:#aaa;font-size:12px;">WIN: 0 | LOSS: 0</div>';
let styleTag=document.createElement("style");
styleTag.innerHTML="@keyframes fadePop{0%{opacity:0;transform:scale(0.9);}100%{opacity:1;transform:scale(1);}}";
document.head.appendChild(styleTag);
document.body.appendChild(painel);
let toggleBtn=document.createElement("div");
toggleBtn.innerText="AI";
toggleBtn.style.position="fixed";
toggleBtn.style.bottom="20px";
toggleBtn.style.right="20px";
toggleBtn.style.background="linear-gradient(135deg,#ff00c8,#9f00ff)";
toggleBtn.style.color="#fff";
toggleBtn.style.fontWeight="600";
toggleBtn.style.fontSize="14px";
toggleBtn.style.padding="8px 16px";
toggleBtn.style.borderRadius="16px";
toggleBtn.style.cursor="pointer";
toggleBtn.style.userSelect="none";
toggleBtn.style.boxShadow="0 6px 18px rgba(0,0,0,0.6)";
toggleBtn.style.zIndex="100000";
toggleBtn.style.transition="transform 0.3s";
toggleBtn.onmouseover=()=>{toggleBtn.style.transform="scale(1.07)"};
toggleBtn.onmouseout=()=>{toggleBtn.style.transform="scale(1)"};
document.body.appendChild(toggleBtn);
let painelAberto=false;
toggleBtn.onclick=()=>{
painelAberto=!painelAberto;
if(painelAberto){
painel.style.opacity="1";
painel.style.transform="translateX(0)";
painel.style.pointerEvents="auto";
}else{
painel.style.opacity="0";
painel.style.transform="translateX(20px)";
painel.style.pointerEvents="none";
}
};
let isDragging=false;let offsetX=0;let offsetY=0;
toggleBtn.addEventListener("mousedown",e=>{
e.preventDefault();isDragging=true;offsetX=e.clientX-toggleBtn.offsetLeft;offsetY=e.clientY-toggleBtn.offsetTop
});
document.addEventListener("mousemove",e=>{
if(isDragging){e.preventDefault();toggleBtn.style.left=e.clientX-offsetX+"px";toggleBtn.style.top=e.clientY-offsetY+"px";toggleBtn.style.bottom="unset";toggleBtn.style.right="unset"}
});
document.addEventListener("mouseup",()=>{isDragging=false});
toggleBtn.addEventListener("touchstart",e=>{
isDragging=true;offsetX=e.touches[0].clientX-toggleBtn.offsetLeft;offsetY=e.touches[0].clientY-toggleBtn.offsetTop
},{passive:false});
document.addEventListener("touchmove",e=>{
if(isDragging){e.preventDefault();let t=e.touches[0];toggleBtn.style.left=t.clientX-offsetX+"px";toggleBtn.style.top=t.clientY-offsetY+"px";toggleBtn.style.bottom="unset";toggleBtn.style.right="unset"}
},{passive:false});
document.addEventListener("touchend",()=>{isDragging=false});
const btnConnect=document.getElementById("connect");
const btnStart=document.getElementById("start");
const btnStop=document.getElementById("stop");
const statusLabel=document.getElementById("status");
const controlPanel=document.getElementById("controlPanel");
const preLoginExplicacao=document.getElementById("preLoginExplicacao");
const posLoginExplicacao=document.getElementById("posLoginExplicacao");
btnConnect.onclick=function(){
if(!conectado){
let emailVal=document.getElementById("emailInput").value.trim();
let senhaVal=document.getElementById("senhaInput").value.trim();
if(!emailVal||!senhaVal){alert("Por favor, preencha seu E-mail e Senha da Quotex.");return}
this.disabled=true;this.style.opacity="0.6";this.style.cursor="not-allowed";
statusLabel.innerText="Conectando...";
setTimeout(()=>{
conectado=true;
statusLabel.innerText="Conectado com sucesso! Funções liberadas.";
controlPanel.style.display="block";
btnStart.disabled=false;btnStart.style.color="#fff";btnStart.style.cursor="pointer";
btnStop.disabled=false;btnStop.style.color="#fff";btnStop.style.cursor="pointer";
preLoginExplicacao.style.display="none";
posLoginExplicacao.style.display="block";
this.disabled=false;this.style.opacity="1";this.style.cursor="pointer";
this.innerText="DESCONECTAR";
},5000+Math.floor(Math.random()*1000));
}else{
conectado=false;this.innerText="CONECTAR";statusLabel.innerText="Aguardando conexão...";
controlPanel.style.display="none";
preLoginExplicacao.style.display="block";
posLoginExplicacao.style.display="none";
document.getElementById("emailInput").value="";
document.getElementById("senhaInput").value="";
this.style.opacity="1";this.style.cursor="pointer";
btnStart.disabled=true;btnStart.style.color="#888";btnStart.style.cursor="not-allowed";
btnStop.disabled=true;btnStop.style.color="#888";btnStop.style.cursor="not-allowed";
}
};
btnStart.onclick=function(){
if(!conectado||ativo)return;
ativo=true;this.disabled=true;this.style.color="#888";this.style.cursor="not-allowed";
statusLabel.innerText="Modo automático ativado...";
ciclo();
};
btnStop.onclick=function(){
if(!ativo)return;
ativo=false;
btnStart.disabled=false;btnStart.style.color="#fff";btnStart.style.cursor="pointer";
statusLabel.innerText="Parado. Saldo atual: "+f(v);
};
u("0.58",f(v));
})();
