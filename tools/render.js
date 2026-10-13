// Usage: node render.js <dir-with-html> <filename-prefix>
// Renders every <prefix>*.html in <dir> to <dir>/out/<name>.jpg at 1080x1350.
// Setup once in <dir>: npm i @fontsource/montserrat  (Google Fonts is blocked in the sandbox)
// Needs playwright (global at /opt/npm-tools) and Chromium at /opt/pw-browsers/chromium.
const {chromium}=require('/opt/npm-tools/node_modules/playwright');
const fs=require('fs');
const dir=process.argv[2]||'.', prefix=process.argv[3]||'';
const css=[400,600,700,800].map(w=>`@font-face{font-family:Montserrat;font-weight:${w};src:url(file://${dir}/node_modules/@fontsource/montserrat/files/montserrat-latin-${w}-normal.woff2)}`).join('');
(async()=>{
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await b.newPage({viewport:{width:1080,height:1350}});
fs.mkdirSync(dir+'/out',{recursive:true});
for(const f of fs.readdirSync(dir).filter(f=>f.startsWith(prefix)&&f.endsWith('.html'))){
 await p.goto('file://'+dir+'/'+f);
 await p.addStyleTag({content:css});
 await p.evaluate(()=>document.fonts.ready);
 await p.waitForTimeout(300);
 await p.screenshot({path:`${dir}/out/${f.replace('.html','.jpg')}`,type:'jpeg',quality:95,clip:{x:0,y:0,width:1080,height:1350}});
}
await b.close();})();
