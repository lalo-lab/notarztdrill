let caseFail=0;
const G=require('../app/src/main/assets/www/grader.js');
global.window={};require('../app/src/main/assets/www/questions.js');const Q=window.QUESTIONS;
let fail=0;
for(const q of Q){const r=G.grade(q,q.a); if(!r.ok){fail++;console.log('SELF-FAIL',q.q,'|',q.a,'|',r.groups.filter(g=>!g.hit).map(g=>g.label));}}
console.log('self fails',fail,'/',Q.length);
const by=s=>Q.find(q=>q.q.startsWith(s));
const cases=[
 ['Reanimation Erwachsene: Adrenalin','1mg iv alle 3 bis 5 Minuten',true],
 ['Reanimation Erwachsene: Adrenalin','1 mg iv alle 5 min',false],
 ['Anaphylaxie Erwachsene: Adrenalin –','500 mikrogramm i.m., nach 5 min wiederholen',true],
 ['Anaphylaxie Erwachsene: Adrenalin –','0,5mg i.v.',false],
 ['Wofür steht SAMPLER','symptome allergien medikamente vorerkrankungen letzte mahlzeit ereignis risikofaktoren',true],
 ['Wofür steht DOPES','Dislokation, Obstruktion, Pneu, Equipment, Magen',true],
 ['Wofür steht DOPES','Dislokation Obstruktion Pneumothorax',false],
 ['Levetiracetam bei Status','60mg/kg max 4,5 g über 10 Minuten',true],
 ['Levetiracetam bei Status','60 mg pro kg, maximal 4.500 mg, 10 min',true],
 ['Hypotonie/Schock: Noradrenalin','0.05 - 0.5 µg/kg/min, push dose 5-10 µg',true],
 ['Anaphylaxie, Kind 2 Jahre','150 mcg = 0.15 ml unverdünnt 1-ml-Spritze',true],
 ['Spannungspneu: Wo','2. ICR medioklavikulär oder 4/5 ICR vordere Axillarlinie',true],
 ['Hinterwandinfarkt','II III aVF',true],
 ['Vorderwandinfarkt','V1 bis V4',true],
 ['Unterlassene Hilfeleistung','§323c StGB',true],
 ['Sichtungskategorie SK IV','blau, keine Überlebenschance',true],
 ['Beckenschlinge: Auf','Höhe Trochanter major',true],
 ['Beckenschlinge: Auf','Beckenkamm',false],
 ['Status epilepticus Stufe 2: Mittel','Keppra, sonst Valproat',true],
 ['Kind 8 Jahre: Tubus','5.5',true],
 ['Kind 8 Jahre: Tubus','6',false],
 ['NIV bei COPD: SpO','88 - 92 %',true],
 ['Epiglottitis: Vorgehen','keine Inspektion des Rachens, Sauerstoff vorhalten, Begleitung in Klinik mit HNO',true],
 ['Tranexamsäure bei Blutung','1g i.v. über 10min innerhalb 3 Stunden',true],
 ['Ist Ketamin beim','nein',true],
 ['Bradykardie: Atropin','',false],
 ['Bradykardie: Atropin','0.5mg bis max 3mg',true],
 ['Wofür steht xABCDE','kritische Blutung, Atemweg, Atmung, Kreislauf, Neurologie, Entkleiden',true],
 ['mSTaRT: Patient befolgt','Rot',true],
 ['MANV: Welche Rolle übernimmt der erste NotSan','Orgl',true],
 ['Wofür steht SPIKES','Setting perception invitation knowledge emotions strategy',true],
 ['Welches Schema wendest du bei Ankunft','4S',true],
 ['Reanimation Kind: Adrenalin','10 µg/kg, max 1 mg, alle 3-5 min',true],
 ['Reanimation Kind: Adrenalin','0,01 mg/kg max 1mg alle 3 bis 5 min',true],
 ['Reanimation Kind: Adrenalin','10mcg/kg max 1mg alle 3-5min',true],
 ['Reanimation Kind: Adrenalin','10 mcg/kg, max. 1000mcg, 3–5 Minuten',true],
 ['Bradykardie: Adrenalin','2-10mcg/min',true],
 ['Bradykardie: Adrenalin','2-10 Mikrogramm pro Minute',true],
 ['Bradykardie: Adrenalin','2-10 mg/min',false],
 ['Anaphylaxie Erwachsene: Adrenalin –','500mcg im, Wdh nach 5min',true],
 ['Bradykardie: Atropin','500mcg bis max. 3mg',true],
 ['Analgesie Kind: Fentanyl','1,5-2mcg/kg',true],
 ['Kind 12 kg: Atropin','240mcg',true],
 ['Tranexamsäure bei Blutung','1000mg iv über 10 min innerhalb von 3h',true],
 ['Reanimation Erwachsene: Adrenalin','1000mcg iv alle 3-5 min',true],
 ['Reanimation Erwachsene: Adrenalin','1 µg iv alle 3-5 min',false],
 ['ACS: Nitroglycerin','0,4-0,8 mg sublingual, RR > 90, kein Viagra, kein Rechtsherzinfarkt',true],
];
for(const [s,a,exp] of cases){const q=by(s); if(!q){console.log('NOQ',s);continue;} const r=G.grade(q,a); if(r.ok!==exp) { caseFail++; } if(r.ok!==exp) console.log('CASE-FAIL',s,'|',a,'->',r.ok,r.groups);}
console.log('done');


if(fail||caseFail){console.error('FEHLER: '+fail+' Selbsttest, '+caseFail+' Testfälle');process.exit(1);}
