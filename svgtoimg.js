javascript:(()=>{const i=document.createElement('input');i.type='file';i.accept='image/*';i.style.display='none';document.body.appendChild(i);[...document.querySelectorAll('img,svg')].forEach(el=>{el.style.cursor='pointer';el.addEventListener('click',e=>{e.stopImmediatePropagation();e.preventDefault();e.stopPropagation();i.onchange=ev=>{const f=ev.target.files[0];if(!f)return;const r=new FileReader();r.onload=ev2=>{if(el.tagName.toLowerCase()==='img'){el.src=ev2.target.result}else{const img=document.createElement('img');img.src=ev2.target.result;const rect=el.getBoundingClientRect();img.style.width=rect.width+'px';img.style.height=rect.height+'px';img.style.borderRadius='50%';img.style.objectFit='cover';el.replaceWith(img);}};r.readAsDataURL(f);i.value=''};i.click();},true);});alert('Clique em qualquer imagem ou SVG. Agora respeita formatos circulares!');})();
