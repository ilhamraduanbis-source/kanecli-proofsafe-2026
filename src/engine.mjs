// Deterministic local preflight. No remote calls. Not a full RFC 4180 CSV parser.
export const SAMPLE='invoice_id,amount,currency\nINV-001,150,MYR\nINV-002,75,MYR';
export const INVALID='invoice_id,amount,currency\nINV-001,-1,MYR\nINV-001,not-a-number,MYR';
const required=['invoice_id','amount','currency'];
export function preflight(input){
 if(typeof input!=='string'||!input.trim()) return {ok:false,rows:0,issues:['Input is empty'],schema:'proofsafe-local-v1'};
 if(input.length>25000) return {ok:false,rows:0,issues:['Input exceeds local 25KB limit'],schema:'proofsafe-local-v1'};
 const lines=input.replaceAll('\r\n','\n').trim().split('\n');
 const headers=lines.shift().split(',').map(x=>x.trim());const issues=[];
 const dup=headers.filter((x,i)=>headers.indexOf(x)!==i);
 if(dup.length)issues.push('Duplicate header: '+[...new Set(dup)].join(', '));
 for(const col of required) if(!headers.includes(col)) issues.push('Missing required column: '+col);
 const idx=Object.fromEntries(required.map(x=>[x,headers.indexOf(x)]));const seen=new Set();let rows=0;
 for(let i=0;i<lines.length;i++){
  if(!lines[i].trim())continue;const cells=lines[i].split(',').map(x=>x.trim());rows++;
  if(cells.length!==headers.length){issues.push('Row '+(i+2)+' column count mismatch');continue;}
  if(required.every(x=>idx[x]!==-1)){
   const id=cells[idx.invoice_id],amount=Number(cells[idx.amount]),currency=cells[idx.currency];
   if(!id)issues.push('Row '+(i+2)+' missing invoice ID');
   else if(seen.has(id))issues.push('Row '+(i+2)+' duplicate invoice ID: '+id);
   else seen.add(id);
   if(!Number.isFinite(amount)||amount<0||cells[idx.amount]==='')issues.push('Row '+(i+2)+' invalid amount');
   if(!/^[A-Z]{3}$/.test(currency))issues.push('Row '+(i+2)+' invalid currency code');
  }
 }
 if(rows===0)issues.push('No data rows');
 return{ok:issues.length===0,rows,issues,schema:'proofsafe-local-v1'};
}