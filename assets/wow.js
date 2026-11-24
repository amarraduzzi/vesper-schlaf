(()=>{
const R=document.documentElement;if(!R.classList.contains('wj'))return;
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const fine=matchMedia('(hover:hover) and (pointer:fine)').matches;
const pb=document.createElement('div');pb.className='prog';document.body.appendChild(pb);
/* titel woord voor woord */
$$('.hero h1,.ah h1').forEach(h=>{h.setAttribute('aria-label',h.textContent.trim());let n=0;const walk=nd=>[...nd.childNodes].forEach(c=>{if(c.nodeType===3){const f=document.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(w=>{if(!w)return;if(/^\s+$/.test(w)){f.appendChild(document.createTextNode(' '));return}const sp=document.createElement('span');sp.className='wd';sp.setAttribute('aria-hidden','true');sp.style.setProperty('--i',n++);sp.textContent=w;f.appendChild(sp)});c.replaceWith(f)}else if(c.nodeType===1)walk(c)});walk(h)});
/* aurora + muisgloed in hero */
const hero=$('.hero');
if(hero){const a=document.createElement('div');a.className='aur';a.innerHTML='<i></i><i></i><i></i>';hero.prepend(a);
 if(fine){const g=document.createElement('div');g.className='mg';hero.prepend(g);hero.addEventListener('pointermove',e=>{const r=hero.getBoundingClientRect();g.style.setProperty('--mx',e.clientX-r.left+'px');g.style.setProperty('--my',e.clientY-r.top+'px')})}}
/* onthullen bij scrollen */
const sel='.calc .card,.ck .card,.rt .grid,.mc,.art,.brw,details,section h2,section .sub,.body h2,.body p:not(.done),.chk,.pic,.rel,.fine';
const els=$$(sel).filter(e=>!e.closest('.hero,.ah'));
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){const t=e.target;t.classList.add('in');io.unobserve(t);setTimeout(()=>t.classList.add('done'),1500)}}),{threshold:.12,rootMargin:'0px 0px -6% 0px'});
els.forEach(e=>{const sib=[...e.parentElement.children].filter(x=>x.matches(sel));e.style.setProperty('--d',Math.min(sib.indexOf(e),5)*.09+'s');e.classList.add('wv');io.observe(e)});
/* tilt op kaarten */
if(fine)$$('.art,.card').forEach(el=>{el.addEventListener('pointermove',e=>{if(e.pointerType!=='mouse')return;const r=el.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;el.style.transform=`perspective(900px) rotateX(${-y*5}deg) rotateY(${x*6}deg) translateY(-3px)`;el.style.setProperty('--gx',(x+.5)*100+'%');el.style.setProperty('--gy',(y+.5)*100+'%')});el.addEventListener('pointerleave',()=>{el.style.transform=''})});
/* scroll: voortgang + parallax */
const bgs=$$('.ah[style],.pano[style]'),pics=$$('.pic');let tick=false;
const upd=()=>{tick=false;const h=document.documentElement.scrollHeight-innerHeight;pb.style.setProperty('--pg',h>0?Math.min(1,scrollY/h):0);
 bgs.forEach(b=>{const r=b.getBoundingClientRect();if(r.bottom>0&&r.top<innerHeight)b.style.setProperty('--py',((innerHeight/2-(r.top+r.height/2))*.12).toFixed(1)+'px')});
 pics.forEach(p=>{const r=p.getBoundingClientRect();if(r.bottom<0||r.top>innerHeight)return;const k=(innerHeight-r.top)/(innerHeight+r.height);const im=$('img',p);if(im)im.style.transform=`scale(1.14) translateY(${((k-.5)*-34).toFixed(1)}px)`})};
addEventListener('scroll',()=>{if(!tick){tick=true;requestAnimationFrame(upd)}},{passive:true});addEventListener('resize',upd);upd();
/* tijden in de Schlafrechner rollen */
const cres=$('#calc .cres');
if(cres){let tk=0;new MutationObserver(()=>{const my=++tk;$$('.cc b',cres).forEach(b=>{const fin=b.textContent;let f=0;const iv=setInterval(()=>{if(my!==tk){clearInterval(iv);return}f++;if(f>12){b.textContent=fin;clearInterval(iv);return}b.textContent=String(Math.floor(Math.random()*24)).padStart(2,'0')+':'+String(Math.floor(Math.random()*6)).padStart(2,'0')+'0'.slice(0,0)+String(Math.floor(Math.random()*10))},32)})}).observe(cres,{childList:true})}
/* sterretjes bij tikken */
const burst=(x,y)=>{for(let i=0;i<9;i++){const p=document.createElement('span');p.className='pt';const a=Math.random()*6.283,d=30+Math.random()*34;p.style.left=x+'px';p.style.top=y+'px';p.style.setProperty('--dx',Math.cos(a)*d+'px');p.style.setProperty('--dy',Math.sin(a)*d+'px');document.body.appendChild(p);setTimeout(()=>p.remove(),850)}};
document.addEventListener('click',e=>{const t=e.target;const tile=t.closest&&t.closest('.tile');if(tile&&tile.getAttribute('aria-pressed')==='true')burst(e.clientX,e.clientY);else if(t.matches&&t.matches('.chk input')&&t.checked){const r=t.getBoundingClientRect();burst(r.left+r.width/2,r.top+r.height/2)}});
})();
