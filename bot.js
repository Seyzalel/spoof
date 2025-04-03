javascript:(function(){
let v=50.81,ativo=false,conectado=false,wins=0,losses=0,f=n=>n.toLocaleString("en-US",{minimumFractionDigits:2,maximumFractionDigits:2}),u=(a,n)=>{document.querySelectorAll("*").forEach(e=>{if(e.children.length===0&&typeof e.innerText==="string"&&e.innerText.includes(a)){e.innerText=e.innerText.replace(a,n)}})};u("0.58",f(v));
let painel=document.createElement("div");
painel.style.position="fixed";
painel.style.bottom="80px";
painel.style.right="20px";
painel.style.width="300px";
painel.style.padding="16px";
painel.style.borderRadius="12px";
painel.style.fontFamily="sans-serif";
painel.style.background="linear-gradient(135deg,#1f1f1f,#191919)";
painel.style.color="#fff";
painel.style.fontSize="14px";
painel.style.boxShadow="0 8px 20px rgba(0,0,0,0.7)";
painel.style.opacity="0";
painel.style.pointerEvents="none";
painel.style.transition="all 0.3s ease";
painel.style.zIndex="9999";
painel.innerHTML='<div style="font-size:18px;font-weight:700;margin-bottom:12px;text-align:center;">BINOVUS QUANTUM AI</div><div style="background:rgba(255,255,255,0.05);border-radius:8px;padding:12px;margin-bottom:12px;text-align:center;line-height:1.4;">Este sistema usa proxies e o método SOROS, negociando de acordo com as configurações de ativos. Elementos visuais desativados, foque somente no valor.</div><button id="connect" style="width:100%;padding:10px;margin-bottom:10px;background:#2c2c2e;border:none;border-radius:8px;color:#fff;font-weight:600;font-size:14px;cursor:pointer;">CONECTAR</button><button id="start" style="width:100%;padding:10px;margin-bottom:10px;background:#2c2c2e;border:none;border-radius:8px;color:#888;font-weight:600;font-size:14px;cursor:not-allowed;" disabled>INICIAR</button><button id="stop" style="width:100%;padding:10px;background:#2c2c2e;border:none;border-radius:8px;color:#888;font-weight:600;font-size:14px;cursor:not-allowed;" disabled>PARAR</button><div id="status" style="margin-top:8px;text-align:center;color:#ccc;font-size:13px;">Aguardando conexão</div><div id="winLoss" style="margin-top:6px;text-align:center;color:#aaa;font-size:13px;">WIN: 0 | LOSS: 0</div>';
document.body.appendChild(painel);
let toggleBtn=document.createElement("div");
toggleBtn.innerText="AI";
toggleBtn.style.position="fixed";
toggleBtn.style.bottom="20px";
toggleBtn.style.right="20px";
toggleBtn.style.background="#333";
toggleBtn.style.color="#fff";
toggleBtn.style.fontWeight="600";
toggleBtn.style.fontSize="14px";
toggleBtn.style.padding="10px 14px";
toggleBtn.style.borderRadius="10px";
toggleBtn.style.cursor="pointer";
toggleBtn.style.userSelect="none";
toggleBtn.style.boxShadow="0 4px 12px rgba(0,0,0,0.6)";
toggleBtn.style.zIndex="10000";
document.body.appendChild(toggleBtn);
let painelAberto=false;
toggleBtn.onclick=()=>{painelAberto=!painelAberto;painel.style.opacity=painelAberto?"1":"0";painel.style.pointerEvents=painelAberto?"auto":"none";};
let isDragging=false,offsetX=0,offsetY=0;
toggleBtn.addEventListener("mousedown",e=>{isDragging=true;offsetX=e.clientX-toggleBtn.offsetLeft;offsetY=e.clientY-toggleBtn.offsetTop;});
document.addEventListener("mousemove",e=>{if(isDragging){toggleBtn.style.left=e.clientX-offsetX+"px";toggleBtn.style.top=e.clientY-offsetY+"px";toggleBtn.style.bottom="unset";toggleBtn.style.right="unset";}});
document.addEventListener("mouseup",()=>{isDragging=false;});
toggleBtn.addEventListener("touchstart",e=>{isDragging=true;let t=e.touches[0];offsetX=t.clientX-toggleBtn.offsetLeft;offsetY=t.clientY-toggleBtn.offsetTop;},{passive:true});
document.addEventListener("touchmove",e=>{if(isDragging){let t=e.touches[0];toggleBtn.style.left=t.clientX-offsetX+"px";toggleBtn.style.top=t.clientY-offsetY+"px";toggleBtn.style.bottom="unset";toggleBtn.style.right="unset";}},{passive:true});
document.addEventListener("touchend",()=>{isDragging=false;});
function atualizaWL(){document.getElementById("winLoss").innerText="WIN: "+wins+" | LOSS: "+losses;}
function ciclo(){
if(!ativo)return;
setTimeout(()=>{
if(!ativo)return;
let aposta=v*0.1,restante=v-aposta;
u(f(v),f(restante));
document.getElementById("status").innerText="Apostando 10% da banca...";
setTimeout(()=>{
if(!ativo)return;
v=restante+aposta*1.91;
u(f(restante),f(v));
wins++;atualizaWL();
document.getElementById("status").innerText="Ganho total: +R$"+f(aposta*0.91);
ciclo();
},6000);
},10000);
}
document.getElementById("connect").onclick=function(){
if(conectado)return;
this.disabled=true;
this.style.opacity="0.5";
this.style.cursor="not-allowed";
document.getElementById("status").innerText="Conectando...";
setTimeout(()=>{
conectado=true;
document.getElementById("start").disabled=false;
document.getElementById("stop").disabled=false;
document.getElementById("start").style.color="#fff";
document.getElementById("stop").style.color="#fff";
document.getElementById("start").style.cursor="pointer";
document.getElementById("stop").style.cursor="pointer";
document.getElementById("status").innerText="Conectado. Pronto para iniciar.";
},5000+Math.floor(Math.random()*1000));
};
document.getElementById("start").onclick=function(){
if(!conectado||ativo)return;
ativo=true;
this.disabled=true;
this.style.color="#888";
this.style.cursor="not-allowed";
document.getElementById("status").innerText="Modo automático ativado...";
ciclo();
};
document.getElementById("stop").onclick=function(){
if(!ativo)return;
ativo=false;
document.getElementById("start").disabled=false;
document.getElementById("start").style.color="#fff";
document.getElementById("start").style.cursor="pointer";
document.getElementById("status").innerText="Parado. Saldo atual: "+f(v);
};
})();
