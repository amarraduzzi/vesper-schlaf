(()=>{
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const rm=matchMedia('(prefers-reduced-motion:reduce)').matches;
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
$$('.rv').forEach(e=>io.observe(e));
const nv=$('header.nv');const onS=()=>{nv.classList.toggle('sc',scrollY>20);const m=$('.hm');if(m&&!rm)m.style.transform='translateY('+Math.min(scrollY*.25,160)+'px)'};
addEventListener('scroll',onS,{passive:true});onS();
/* stars */
const cv=$('#stars');
if(cv){const c=cv.getContext('2d');let W,H,S=[],sh=null;
 const size=()=>{const r=cv.parentElement.getBoundingClientRect();W=cv.width=r.width;H=cv.height=r.height;S=Array.from({length:Math.round(W*H/5200)},()=>({x:Math.random()*W,y:Math.random()*H,r:Math.random()*1.3+.2,p:Math.random()*6.28,s:Math.random()*.02+.005}))};
 size();addEventListener('resize',size);
 const draw=()=>{c.clearRect(0,0,W,H);for(const s of S){s.p+=s.s;c.globalAlpha=.35+.65*Math.abs(Math.sin(s.p));c.fillStyle='#fff';c.beginPath();c.arc(s.x,s.y,s.r,0,6.283);c.fill()}
  if(!sh&&Math.random()<.011)sh={x:Math.random()*W*.8+W*.1,y:Math.random()*H*.35,l:0};
  if(sh){sh.l+=9;sh.x+=7;sh.y+=3.5;c.globalAlpha=Math.max(0,1-sh.l/180);c.strokeStyle='#f3ead7';c.lineWidth=1.5;c.beginPath();c.moveTo(sh.x,sh.y);c.lineTo(sh.x-sh.l*.45,sh.y-sh.l*.22);c.stroke();if(sh.l>180)sh=null}
  if(!rm)requestAnimationFrame(draw)};draw()}
/* calc */
const calc=$('#calc');
if(calc){let mode=0;const inp=$('input',calc),out=$('.cres',calc);
 const f=m=>{m=((m%1440)+1440)%1440;return String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0')};
 const run=()=>{const p=inp.value.split(':').map(Number);if(p.length<2||isNaN(p[0]))return;const t=p[0]*60+p[1];const cs=mode?[4,5,6]:[6,5,4];
  out.innerHTML=cs.map(c=>`<div class="cc"><small>${mode?calc.dataset.l2:calc.dataset.l1}</small><b>${f(mode?t+15+c*90:t-c*90-15)}</b><span>${c} ${calc.dataset.cyc} · ${String(c*1.5).replace('.',',')} ${calc.dataset.hr}</span></div>`).join('')};
 $$('.tabs button',calc).forEach((b,i)=>b.onclick=()=>{mode=i;inp.value=i?'23:00':'07:00';$$('.tabs button',calc).forEach((x,j)=>x.setAttribute('aria-selected',j==i));run()});
 inp.oninput=run;run()}
/* check */
const ck=$('#check .ckb');
if(ck){let i=0,sum=0;const qs=$$('.cq',ck),dots=$$('.cdots i',ck);dots[0].classList.add('on');
 $$('.co button',ck).forEach(b=>b.onclick=()=>{sum+=+b.dataset.v;qs[i].hidden=true;i++;
  if(i<3){qs[i].hidden=false;dots[i].classList.add('on')}else{$$('.cdots i',ck).forEach(d=>d.classList.add('on'));const k=sum<=1?'lark':sum<=4?'dove':'owl';$('.cr[data-k='+k+']',ck).hidden=false;$('.cf2',ck).hidden=false}});
 $('.cagain',ck).onclick=()=>{i=0;sum=0;qs.forEach((q,j)=>q.hidden=j>0);$$('.cr',ck).forEach(r=>r.hidden=true);$('.cf2',ck).hidden=true;dots.forEach((d,j)=>d.classList.toggle('on',j==0))}}
/* ritual */
const rt=$('#abend');
if(rt){const t=$$('.tile',rt),m=$('.moon',rt),msg=$('.rmsg',rt),cnt=$('.rcount',rt),ms=msg.dataset.m.split('|');
 t.forEach(b=>b.onclick=()=>{b.setAttribute('aria-pressed',b.getAttribute('aria-pressed')!='true');const n=t.filter(x=>x.getAttribute('aria-pressed')=='true').length;
  m.style.setProperty('--p',Math.max(.04,n/t.length));msg.textContent=ms[n==0?0:n<=2?1:n<=4?2:n<8?3:4];cnt.textContent=n+' / '+t.length+' '+cnt.dataset.u})}
/* breath */
const bw=$('.brw');
if(bw){const c=$('.brc',bw),sp=$('span',c),bt=$('.brb',bw),rs=$('.brs',bw);let on=false,n=0,t1,t2;
 const cyc=()=>{sp.textContent=bw.dataset.i;c.classList.add('in');t1=setTimeout(()=>{sp.textContent=bw.dataset.o;c.classList.remove('in');t2=setTimeout(()=>{n++;rs.textContent=n+' '+bw.dataset.u;cyc()},6000)},4000)};
 bt.onclick=()=>{on=!on;if(on){n=0;rs.textContent='0 '+bw.dataset.u;bt.textContent=bw.dataset.st;cyc()}else{clearTimeout(t1);clearTimeout(t2);c.classList.remove('in');bt.textContent=bw.dataset.go;sp.textContent='…'}}}
/* myth */
$$('.mc').forEach(b=>b.onclick=()=>b.setAttribute('aria-pressed',b.getAttribute('aria-pressed')!='true'));
/* article checklist */
const cl=$('.chk');
if(cl){const bx=$$('input',cl),d=$('.done');bx.forEach(x=>x.onchange=()=>{d.hidden=!bx.every(y=>y.checked)})}
})();
