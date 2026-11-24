(()=>{
const R=document.documentElement;if(!R.classList.contains('wj'))return;
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const fine=matchMedia('(hover:hover) and (pointer:fine)').matches;
const lang=(R.lang||'de').slice(0,2);
let mox=0,moy=0;
/* lichtdeeltjes + muisspoor */
const cv=document.createElement('canvas');cv.className='fx';document.body.appendChild(cv);
const c=cv.getContext('2d');let W,H;const dpr=Math.min(devicePixelRatio||1,1.5);
const spr=document.createElement('canvas');spr.width=spr.height=64;
{const g=spr.getContext('2d'),gr=g.createRadialGradient(32,32,0,32,32,32);gr.addColorStop(0,'rgba(255,236,190,1)');gr.addColorStop(.25,'rgba(244,199,123,.55)');gr.addColorStop(1,'rgba(244,199,123,0)');g.fillStyle=gr;g.fillRect(0,0,64,64)}
const size=()=>{W=innerWidth;H=innerHeight;cv.width=W*dpr;cv.height=H*dpr;cv.style.width=W+'px';cv.style.height=H+'px';c.setTransform(dpr,0,0,dpr,0,0)};size();addEventListener('resize',size);
const M=Array.from({length:fine?56:26},()=>({x:Math.random()*innerWidth,y:Math.random()*innerHeight,z:Math.random()*.9+.1,vx:(Math.random()-.5)*.25,vy:-Math.random()*.2-.05,p:Math.random()*6.28,s:Math.random()*.02+.006}));
let mx=-999,my=-999,ly=scrollY;const sp=[];
const mqs=[];
const place=()=>{$$('.mt svg').forEach(sv=>{const k=+sv.dataset.k;sv.style.transform=`translate(${(-mox*(k+1)*7).toFixed(1)}px,${(Math.min(scrollY,900)*[.22,.12,.04][k]).toFixed(1)}px)`});const a=$('.aur');if(a)a.style.transform=`translate(${(mox*-26).toFixed(1)}px,${(moy*-18).toFixed(1)}px)`};
addEventListener('pointermove',e=>{if(e.pointerType!=='mouse')return;mx=e.clientX;my=e.clientY;mox=e.clientX/innerWidth*2-1;moy=e.clientY/innerHeight*2-1;place();if(sp.length<70)sp.push({x:mx,y:my,vx:(Math.random()-.5)*.8,vy:(Math.random()-.5)*.8+.3,l:1})});
const loop=()=>{if(document.hidden){requestAnimationFrame(loop);return}
 let dy=scrollY-ly;ly=scrollY;dy=Math.max(-60,Math.min(60,dy));c.clearRect(0,0,W,H);
 for(const m of M){m.p+=m.s;m.x+=m.vx+Math.sin(m.p)*.15*m.z;m.y+=m.vy-dy*m.z*.35;
  const ddx=m.x-mx,ddy=m.y-my,d2=ddx*ddx+ddy*ddy;if(d2<16900){const d=Math.sqrt(d2)||1,f=(130-d)/130;m.x+=ddx/d*f*3.2;m.y+=ddy/d*f*3.2}
  if(m.y<-20)m.y=H+20;if(m.y>H+20)m.y=-20;if(m.x<-20)m.x=W+20;if(m.x>W+20)m.x=-20;
  const s=6+m.z*18;c.globalAlpha=(.25+.55*Math.abs(Math.sin(m.p*1.7)))*m.z;c.drawImage(spr,m.x-s/2,m.y-s/2,s,s)}
 for(let i=sp.length-1;i>=0;i--){const s=sp[i];s.x+=s.vx;s.y+=s.vy;s.l-=.03;if(s.l<=0){sp.splice(i,1);continue}c.globalAlpha=s.l*.8;const z=4+s.l*16;c.drawImage(spr,s.x-z/2,s.y-z/2,z,z)}
 const now=performance.now();mqs.forEach(q=>{const p=q.t.scrollWidth/4;if(!p)return;const o=((((scrollY*.5+now*.03)*q.dir)%p)+p)%p;q.t.style.transform=`translateX(${-o}px)`});
 requestAnimationFrame(loop)};loop();
/* bergen in de hero */
const hero=$('.hero');
if(hero){const ns='http://www.w3.org/2000/svg',box=document.createElement('div');box.className='mt';
 ['#161d52','#0f1540','#070a1a'].forEach((col,k)=>{const sv=document.createElementNS(ns,'svg');sv.setAttribute('viewBox','0 0 1200 300');sv.setAttribute('preserveAspectRatio','none');sv.setAttribute('aria-hidden','true');
  const sd=k*7.3+2;let d='M0 300 L0 '+(150+k*45);
  for(let x=0;x<=1200;x+=20){const y=150+k*45-Math.sin(x/(170-k*30)+sd)*(45-k*8)-Math.sin(x/(60-k*8)+sd*2)*(14-k*3)-Math.sin(x/330+sd)*30;d+=' L'+x+' '+y.toFixed(1)}
  d+=' L1200 300 Z';const p=document.createElementNS(ns,'path');p.setAttribute('d',d);p.setAttribute('fill',col);p.setAttribute('opacity',[.8,.92,1][k]);sv.appendChild(p);sv.dataset.k=k;box.appendChild(sv)});
 hero.appendChild(box);place()}
/* tekstbanden */
const WD={de:['Ruhe','Abend','Rhythmus','Dunkelheit','Atem','Traum','Mond'],fr:['Calme','Soir','Rythme','Obscurité','Souffle','Rêve','Lune'],it:['Calma','Sera','Ritmo','Buio','Respiro','Sogno','Luna']}[lang]||['Ruhe','Abend','Mond'];
const mk=(before,dir)=>{if(!before)return;const m=document.createElement('div');m.className='mq';m.setAttribute('aria-hidden','true');const t=document.createElement('div');t.className='mqt';t.textContent=(WD.join(' ✦ ')+' ✦ ').repeat(4);m.appendChild(t);before.parentNode.insertBefore(m,before);mqs.push({t,dir})};
mk($('#check'),1);mk($('#artikel'),-1);
/* maan-knop: vult zich terwijl je leest */
const mb=document.createElement('button');mb.type='button';mb.className='mtop';mb.setAttribute('aria-label',{de:'Nach oben',fr:'Haut de page',it:'Torna su'}[lang]||'Top');
mb.innerHTML='<svg viewBox="0 0 48 48" aria-hidden="true"><defs><clipPath id="mcp"><circle cx="24" cy="24" r="17"/></clipPath></defs><circle cx="24" cy="24" r="17" fill="#f3ead7"/><circle class="dk" cx="24" cy="24" r="17" fill="#0d1233" clip-path="url(#mcp)"/></svg>';
mb.onclick=()=>scrollTo({top:0,behavior:'smooth'});document.body.appendChild(mb);const dk=$('.dk',mb);
/* scroll: maanfase, pano-maan, bergen */
const pano=$('.pano');let tk=false;
const upd=()=>{tk=false;const h=document.documentElement.scrollHeight-innerHeight,p=h>0?Math.min(1,scrollY/h):0;dk.setAttribute('cx',(24+p*40).toFixed(1));mb.classList.toggle('on',scrollY>500);
 if(pano){const r=pano.getBoundingClientRect();pano.style.setProperty('--rs',Math.max(0,Math.min(1,(innerHeight-r.top)/(innerHeight+r.height))).toFixed(3))}place()};
addEventListener('scroll',()=>{if(!tk){tk=true;requestAnimationFrame(upd)}},{passive:true});upd();
/* magnetische knoppen */
if(fine)$$('.btn,.cta2').forEach(b=>{b.addEventListener('pointermove',e=>{const r=b.getBoundingClientRect();b.style.transform=`translate(${((e.clientX-r.left-r.width/2)*.18).toFixed(1)}px,${((e.clientY-r.top-r.height/2)*.28).toFixed(1)}px)`});b.addEventListener('pointerleave',()=>{b.style.transform=''})});
})();
