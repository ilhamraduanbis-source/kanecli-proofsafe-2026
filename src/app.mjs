import {preflight,SAMPLE,INVALID} from './engine.mjs';
const $=id=>document.getElementById(id);let last=null;
function reset(){
 last=null;$('download').disabled=true;$('rows').textContent='0';$('issues').textContent='0';
 $('findings').replaceChildren();const li=document.createElement('li');li.textContent='Run the preflight to see evidence.';$('findings').append(li);
}
$('check').addEventListener('click',()=>{
 const r=preflight($('csv').value);last=r;
 $('rows').textContent=String(r.rows);$('issues').textContent=String(r.issues.length);
 $('status').textContent=r.ok?'PASS · Local CSV validation passed; no submission or payment verified.':'FAIL · Local CSV validation found '+r.issues.length+' issue(s).';
 $('findings').replaceChildren();
 for(const finding of r.issues.length?r.issues:['No local validation issues detected.']){
  const li=document.createElement('li');li.textContent=finding;$('findings').append(li);
 }
 $('download').disabled=false;
});
$('sample').addEventListener('click',()=>{$('csv').value=SAMPLE;reset();$('status').textContent='Sample reset. No validation has run yet.';});
$('bad').addEventListener('click',()=>{$('csv').value=INVALID;reset();$('status').textContent='Failing synthetic case loaded. Select Validate locally.';});
$('download').addEventListener('click',()=>{
 if(!last)return;
 const payload={...last,source:'LOCAL_BROWSER',verifiedByKane:false,transactionSettled:false,scope:'Local CSV QA only; zero claimed transactions',timestamp:new Date().toISOString()};
 const url=URL.createObjectURL(new Blob([JSON.stringify(payload,null,2)],{type:'application/json'}));const a=document.createElement('a');
 a.href=url;a.download='proofsafe-local-validation.json';a.click();
 setTimeout(()=>URL.revokeObjectURL(url),1000);
});
