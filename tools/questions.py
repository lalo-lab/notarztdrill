# Fragenkatalog NotarztDrill – Quelle: Lernskript ZWB Notfallmedizin ÄKWL Münster
# Q(thema, frage, antwort, schluessel, min)
# schluessel: Gruppen mit ";" getrennt, Alternativen mit "|". Jede Gruppe muss erkannt werden
# (oder mindestens `min` Gruppen).
import json, sys

QS = []
def Q(t, q, a, k, m=None):
    groups = [[alt.strip() for alt in g.split("|") if alt.strip()] for g in k.split(";") if g.strip()]
    d = {"t": t, "q": q, "a": a, "k": groups}
    if m is not None:
        d["m"] = m
    QS.append(d)

# ───────────────────────── Abkürzungen und Schemata ─────────────────────────
A = "Abkürzungen"
Q(A, "Wofür stehen die 4 S?", "Sicherheit, Szene, Situation, Support – bei Ankunft an jeder Einsatzstelle.",
  "Sicherheit;Szene;Situation;Support|Unterstützung")
Q(A, "Welches Schema wendest du bei Ankunft an jeder Einsatzstelle an?", "4 S (Sicherheit, Szene, Situation, Support).",
  "4 S|vier S|4S")
Q(A, "Wofür steht WASB?", "Wach, reagiert auf Ansprache, reagiert auf Schmerz, Bewusstlos – erster Eindruck Bewusstsein.",
  "wach;Ansprache;Schmerz;bewusstlos")
Q(A, "Mit welchem Schema beurteilst du beim ersten Eindruck das Bewusstsein?", "WASB (Wach, Ansprache, Schmerz, Bewusstlos).",
  "WASB|AVPU")
Q(A, "Wofür steht xABCDE?", "eXsanguination (kritische Blutung), Airway, Breathing, Circulation, Disability, Exposure/Environment – Primary Survey.",
  "Exsanguination|kritische Blutung|Blutung;Airway|Atemweg;Breathing|Atmung|Belüftung;Circulation|Kreislauf;Disability|Neurologie|Defizit;Exposure|Environment|Entkleiden|Umgebung|Umfeld")
Q(A, "Welches Schema strukturiert den Primary Survey?", "xABCDE / cABCDE.",
  "xABCDE|cABCDE|ABCDE")
Q(A, "Wofür steht SAMPLER(S)?", "Symptome, Allergien, Medikamente, Patientengeschichte, Letzte Mahlzeit/Stuhlgang/Wasserlassen/Regel, Ereignis, Risikofaktoren, (Schwangerschaft) – Anamnese.",
  "Symptom;Allergie;Medikament;Patientengeschichte|Vorgeschichte|Vorerkrankung;letzte|Mahlzeit;Ereignis;Risikofaktor;Schwangerschaft", 7)
Q(A, "Welches Schema nutzt du für die strukturierte Anamnese?", "SAMPLER(S).",
  "SAMPLER|SAMPLERS|SAMPLE")
Q(A, "Wofür steht OPQRST?", "Onset, Provokation/Linderung, Qualität, Region/Ausstrahlung, Severity (NRS), Time – Schmerzanamnese.",
  "Onset|Beginn;Provokation|Linderung;Qualität;Region|Ausstrahlung;Severity|Stärke|Intensität|NRS;Time|Zeit|Verlauf")
Q(A, "Welches Schema nutzt du für die Schmerzanamnese?", "OPQRST.", "OPQRST")
Q(A, "GCS: Welche drei Komponenten mit welchen Punktwerten, und welche Spanne insgesamt?", "Augen 1–4, verbal 1–5, motorisch 1–6 (gesamt 3–15).",
  "Augen;1-4;verbal|Sprache;1-5;motor;1-6;3-15", 6)
Q(A, "Ab welchem GCS besteht eine Intubationsindikation?", "GCS ≤ 8.", "8")
Q(A, "Welcher Score beschreibt das Bewusstsein und ist bei ≤ 8 Intubationsindikation?", "GCS (Glasgow Coma Scale).", "GCS|Glasgow")
Q(A, "Wofür steht SALAD (ausgeschrieben)?", "Suction Assisted Laryngoscopy and Airway Decontamination.",
  "Suction;Assisted;Laryngoscopy|Laryngoskopie;Airway;Decontamination|Dekontamination")
Q(A, "Welche Technik wendest du bei massivem Erbrechen oder Blut im Atemweg an?", "SALAD: steifer Absauger führt das Laryngoskop, danach im linken Hypopharynx/Ösophagus parken, dann intubieren.",
  "SALAD")
Q(A, "Wofür steht DOPES?", "Dislokation, Obstruktion, Pneumothorax, Equipment, Stomach (Magenüberblähung) – beatmeter Patient verschlechtert sich.",
  "Dislokation;Obstruktion;Pneumothorax|Pneu;Equipment|Gerät|Ausrüstung|Material;Stomach|Magen")
Q(A, "Beatmeter Patient verschlechtert sich – welches Schema arbeitest du ab?", "DOPES.", "DOPES")
Q(A, "qSOFA: Welche drei Kriterien, und ab wie vielen Punkten besteht ein Risiko?", "AF ≥ 22/min, RR syst. ≤ 100 mmHg, veränderte Bewusstseinslage (GCS < 15); ≥ 2 Punkte = Risiko.",
  "22;100;Bewusstsein|GCS|Vigilanz|verwirrt|Bewusstseinslage;2 Punkte|ab 2|2")
Q(A, "Welcher Score dient dem Sepsis-Screening?", "qSOFA.", "qSOFA|SOFA")
Q(A, "Wofür steht CRB-65?", "Confusion, Respiratory rate ≥ 30, Blood pressure syst. < 90 oder diast. ≤ 60, Alter ≥ 65 – Pneumonie-Schweregrad.",
  "Confusion|Verwirrtheit|verwirrt;30;90;60;65|Alter")
Q(A, "Welcher Score beurteilt den Pneumonie-Schweregrad?", "CRB-65.", "CRB 65|CRB|CURB")
Q(A, "Wofür steht BE-FAST?", "Balance, Eyes, Face, Arm, Speech, Time – Schlaganfall; Symptombeginn/„Last seen well“, Wake-up-Stroke.",
  "Balance|Gleichgewicht;Eyes|Augen|Sehen;Face|Gesicht;Arm;Speech|Sprache;Time|Zeit")
Q(A, "Welches Schema nutzt du bei Verdacht auf Schlaganfall?", "BE-FAST.", "BE FAST|BEFAST|FAST")
Q(A, "Welche 5 NEXUS-Kriterien kennst du, und was bedeutet es, wenn alle erfüllt sind?", "Keine Mittellinien-Druckdolenz, keine Intoxikation, wach/orientiert, keine fokale Neurologie, keine ablenkende Verletzung. Alle 5 erfüllt = keine HWS-Immobilisation nötig.",
  "Mittellinie|Druckdolenz|Druckschmerz;Intoxikation|Intox;wach|orientiert;fokal|Neurologie;ablenkend;keine Immobilisation|nicht immobilisieren|keine HWS|Immobilisation", 5)
Q(A, "Welche Kriterien entscheiden, ob keine HWS-Immobilisation nötig ist?", "NEXUS-Kriterien.", "NEXUS")
Q(A, "Nenne die 4 H und 4 T (HITS).", "Hypoxie, Hypovolämie, Hypo-/Hyperkaliämie/metabolisch, Hypothermie; Herzbeuteltamponade, Intoxikation, Thrombose (koronar/pulmonal), Spannungspneu.",
  "Hypoxie;Hypovolämie;Kaliämie|Kalium|metabolisch;Hypothermie;Tamponade;Intoxikation|Intox;Thrombose|Embolie|Infarkt;Spannungspneu", 7)
Q(A, "Welche Merkhilfe fasst die reversiblen Ursachen bei Reanimation zusammen?", "HITS / 4 H, 4 T.", "HITS|4 H|4H|4 T")
Q(A, "Welche Schritte hat mSTaRT (Merkhilfe)?", "Gehen, Bluten, Atmen, Puls, Befolgen.",
  "gehen|gehfähig;bluten|Blutung;atmen|Atmung;Puls;befolgen|Aufforderung")
Q(A, "Welches Sichtungsschema nutzt du beim MANV?", "mSTaRT.", "mSTaRT|START")
Q(A, "Wofür steht SPIKES?", "Setting, Perception, Invitation, Knowledge, Emotions, Strategy/Summary – schlechte Nachrichten überbringen.",
  "Setting;Perception|Wahrnehmung;Invitation|Einladung;Knowledge|Wissen;Emotion;Strategy|Summary|Zusammenfassung|Strategie")
Q(A, "Welches Schema nutzt du, um schlechte Nachrichten zu überbringen?", "SPIKES.", "SPIKES")
Q(A, "Wofür steht ISBAR?", "Identifikation, Situation, Background, Assessment, Recommendation – strukturierte Übergabe.",
  "Identifikation;Situation;Background|Hintergrund;Assessment|Einschätzung|Bewertung;Recommendation|Empfehlung")
Q(A, "Welches Schema nutzt du für die strukturierte Übergabe?", "SBAR / ISBAR.", "ISBAR|SBAR")
Q(A, "STU: Wofür steht es, und in welcher Reihenfolge untersuchst du?", "Schnelle Trauma-Untersuchung: Kopf → Hals (Trachea, Halsvenen, HWS) → Thorax (Inspektion, Palpation, Auskultation) → Abdomen → Becken (nicht rütteln) → Beine → Arme → Rücken beim Drehen.",
  "schnelle;Trauma;Untersuchung;Kopf;Hals;Thorax;Abdomen|Bauch;Becken;Beine;Arme;Rücken", 10)
Q(A, "Wofür steht DCAP-BTLS (Befunde der STU)?", "Deformität, Kontusion, Abschürfung, Penetration, Verbrennung, Druckschmerz, Riss, Schwellung.",
  "Deformität;Kontusion|Prellung;Abschürfung;Penetration;Verbrennung;Druckschmerz;Riss|Lazeration;Schwellung", 7)
Q(A, "Was machst du beim kritischen Traumapatienten (Hochrasanz, Vitalbedrohung) in 60–90 s parallel zu xABCDE?", "STU – schneller Ganzkörpercheck (Schnelle Trauma-Untersuchung).",
  "STU|schnelle Trauma|Ganzkörper|Bodycheck")
Q(A, "Wie lange dauert die STU beim kritischen Traumapatienten?", "60–90 s, parallel zu xABCDE.", "60-90")

# ───────────────────────── Dosistabelle Erwachsene ─────────────────────────
D = "Dosis Erwachsene"
Q(D, "Reanimation Erwachsene: Adrenalin – Dosis, Weg und Intervall?", "1 mg i.v./i.o. alle 3–5 min.",
  "1 mg|1000 µg;i.v.|i.o.|intravenös|intraossär;3-5")
Q(D, "Reanimation: Wann gibst du das erste Adrenalin bei VF, wann bei Asystolie/PEA?", "VF: ab dem 3. Schock. Asystolie/PEA: sofort (so früh wie möglich).",
  "3|dritten;sofort|früh|so früh wie möglich|direkt")
Q(D, "Reanimation VF: Welche zwei Medikamente gibst du nach dem 3. Schock?", "Adrenalin 1 mg + Amiodaron 300 mg.",
  "Adrenalin;Amiodaron")
Q(D, "Amiodaron bei VF: Dosen und Zeitpunkte?", "300 mg nach dem 3. Schock, 150 mg nach dem 5. Schock.",
  "300;3|dritten;150;5|fünften")
Q(D, "Anaphylaxie Erwachsene: Adrenalin – Dosis, Weg und Wiederholung?", "0,5 mg i.m. (0,01 mg/kg), Wiederholung nach 5 min; i.v. nur titriert in 10–50-µg-Boli.",
  "0,5 mg|500 µg|0,01 mg/kg;i.m.|intramuskulär;5 min")
Q(D, "Anaphylaxie Erwachsene: Wie gibst du Adrenalin i.v.?", "Nur titriert in 10–50-µg-Boli.",
  "titr;10-50;µg")
Q(D, "Anaphylaxie: Welches Medikament ist 1. Wahl?", "Adrenalin (0,5 mg i.m.).", "Adrenalin")
Q(D, "Anaphylaxie: Welche Medikamente gibst du nur ergänzend?", "Prednisolon und Dimetinden.", "Prednisolon|Kortison|Steroid;Dimetinden|Fenistil|Antihistamin")
Q(D, "Bradykardie: Atropin – Dosis und Maximaldosis?", "0,5 mg i.v., wiederholt bis max. 3 mg.", "0,5 mg|500 µg;3 mg")
Q(D, "Bradykardie: Welches Medikament ist 1. Wahl?", "Atropin.", "Atropin")
Q(D, "Bradykardie: Adrenalin – Dosierung?", "2–10 µg/min i.v.", "2-10;µg/min")
Q(D, "Schmalkomplex-Tachykardie: Adenosin – Dosierung?", "6 mg schnell i.v., dann 12 mg, ggf. erneut 12–18 mg.",
  "6 mg;12 mg;schnell|rasch|Bolus")
Q(D, "Stabile Schmalkomplex-Tachykardie: Welches Medikament nach vagalen Manövern?", "Adenosin.", "Adenosin|Adrekar")
Q(D, "Hypotonie/Schock: Noradrenalin – Perfusor-Dosis und Push-dose?", "0,05–0,5 µg/kg/min; Push-dose 5–10 µg.",
  "0,05-0,5;µg/kg/min;5-10")
Q(D, "Hypotonie/Schock: Welcher Vasopressor?", "Noradrenalin.", "Noradrenalin")
Q(D, "Esketamin zur Analgesie (Erwachsene): Dosis?", "0,125–0,25 mg/kg i.v.", "0,125-0,25;mg/kg")
Q(D, "Analgosedierung: Welche Kombination und welche Dosen?", "Esketamin 0,25–0,5 mg/kg + Midazolam 1–2 mg.",
  "Esketamin|Ketamin;0,25-0,5;Midazolam;1-2 mg")
Q(D, "Esketamin zur Narkose (Erwachsene): Dosis, und was gilt im Schock?", "0,5–1 mg/kg, im Schock eher unteres Ende.",
  "0,5-1;mg/kg;unter|niedrig|reduz|weniger")
Q(D, "Fentanyl zur Analgesie (Erwachsene): Dosis?", "1–2 µg/kg (0,05–0,1 mg titriert).", "1-2 µg/kg|0,05-0,1 mg|50-100 µg")
Q(D, "Morphin zur Analgesie: Dosis und Schrittgröße?", "0,05–0,1 mg/kg in 2–3-mg-Schritten.", "0,05-0,1;mg/kg;2-3")
Q(D, "Analgesie Erwachsene: Welche drei Medikamente stehen in der Dosistabelle?", "Esketamin, Fentanyl, Morphin.", "Esketamin|Ketamin;Fentanyl;Morphin")
Q(D, "Propofol zur Narkose: Dosis, und was gilt im Schock?", "1–2 mg/kg, im Schock meiden oder stark reduzieren.",
  "1-2;mg/kg;meiden|vermeiden|reduz|nicht")
Q(D, "Etomidat zur Narkose: Dosis?", "0,2–0,3 mg/kg.", "0,2-0,3;mg/kg")
Q(D, "Narkose-Hypnotika in der Dosistabelle: welche drei?", "Esketamin, Propofol, Etomidat.", "Esketamin|Ketamin;Propofol;Etomidat")
Q(D, "Rocuronium zur RSI: Dosis?", "1–1,2 mg/kg.", "1-1,2;mg/kg")
Q(D, "Succinylcholin: Dosis?", "1–1,5 mg/kg.", "1-1,5;mg/kg")
Q(D, "Relaxierung: Welche zwei Relaxanzien stehen in der Tabelle?", "Rocuronium (1–1,2 mg/kg) und Succinylcholin (1–1,5 mg/kg).", "Rocuronium|Esmeron;Succinylcholin|Suxamethonium|Lysthenon|Succi")
Q(D, "Tranexamsäure bei Blutung: Dosis, Gabe und Zeitfenster?", "1 g i.v. über 10 min, innerhalb von 3 h.",
  "1 g|1000 mg;10 min;3 h")
Q(D, "Blutung/Trauma: Welches Antifibrinolytikum gibst du?", "Tranexamsäure (TXA).", "Tranexamsäure|TXA|Cyklokapron")
Q(D, "ACS: ASS – Dosis p.o. und i.v.?", "150–300 mg p.o. oder 75–250 mg i.v. (in DE oft 250–500 mg).",
  "150-300;75-250|250-500")
Q(D, "ACS: Welche drei Medikamente stehen in der Dosistabelle?", "ASS, Heparin, Nitroglycerin.", "ASS|Aspirin|Acetylsalicyl;Heparin;Nitro")
Q(D, "ACS/STEMI: Heparin – Dosis?", "70–100 IE/kg, meist 5.000 IE.", "70-100|5000")
Q(D, "ACS: Nitroglycerin – Dosis, Weg und Voraussetzungen?", "0,4–0,8 mg s.l., nur bei RR syst. > 90, kein PDE-5-Hemmer, kein Rechtsherzinfarkt.",
  "0,4-0,8;s.l.|sublingual|Spray|Hub;90;PDE|Sildenafil|Viagra|Potenzmittel;Rechtsherz|rechtsventrikulär|Hinterwand", 4)
Q(D, "Hypoglykämie Erwachsene: Glukose – Dosis und Beispiel?", "8–10 g i.v. titriert (z. B. G20 40–50 ml).",
  "8-10 g|8-10;titr|G20|40-50")
Q(D, "Hypoglykämie: Warum G40 nicht (peripher)?", "G40 ist venenreizend – besser G10/G20 titriert.", "venenreiz|reizt|Phlebitis|Nekrose|hyperton")
Q(D, "Status epilepticus Stufe 1: Welche Medikamente und Dosen?", "Lorazepam 0,1 mg/kg i.v. (max. 4 mg pro Gabe) / Midazolam 10 mg i.m. oder i.n.",
  "Lorazepam|Tavor;0,1 mg/kg;4 mg;Midazolam;10 mg;i.m.|intranasal|nasal|intramuskulär", 5)
Q(D, "Status epilepticus Stufe 2: Mittel der Wahl und Alternative?", "Levetiracetam, alternativ Valproat.", "Levetiracetam|Keppra;Valproat|Valproinsäure|Ergenyl")
Q(D, "Levetiracetam bei Status epilepticus: Dosis, Maximaldosis, Gabe?", "60 mg/kg, max. 4.500 mg, über 10 min.",
  "60;mg/kg;4500|4,5 g;10 min")
Q(D, "Valproat bei Status epilepticus: Dosis und Maximaldosis?", "40 mg/kg, max. 3.000 mg.", "40;mg/kg;3000|3 g")
Q(D, "Status epilepticus: Lorazepam wirkt nicht – Stufenschema?", "Höher dosieren, dann Levetiracetam bis 4.500 mg, dann Narkose und Intubation.",
  "Levetiracetam|Keppra;Narkose|Intubation")
Q(D, "Asthma/COPD: Welche zwei Inhalativa und welche Dosen?", "Salbutamol 2,5–5 mg + Ipratropium 0,5 mg vernebelt.",
  "Salbutamol|Sultanol;2,5-5;Ipratropium|Atrovent;0,5")
Q(D, "Schweres Asthma: Reproterol und Magnesium – Dosen?", "Reproterol 0,09 mg langsam i.v. / Magnesium 2 g i.v. über 20 min.",
  "0,09;langsam;2 g;20 min")
Q(D, "Schweres Asthma: Welche zwei i.v.-Medikamente zusätzlich?", "Reproterol und Magnesium.", "Reproterol|Bronchospasmin;Magnesium")
Q(D, "Prednisolon: Dosis bei Asthma/COPD und bei Anaphylaxie?", "50–100 mg (Asthma/COPD), 250 mg (Anaphylaxie) i.v.", "50-100;250")
Q(D, "Anaphylaxie: Dimetinden – Dosis und Stellenwert?", "0,1 mg/kg (4–8 mg) i.v., nur ergänzend.", "0,1 mg/kg|4-8;ergänz|zusätzlich|nur")
Q(D, "Hypertensiver Notfall: Medikament, Dosis und Senkungsziel?", "Urapidil 5–25 mg titriert, um max. 20–25 % senken.",
  "Urapidil|Ebrantil;5-25;20-25")
Q(D, "Opioid-Intoxikation: Medikament, Dosis und Ziel?", "Naloxon 0,04–0,4 mg titriert, Ziel Atmung, nicht Wachheit.",
  "Naloxon|Narcanti;0,04-0,4;Atmung")
Q(D, "Benzodiazepin-Intoxikation: Medikament, Dosis und Risiko?", "Flumazenil 0,2 mg titriert (Krampfrisiko).",
  "Flumazenil|Anexate;0,2;Krampf")
Q(D, "Für welches Körpergewicht gelten die Standarddosen der Erwachsenen-Tabelle?", "70–80 kg.", "70-80")

# ───────────────────────── Dosistabelle Kinder ─────────────────────────
K = "Dosis Kinder"
Q(K, "Faustformel (1–10 J.): geschätztes Gewicht?", "Gewicht = (Alter + 4) × 2 kg.", "Alter;4;2")
Q(K, "Faustformel (1–10 J.): Tubus-ID gecufft?", "Tubus ID gecufft = Alter/4 + 3,5.", "Alter;4;3,5")
Q(K, "Faustformel (1–10 J.): minimaler systolischer Blutdruck?", "RR syst. minimal = 70 + 2 × Alter mmHg.", "70;2;Alter")
Q(K, "Kind 2 Jahre: geschätztes Gewicht?", "(2 + 4) × 2 = 12 kg.", "12")
Q(K, "Kind 4 Jahre: geschätztes Gewicht?", "(4 + 4) × 2 = 16 kg.", "16")
Q(K, "Kind 8 Jahre: geschätztes Gewicht?", "(8 + 4) × 2 = 24 kg.", "24")
Q(K, "Kind 4 Jahre: Tubus-ID gecufft?", "4/4 + 3,5 = 4,5.", "4,5")
Q(K, "Kind 8 Jahre: Tubus-ID gecufft?", "8/4 + 3,5 = 5,5.", "5,5")
Q(K, "Kind 5 Jahre: minimaler systolischer Blutdruck?", "70 + 2 × 5 = 80 mmHg.", "80")
Q(K, "Was tust du beim Kind immer zuerst, bevor du Dosen rechnest?", "Gewicht schätzen und laut sagen, dann rechnen.", "Gewicht;laut|sagen|ansagen", 1)
Q(K, "Reanimation Kind: Adrenalin – Dosis, Maximum, Intervall?", "10 µg/kg i.v./i.o. (max. 1 mg) alle 3–5 min.",
  "10 µg/kg|0,01 mg/kg;1 mg;3-5")
Q(K, "Reanimation Kind 12 kg: Adrenalin-Dosis?", "120 µg.", "120 µg|0,12 mg|120")
Q(K, "Reanimation Kind: Defibrillation – Energie?", "4 J/kg, refraktär bis 8 J/kg (max. 360 J).", "4 J/kg|4;8;360", 2)
Q(K, "Reanimation Kind 12 kg: Defibrillationsenergie?", "50 J (4 J/kg).", "50|48")
Q(K, "Reanimation Kind VF: Amiodaron – Dosis und Zeitpunkte?", "5 mg/kg nach dem 3. und 5. Schock.", "5 mg/kg;3|dritten;5|fünften", 2)
Q(K, "Reanimation Kind 12 kg: Amiodaron-Dosis?", "60 mg.", "60")
Q(K, "Anaphylaxie Kind: Adrenalin i.m. – Dosen nach Altersgruppe?", "6 Mon.–6 J.: 150 µg · 6–12 J.: 300 µg · > 12 J.: 500 µg.",
  "150;300;500")
Q(K, "Anaphylaxie, Kind 2 Jahre: Adrenalin i.m. – Dosis und wie zieht der NotSan auf?", "150 µg = 0,15 ml aus 1 mg/ml (unverdünnt) in einer 1-ml-Spritze.",
  "150 µg|0,15 mg;0,15 ml;1 mg/ml|unverdünnt|1:1000;1 ml|Tuberkulin")
Q(K, "Krupp/Anaphylaxie Atemweg: Adrenalin vernebelt beim Kind – Dosierung?", "1 mg/ml unverdünnt, 0,5 ml/kg, max. 5 ml.",
  "unverdünnt|1 mg/ml;0,5 ml/kg;5 ml")
Q(K, "Kind 12 kg: Wie viel Adrenalin vernebelt?", "5 ml (0,5 ml/kg = 6 ml, max. 5 ml).", "5 ml|5")
Q(K, "Krupp: Welche Steroide und Dosen?", "Prednisolon 100 mg rektal / Dexamethason 0,15–0,6 mg/kg p.o.",
  "Prednisolon|Rectodelt;100;Dexamethason;0,15-0,6")
Q(K, "Asthma Kind: Salbutamol vernebelt – Dosis?", "< 5 J.: 2,5 mg · ≥ 5 J.: 5 mg.", "2,5;5")
Q(K, "Analgesie Kind: Esketamin – Dosis i.v. und i.n.?", "i.v. 0,25–0,5 mg/kg · i.n. 0,5–1 mg/kg.",
  "0,25-0,5;0,5-1")
Q(K, "Analgesie Kind: Fentanyl intranasal – Dosis?", "1,5–2 µg/kg.", "1,5-2;µg/kg")
Q(K, "Kind 12 kg: Fentanyl intranasal – Dosis?", "18–24 µg.", "18-24")
Q(K, "Fieber/Schmerz Kind: Paracetamol und Ibuprofen – Dosen?", "Paracetamol 15 mg/kg / Ibuprofen 10 mg/kg.", "15 mg/kg|15;10 mg/kg|10")
Q(K, "Kind 12 kg: Paracetamol- und Ibuprofen-Dosis?", "180 mg / 120 mg.", "180;120")
Q(K, "Krampfanfall Kind: Midazolam buccal/i.n. – Dosis, Maximum, Buccolam 1–5 J.?", "0,2–0,3 mg/kg (max. 10 mg); Buccolam 1–5 J.: 5 mg.",
  "0,2-0,3;10 mg;5 mg")
Q(K, "Krampfanfall Kind: Midazolam i.v. und Diazepam rektal – Dosen?", "Midazolam i.v. 0,1 mg/kg / Diazepam rektal < 15 kg 5 mg, > 15 kg 10 mg.",
  "0,1 mg/kg|0,1;15 kg;5 mg;10 mg")
Q(K, "Volumen Kind: Vollelektrolytlösung – Dosierung?", "10 ml/kg Bolus, dann neu beurteilen.", "10 ml/kg|10;neu beurteilen|reevaluieren|beurteilen|reevaluation")
Q(K, "Kind 12 kg: Volumenbolus?", "120 ml.", "120")
Q(K, "Hypoglykämie Kind: Glukose – Dosis?", "0,2 g/kg = 2 ml/kg G10.", "0,2 g/kg|2 ml/kg;G10")
Q(K, "Kind 12 kg: Glukose bei Hypoglykämie?", "24 ml G10.", "24;G10")
Q(K, "Bradykardie Kind: Atropin – Dosis?", "20 µg/kg.", "20 µg/kg|0,02 mg/kg")
Q(K, "Kind 12 kg: Atropin-Dosis?", "240 µg.", "240|0,24")
Q(K, "Normwerte Säugling: HF und AF?", "HF 110–160/min, AF 30–40/min.", "110-160;30-40")
Q(K, "Normwerte 1–2 Jahre: HF und AF?", "HF 100–150/min, AF 25–35/min.", "100-150;25-35")
Q(K, "Normwerte 2–5 Jahre: HF und AF?", "HF 95–140/min, AF 25–30/min.", "95-140;25-30")
Q(K, "Normwerte 5–12 Jahre: HF und AF?", "HF 80–120/min, AF 20–25/min.", "80-120;20-25")
Q(K, "Normwerte > 12 Jahre: HF und AF?", "HF 60–100/min, AF 15–20/min.", "60-100;15-20")
Q(K, "Kind ohne Zugang, Krampfanfall: Medikament und Weg?", "Midazolam buccal oder intranasal (Buccolam 1–5 J.: 5 mg).", "Midazolam|Buccolam;buccal|bukkal|intranasal|nasal")

# ───────────────────────── Trauma und Polytrauma ─────────────────────────
T = "Trauma"
Q(T, "Polytrauma: Was tust du schon auf der Anfahrt?", "Meldebild bewerten, RTH sofort nachfordern, Feuerwehr (technische Rettung, Absicherung, Licht), Polizei, Zielklinik (überregionales Traumazentrum) mit dem NEF-Fahrer besprechen, Aufgaben vorverteilen.",
  "Meldebild;RTH|Hubschrauber;Feuerwehr;Polizei;Zielklinik|Traumazentrum;Aufgaben|vorverteilen", 5)
Q(T, "Bei Hochrasanz-Meldebild: Welches Rettungsmittel forderst du sofort von der Anfahrt aus an?", "RTH.", "RTH|Hubschrauber|Christoph")
Q(T, "Welche Zielklinik besprichst du beim Polytrauma?", "Überregionales Traumazentrum.", "überregional;Traumazentrum")
Q(T, "X: Wie legst du das Tourniquet an?", "„High and tight“, Uhrzeit notieren.", "high|hoch|proximal;tight|fest|straff;Uhrzeit|Zeit")
Q(T, "X: Blutung rumpfnah (kein Tourniquet möglich) – Maßnahme?", "Hämostyptikum + Druckverband.", "Hämostypt|Hämostat|Packing|Tamponade;Druckverband|Druck")
Q(T, "A beim Trauma: Welche Maßnahmen?", "Helmabnahme zu zweit, manuelle Inline-Stabilisierung, Absaugen, ggf. SALAD.",
  "Helm;Inline|manuelle|Stabilisierung;absaugen|Absaugung;SALAD", 3)
Q(T, "Spannungspneu: Wo punktierst du mit der Nadel?", "2. ICR MCL oder 4./5. ICR vordere Axillarlinie.",
  "2;ICR|Interkostal;MCL|medioklavikular|Medioklavikularlinie;Axillar", 3)
Q(T, "Nach der Nadeldekompression: Wo und wie machst du die Minithorakotomie?", "4./5. ICR vordere bis mittlere Axillarlinie, stumpf, Fingerexploration, kein Trokar.",
  "4|5;Axillar;stumpf;Finger;Trokar|kein Trokar", 4)
Q(T, "Beckenschlinge: Auf welcher Höhe?", "Auf Höhe der Trochanteren major.", "Trochanter")
Q(T, "Beckenschlinge zu hoch angelegt – Folge?", "Wirkungslos bzw. destabilisierend.", "wirkungslos|unwirksam|nutzlos|ineffektiv|destabil")
Q(T, "C beim Trauma: Welche Maßnahmen?", "Beckenschlinge, 2 großlumige Zugänge oder i.o., TXA 1 g über 10 min, VEL restriktiv, Noradrenalin, Calcium erwägen, eFAST wenn ohne Zeitverlust.",
  "Becken;Zugang|Zugänge|i.o.;TXA|Tranexam;restriktiv|VEL|Volumen;Noradrenalin;Calcium|Kalzium;eFAST|Sono|Ultraschall", 5)
Q(T, "D beim Trauma: Was erhebst du?", "GCS einzeln rechnen, Pupillen, BZ; GCS ≤ 8 = Intubation.", "GCS;Pupille;BZ|Blutzucker")
Q(T, "E beim Trauma: Was beachtest du, und wo entkleidest du vollständig?", "Wärmeerhalt; vollständig entkleiden erst im warmen RTW.", "Wärme|Wärmeerhalt|Hypothermie|warm;RTW|Rettungswagen")
Q(T, "Blutdruckziel bei Blutung ohne SHT?", "Permissive Hypotension: syst. 80–90 mmHg, MAP 50–65.", "80-90;50-65|permissiv", 1)
Q(T, "Blutdruckziel bei Blutung mit SHT?", "Keine permissive Hypotension: syst. ≥ 90, nach S3 Polytrauma eher MAP ≥ 80 mmHg.", "90;80")
Q(T, "Letale Trias – und was kommt beim „Diamond“ dazu?", "Hypothermie, Azidose, Koagulopathie; „Diamond“ plus Hypokalzämie.",
  "Hypothermie|Unterkühlung;Azidose;Koagulopathie|Gerinnung;Hypokalzämie|Calcium|Kalzium")
Q(T, "SHT: Welche Ziele für Oxygenierung, Beatmung und Lagerung?", "Normoxie (SpO₂ ≥ 94 %), Normokapnie (etCO₂ 35–40 mmHg), Oberkörper 30° bei stabilem Kreislauf, keine prophylaktische Hyperventilation.",
  "94;35-40;30;Hyperventil", 3)
Q(T, "SHT: Wann darfst du hyperventilieren?", "Nur bei Einklemmungszeichen kurzfristig moderat.", "Einklemm|Herniation")
Q(T, "HWS: Reicht ein Stiffneck allein?", "Nein, er immobilisiert nicht sicher; manuelle Stabilisierung bleibt wichtig.", "nein|nicht;manuell")
Q(T, "Nenne die drei Rettungsarten.", "Sofortrettung, schnelle (zeitkontrollierte) Rettung, patientenorientierte (schonende) Rettung.",
  "Sofort;schnell|zeitkontroll|zeitkritisch;patientenorientiert|schonend")
Q(T, "Sofortrettung: Wann und wie?", "Sekunden, ohne Rücksicht auf Schäden (Feuer, Reanimation).", "Sekunde|ohne Rücksicht;Feuer|Brand|Reanimation", 1)
Q(T, "Schnelle (zeitkontrollierte) Rettung: Für wen?", "Kritischer Patient, wenige Minuten.", "kritisch|instabil")
Q(T, "Patientenorientierte (schonende) Rettung: Für wen?", "Stabiler Patient, Sekundärschäden vermeiden.", "stabil;Sekundär", 1)
Q(T, "Traumatische Reanimation: Welche Prioritäten?", "Ursachen zuerst, Kompressionen nachrangig: Blutung stoppen, Hypovolämie ausgleichen, Oxygenierung, beidseitige Thoraxentlastung, an Perikardtamponade denken.",
  "Blutung;Hypovol|Volumen;Oxygen|Sauerstoff|Atemweg;Thorax|Entlastung|Dekompression;Tamponade|Perikard", 4)

# ───────────────────────── Reanimation und Rhythmusstörungen ─────────────────────────
R = "Reanimation"
Q(R, "Thoraxkompressionen: Frequenz, Tiefe und weitere Qualitätsmerkmale?", "100–120/min, 5–6 cm tief, vollständige Entlastung, Helferwechsel alle 2 min, Pausen < 5 s.",
  "100-120;5-6;Entlastung;2 min;5 s", 4)
Q(R, "Wie oft Rhythmusanalyse, und wann lädst du den Defibrillator?", "Alle 2 min; während der Kompressionen laden.", "2 min|2;Kompression|drücken")
Q(R, "Schockbarer Rhythmus: Welche Energie (biphasisch)?", "≥ 150 J (geräteabhängig, oft 150–200 J), sofort weiterdrücken.", "150")
Q(R, "Welche Rhythmen sind schockbar, welche nicht?", "Schockbar: VF/pVT. Nicht schockbar: Asystolie/PEA.", "VF|Kammerflimmern;VT|pVT|Tachykardie;Asystolie;PEA|pulslose elektrische")
Q(R, "Adrenalin unter Reanimation: Gibt es eine Maximaldosis?", "Nein, alle 3–5 min ohne Maximaldosis.", "keine|nein|ohne")
Q(R, "Atemweg unter Reanimation: Vorgehen?", "Zunächst Beutel-Maske oder supraglottisch; Intubation nur durch Erfahrene, möglichst Videolaryngoskop, Kompressionspause < 5 s. Danach kontinuierlich drücken, 10 Beatmungen/min.",
  "Beutel|Maske|supraglottisch|Larynx;Erfahren|Video;5 s;10", 3)
Q(R, "Nach Atemwegssicherung unter Reanimation: Beatmungsfrequenz?", "10 Beatmungen/min bei kontinuierlichen Kompressionen.", "10")
Q(R, "Refraktäres VF: Was erwägst du?", "Pad-Position wechseln (anterior-posterior), reversible Ursachen, mechanische Reanimationshilfe, Transport in ein Zentrum mit eCPR.",
  "Pad|Position|anterior|posterior;reversibl|Ursache|HITS;mechanisch|LUCAS|Corpuls;eCPR|ECMO|ECLS", 3)
Q(R, "Kapnografie unter Reanimation: Wichtigste Aufgabe?", "Tubuslage bestätigen (kein CO₂ = Tubus falsch, bis das Gegenteil bewiesen ist).", "Tubus|Lage")
Q(R, "Kein CO₂ in der Kapnografie nach Intubation – Bedeutung?", "Tubus falsch, bis das Gegenteil bewiesen ist.", "falsch|Fehllage|ösophageal|Ösophagus")
Q(R, "Sprunghafter etCO₂-Anstieg unter Reanimation – Bedeutung?", "Hinweis auf ROSC.", "ROSC|Spontankreislauf")
Q(R, "Dauerhaft sehr niedriges etCO₂ unter Reanimation – Abbruchkriterium?", "Ungünstiges Zeichen, aber kein alleiniges Abbruchkriterium.", "nein|kein|nicht")
Q(R, "Kapnografie unter Reanimation: Welche drei Aufgaben?", "Tubuslage bestätigen, Qualität der Kompressionen überwachen, ROSC erkennen (sprunghafter Anstieg).",
  "Tubus|Lage;Qualität|Kompression;ROSC")
Q(R, "Post-ROSC: SpO₂-Ziel?", "94–98 %, FiO₂ reduzieren, Hyperoxie vermeiden.", "94-98")
Q(R, "Post-ROSC: CO₂-Ziel?", "Normokapnie, paCO₂ 35–45 mmHg (etCO₂ liegt bei schlechter Perfusion darunter).", "35-45|Normokapnie")
Q(R, "Post-ROSC: Blutdruckziel?", "MAP > 65 mmHg, Hypotonie vermeiden.", "65")
Q(R, "Post-ROSC: Temperaturziel?", "Fieber > 37,7 °C für mindestens 72 h vermeiden.", "37,7;72")
Q(R, "Post-ROSC: Welche Diagnostik?", "12-Kanal-EKG, BZ, Sono.", "12|EKG;BZ|Blutzucker;Sono|Ultraschall")
Q(R, "Post-ROSC: Welche Zielklinik und wie anmelden?", "Cardiac Arrest Center mit 24/7-Herzkatheter, Voranmeldung direkt ins Katheterlabor.",
  "Cardiac Arrest|CAC;Katheter")
Q(R, "STEMI in II, III, aVF: Lokalisation und Besonderheiten?", "Hinterwand (inferior), V4R prüfen, Vorsicht mit Nitro.", "Hinterwand|inferior;V4R|rechts;Nitro", 2)
Q(R, "STEMI in V1–V4: Lokalisation?", "Vorderwand (anterior/septal).", "Vorderwand|anterior|septal")
Q(R, "STEMI in I, aVL, V5–V6: Lokalisation?", "Seitenwand (lateral).", "Seitenwand|lateral")
Q(R, "Hinterwandinfarkt: In welchen Ableitungen?", "II, III, aVF.", "II|2;III|3;aVF")
Q(R, "Vorderwandinfarkt: In welchen Ableitungen?", "V1–V4.", "V1;V4")
Q(R, "Seitenwandinfarkt: In welchen Ableitungen?", "I, aVL, V5–V6.", "aVL;V5|V6")
Q(R, "Bradykardie: Welche Befunde gelten als Asystolierisiko?", "Kürzliche Asystolie, Mobitz II, AV-Block III mit breitem QRS, Pausen > 3 s.",
  "Asystolie;Mobitz;AV Block|AV-Block III|drittgradig;3 s|Pause", 3)
Q(R, "Bradykardie mit Asystolierisiko: Optionen?", "Früh pacen oder Adrenalin 2–10 µg/min bzw. Isoprenalin 5 µg/min.", "pacen|Pacing|Schrittmacher;Adrenalin;Isoprenalin", 2)
Q(R, "Isoprenalin bei Bradykardie: Dosis?", "5 µg/min.", "5 µg/min|5")
Q(R, "Transkutanes Pacing: Einstellungen und Vorgehen?", "Elektroden anterior-posterior, Modus Demand, Frequenz 60–70/min, Stromstärke steigern bis elektrisches und mechanisches Capture, Puls femoral tasten, Analgosedierung.",
  "anterior|posterior;Demand;60-70;Capture|Strom;femoral;Analgosed|Sedierung", 4)
Q(R, "Tachykardie: Welche Instabilitätszeichen?", "Schock, Synkope, Ischämie, Herzinsuffizienz.", "Schock;Synkope;Ischämie;Herzinsuffizienz|Lungenödem", 3)
Q(R, "Tachykardie mit Instabilitätszeichen: Therapie?", "Synchronisierte Kardioversion unter Analgosedierung.", "synchron|Kardioversion;Analgosed|Sedierung|Narkose")
Q(R, "Stabile Tachykardie mit schmalem QRS: Therapie?", "Vagale Manöver, dann Adenosin.", "vagal|Valsalva;Adenosin")
Q(R, "Merke Münster: Asthmatiker mit Luftnot und Tachykardie – woran denken?", "Nicht von Vorerkrankungen blenden lassen – eine AVNRT kann die Luftnot erklären.", "AVNRT|Rhythmus|Tachykardie")
Q(R, "Auf welchen Leitlinien basiert die Reanimation im Lernskript?", "ERC-Leitlinien 2025 (veröffentlicht am 22.10.2025).", "ERC|GRC;2025")

# ───────────────────────── Atemweg und Notfallnarkose ─────────────────────────
W = "Atemweg & Narkose"
Q(W, "Indikationen zur präklinischen Narkose (S1-Leitlinie)?", "Hypoxie trotz O₂ (SpO₂ < 90 %, nach Ausschluss Spannungspneu), schweres SHT (GCS ≤ 8), traumabedingte Kreislaufinstabilität, schweres Thoraxtrauma mit respiratorischer Insuffizienz.",
  "Hypox|90;SHT|GCS;Kreislauf|instabil;Thorax", 3)
Q(W, "Präoxygenierung vor Notfallnarkose: Dauer und womit?", "3–4 min mit dicht sitzender Maske/Reservoir oder NIV, ggf. apnoische Oxygenierung über Nasenbrille.",
  "3-4;Maske|Reservoir|NIV", 2)
Q(W, "Was ist apnoische Oxygenierung bei der Notfallnarkose?", "Sauerstoff über Nasenbrille während der Apnoe/Intubation.", "Nasenbrille")
Q(W, "Lagerung zur Intubation?", "Ohr auf Sternumhöhe.", "Ohr;Sternum")
Q(W, "Notfallnarkose: Welches Atemwegsmaterial liegt bereit?", "Absaugung läuft, Videolaryngoskop + Bougie, Tubus (7,0–8,0) mit Spritze, Larynxtubus bereit, Koniotomie-Set bereit.",
  "Absaug|Sauger;Video;Bougie;Tubus;Larynx|supraglottisch;Konio", 5)
Q(W, "Tubusgröße für Erwachsene bei der Notfallnarkose?", "7,0–8,0.", "7-8|7,0-8,0|7,5")
Q(W, "Notfallnarkose: Monitoring und Kreislaufvorbereitung?", "Kapnografie, zwei sichere Zugänge, Noradrenalin vorbereitet oder laufend, Push-dose-Pressor.",
  "Kapno|CO2;2|zwei|Zugänge|Zugang;Noradrenalin|Pressor|Push", 3)
Q(W, "Was gehört ins Teambriefing vor der Notfallnarkose?", "Wer macht was, ab wann Plan B, Ansage der Medikamente.", "wer|Rolle|Aufgabe;Plan B;Medikament|Ansage")
Q(W, "Häufigster Fallstrick bei der Notfallnarkose im Schock?", "Die Klinik-Routine mit Propofol – im Schock gefährlich.", "Propofol")
Q(W, "Kreislaufschonende RSI im Schock: Medikamente und Dosen?", "Esketamin 0,5–1 mg/kg + Fentanyl reduziert (1–2 µg/kg) + Rocuronium 1–1,2 mg/kg.",
  "Esketamin|Ketamin;0,5-1;Fentanyl;1-2;Rocuronium;1-1,2", 5)
Q(W, "Ist Ketamin beim beatmeten SHT-Patienten kontraindiziert?", "Nein, nicht kontraindiziert.", "nein|nicht")
Q(W, "Plan A/B/C: Was bezieht sich darauf?", "Auf den Atemweg (nicht auf Medikamente).", "Atemweg")
Q(W, "Atemweg Plan A?", "Videolaryngoskop + Bougie, max. 2 Versuche.", "Video;Bougie;2", 2)
Q(W, "Atemweg Plan B?", "Supraglottischer Atemweg (Larynxtubus/-maske), oxygenieren.", "supraglott|Larynx|LMA|i-gel")
Q(W, "Atemweg Plan C?", "Koniotomie („cannot intubate, cannot oxygenate“).", "Koniotomie|Konio|Krikothyreotomie")
Q(W, "Wie viele Intubationsversuche bei Plan A?", "Maximal 2.", "2|zwei")
Q(W, "Nach der Intubation: Kontrolle und Beatmungsziele?", "Kapnografie als Lagekontrolle, Auskultation, Tubus fixieren, SpO₂ ≥ 94 %, etCO₂ 35–40 mmHg, Vt 6–8 ml/kg ideales Körpergewicht, PEEP 5, Narkose fortführen.",
  "Kapno;Auskult;fixier;94;35-40;6-8;PEEP|5", 5)
Q(W, "Beatmung nach Intubation: Tidalvolumen und PEEP?", "Vt 6–8 ml/kg ideales Körpergewicht, PEEP 5.", "6-8;ideal|ml/kg;5", 2)
Q(W, "NIV bei COPD/Lungenödem: Modus und Drücke?", "CPAP/ASB, PEEP 5–8 mbar, ASB 5–10 mbar über PEEP steigern, FiO₂ nach SpO₂.",
  "CPAP|ASB;5-8;5-10")
Q(W, "NIV bei COPD: SpO₂-Ziel?", "88–92 %.", "88-92")
Q(W, "NIV: Womit verbesserst du die Toleranz?", "Leichte Sedierung mit Morphin 2–3 mg.", "Morphin;2-3")
Q(W, "NIV: Kontraindikationen?", "Bewusstlosigkeit, fehlende Schutzreflexe, Erbrechen/Aspirationsgefahr, Gesichtsverletzung, Pneumothorax, Kreislaufschock.",
  "Bewusstlos|Vigilanz;Schutzreflex;Erbrech|Aspiration;Gesicht;Pneumothorax|Pneu;Schock|Kreislauf", 4)
Q(W, "Warum Intubation bei exazerbierter COPD vermeiden?", "Schwieriges Weaning, höhere Mortalität.", "Weaning|Entwöhnung;Mortalität|Sterblichkeit")
Q(W, "Tracheostoma mit Atemnot: Vorgehen?", "Kanüle oft verlegt: Innenkanüle ziehen, absaugen, im Zweifel ganze Kanüle entfernen und über das Stoma beatmen.",
  "Innenkanüle;absaugen|Absaugung;entfern|ziehen;Stoma", 3)
Q(W, "Laryngektomierter Patient: Wo ist der Atemweg?", "Nur über das Stoma.", "Stoma")
Q(W, "SALAD: Wie gehst du technisch vor?", "Steifer Absauger voraus, Laryngoskop hinterher, Sauger links im Hypopharynx parken, dann intubieren.",
  "Absauger|Sauger;voraus|zuerst|führt;links|Hypopharynx|parken|Ösophagus", 2)

# ───────────────────────── Pädiatrie ─────────────────────────
P = "Pädiatrie"
Q(P, "Pädiatrisches Beurteilungsdreieck: Die drei Seiten?", "Aussehen, Atemarbeit, Hautdurchblutung.", "Aussehen|Erscheinung;Atemarbeit|Atmung;Haut|Durchblutung|Zirkulation")
Q(P, "Beurteilungsdreieck „Aussehen“: Worauf achtest du?", "Tonus, Interaktion, Blick, Sprache/Schreien.", "Tonus;Interaktion;Blick;Sprache|Schreien", 3)
Q(P, "Beurteilungsdreieck „Atemarbeit“: Worauf achtest du?", "Geräusche, Einziehungen, Nasenflügeln.", "Geräusch|Stridor;Einziehung;Nasenflügel", 2)
Q(P, "Beurteilungsdreieck „Hautdurchblutung“: Worauf achtest du?", "Blässe, Marmorierung, Zyanose.", "Blässe|blass;Marmor;Zyanose", 2)
Q(P, "Kinder allgemein: Welche drei Grundregeln?", "Gewicht schätzen, Kind beim Elternteil lassen, nicht aufregen.", "Gewicht;Eltern|Mutter|Vater;aufreg|Ruhe", 2)
Q(P, "Pseudokrupp: Beginn, Husten, Stimme?", "Nachts nach leichtem Infekt, bellender Husten, heisere Stimme.", "nachts|Nacht;bellend;heiser")
Q(P, "Epiglottitis: Beginn, Husten, Stimme?", "Rasch mit hohem Fieber, eher kein Husten, kloßige Stimme.", "rasch|schnell|plötzlich|Fieber;kein|keiner;kloß")
Q(P, "Epiglottitis: Speichelfluss und Allgemeinzustand?", "Speichelfluss mit Schluckbeschwerden, toxisch, sitzt vornübergebeugt.", "Speichel;toxisch|schlecht|krank;vornüber|sitzt", 2)
Q(P, "Epiglottitis: Vorgehen?", "Keine Racheninspektion, O₂-Vorlage, Begleitung, Klinik mit Anästhesie/HNO.",
  "Rachen|Inspektion|Spatel;O2|Sauerstoff;Begleit;Anästhesie|HNO", 3)
Q(P, "Bei Stridor beim Kind: Was ist absolut verboten?", "Racheninspektion mit Spatel.", "Spatel|Rachen|Inspektion")
Q(P, "Westley-Score: Welche Kriterien?", "Stridor, Einziehungen, Luftstrom, Zyanose, Bewusstsein.", "Stridor;Einziehung;Luftstrom|Belüftung;Zyanose;Bewusstsein", 4)
Q(P, "Westley-Score: Schweregrade nach Punkten?", "0–2 leicht, 3–5 mittelschwer, 6–11 schwer, ≥ 12 drohendes Atemversagen.", "0-2;3-5;6-11;12")
Q(P, "Westley-Score: Punkte für Zyanose und Bewusstsein?", "Zyanose 0, 4 bei Aufregung, 5 in Ruhe; Bewusstsein 0 oder 5.", "4;5")
Q(P, "Krupp-Therapie: Basis und Steroid?", "Ruhe, beim Elternteil lassen, O₂ als Vorlage; Prednisolon 100 mg rektal oder Dexamethason 0,15–0,6 mg/kg p.o.",
  "Ruhe|Eltern;Prednisolon|Dexamethason|Steroid|Kortison;100|0,15-0,6", 2)
Q(P, "Krupp: Ab welchem Schweregrad Adrenalin vernebelt?", "Ab mittelschwer.", "mittel")
Q(P, "Krupp nach Adrenalin vernebelt: Wie lange beobachten und warum?", "Mindestens 2–4 h in der Kinderklinik wegen Rebound.", "2-4;Rebound")
Q(P, "Weitere Differenzialdiagnosen bei Stridor?", "Bakterielle Tracheitis, Fremdkörperaspiration, Anaphylaxie/Angioödem.", "Tracheitis;Fremdkörper;Anaphylax|Angioödem", 2)
Q(P, "Woran erkennst du eine Fremdkörperaspiration beim Kind?", "Plötzlich, beim Spielen/Essen, kein Infekt.", "plötzlich;Spielen|Essen;kein Infekt|Infekt", 2)
Q(P, "Anaphylaxie Kind: Welche Maßnahmen zusätzlich zu Adrenalin i.m.?", "Adrenalin vernebelt, O₂, Volumen; Prednisolon und Dimetinden nur ergänzend.",
  "vernebel;O2|Sauerstoff;Volumen", 2)
Q(P, "Anaphylaxie beim Kind: Darf das Kind zu Hause bleiben?", "Nein, das Kind kommt immer in die Klinik.", "nein|Klinik|immer")
Q(P, "Fieberkrampf/Krampfanfall: Vorgehen?", "Midazolam buccal oder intranasal (Buccolam 1–5 J.: 5 mg), BZ messen, Fieber senken, nach dem ersten Anfall Klinik.",
  "Midazolam|Buccolam;BZ|Blutzucker;Fieber;Klinik", 3)
Q(P, "Schmerztherapie beim Kind ohne Zugang?", "Esketamin oder Fentanyl intranasal (MAD-Zerstäuber).", "Esketamin|Fentanyl|Ketamin;intranasal|nasal|MAD")
Q(P, "Kind: Wann i.o.-Zugang?", "Bei Kreislaufinstabilität ohne Zeitverlust.", "Kreislauf|instabil|Schock")
Q(P, "Verdacht auf Kindeswohlgefährdung (Verletzungsmuster passt nicht): Vorgehen?", "Befunde dokumentieren, Kind in die Klinik bringen, Klinik informieren.",
  "dokument;Klinik;informier|Bescheid|mitteilen", 2)
Q(P, "Wer schaltet bei Kindeswohlgefährdung in der Regel das Jugendamt ein?", "In der Regel die Klinik.", "Klinik|Krankenhaus")

# ───────────────────────── MANV ─────────────────────────
M = "MANV"
Q(M, "MANV: Welche Rolle übernimmt der erste Notarzt vor Ort?", "Kommissarisch die Aufgaben des LNA, bis der LNA eintrifft.", "kommissarisch|vorläufig;LNA|Leitender Notarzt")
Q(M, "MANV: Welche Rolle übernimmt der erste NotSan?", "Kommissarisch die Aufgaben des OrgL.", "OrgL|Organisatorischer Leiter")
Q(M, "MANV: Behandelst du als erster Notarzt?", "Nein – du sichtest und führst, du behandelst nicht.", "nein|nicht;sichten|führen|Sichtung", 1)
Q(M, "MANV: Was gehört in die erste Rückmeldung an die Leitstelle?", "Einsatzstelle, Lage (… gegen …), geschätzte Zahl Verletzte und Eingeklemmte, kommissarische Übernahme der Einsatzleitung RD, Nachforderung: MANV-Stufe nach AAO, LNA und OrgL, RTW, NEF, RTH, Feuerwehr technische Rettung, Polizei; Beginn der Sichtung, Rückmeldung folgt.",
  "Einsatzstelle|Ort;Verletzte|Anzahl;eingeklemmt;kommissarisch|Einsatzleitung;MANV Stufe|AAO;LNA;OrgL;RTW;NEF;RTH;Feuerwehr;Polizei;Sichtung", 9)
Q(M, "MANV-Rückmeldung: Wonach richtet sich die Nachforderung der MANV-Stufe?", "Nach der AAO (Alarm- und Ausrückeordnung).", "AAO|Alarm")
Q(M, "MANV: Was tust du in den ersten Minuten?", "Lage erkunden, Anfahrtsweg und Bereitstellungsraum festlegen, Patientenablage einrichten, Leichtverletzte an einer Sammelstelle zusammenführen, sichten, Kennzeichnung (Anhängekarte), NEF-Fahrer für Funk und Dokumentation.",
  "Lage|erkund;Bereitstellungsraum;Patientenablage;Sammelstelle;sichten|Sichtung;Anhängekarte|Kennzeichnung;Funk|Dokumentation", 5)
Q(M, "MANV: Bei wem meldest du dich beim Eintreffen?", "Bei der Einsatzleitung (Feuerwehr).", "Einsatzleitung|Feuerwehr|Einsatzleiter")
Q(M, "MANV: Wann betrittst du den Gefahrenbereich?", "Erst nach Freigabe durch Feuerwehr oder Polizei.", "Freigabe;Feuerwehr|Polizei", 1)
Q(M, "MANV: Welche Aufgaben bekommt dein NEF-Fahrer?", "Funk und Dokumentation.", "Funk;Dokumentation")
Q(M, "mSTaRT Schritt 1: Patient ist gehfähig – Kategorie und wohin?", "Grün (SK III), zur Sammelstelle.", "grün|SK III|SK 3;Sammelstelle", 1)
Q(M, "mSTaRT: Starke, spritzende Blutung – Kategorie und Maßnahme?", "Rot, sofort Tourniquet oder Druck.", "rot|SK I;Tourniquet|Druck")
Q(M, "mSTaRT: Keine Atmung – was tust du, und was folgt?", "Atemweg freimachen. Weiter keine Atmung → schwarz (tot). Atmung danach → rot, Seitenlage.",
  "Atemweg|freimachen;schwarz|tot;rot;Seitenlage", 3)
Q(M, "mSTaRT: Ab welcher Atemfrequenz rot?", "AF > 30/min.", "30")
Q(M, "mSTaRT: Kreislaufkriterium für rot?", "Radialispuls nicht tastbar oder Rekap > 2 s.", "Radial;2 s|2|Rekap", 2)
Q(M, "mSTaRT: Patient befolgt einfache Aufforderungen nicht – Kategorie?", "Rot.", "rot|SK I")
Q(M, "mSTaRT: Nicht gehfähig, aber alle weiteren Kriterien unauffällig – Kategorie?", "Gelb (SK II).", "gelb|SK II|SK 2")
Q(M, "mSTaRT: Welche Sofortmaßnahmen sind während der Sichtung erlaubt?", "Atemweg freimachen, Blutung stillen, Seitenlage.", "Atemweg;Blutung;Seitenlage")
Q(M, "mSTaRT: Bei wem greift Schritt 1 (gehfähig) nicht?", "Bei Menschen, die schon vorher nicht gehen konnten (Rollstuhl).", "Rollstuhl|vorher|gehbehindert")
Q(M, "Sichtungskategorie SK I: Farbe und Bedeutung?", "Rot – akute vitale Bedrohung, Sofortbehandlung.", "rot;vital|Sofort")
Q(M, "Sichtungskategorie SK II: Farbe und Bedeutung?", "Gelb – schwer verletzt, aufgeschobene Behandlung.", "gelb;schwer|aufgeschoben|dringlich")
Q(M, "Sichtungskategorie SK III: Farbe und Bedeutung?", "Grün – leicht verletzt, spätere Behandlung.", "grün;leicht|später")
Q(M, "Sichtungskategorie SK IV: Farbe und Bedeutung?", "Blau – ohne Überlebenschance, betreuende Behandlung.", "blau;Überlebens|betreu|palliativ")
Q(M, "Sichtung: Was bedeutet „ex“ bzw. schwarz?", "Tot.", "tot|verstorben")
Q(M, "MANV: Blau und Schwarz – Unterschied?", "Blau (SK IV) = ohne Überlebenschance, betreuende Behandlung; Schwarz = tot.", "blau|SK IV;Überlebens|betreu;schwarz;tot")
Q(M, "MANV: Welche Westenfarbe hat meist der Einsatzleiter, welche die Einsatzleitung Rettungsdienst (LNA, OrgL)?", "Einsatzleiter meist gelb, Einsatzleitung Rettungsdienst (LNA, OrgL) meist weiß (regional unterschiedlich, z. B. Brandenburg blau).",
  "gelb;weiß")

# ───────────────────────── Organisation Rettungsdienst NRW ─────────────────────────
O = "Organisation NRW"
Q(O, "Rettungsdienstgesetze: Wessen Sache und wie viele?", "Landessache, 16 Gesetze (in NRW das RettG NRW).", "Land|Länder;16")
Q(O, "Wie heißt das Rettungsdienstgesetz in NRW?", "RettG NRW.", "RettG|Rettungsgesetz")
Q(O, "Wer ist Träger des Rettungsdienstes in NRW?", "Kreise und kreisfreie Städte.", "Kreis;kreisfrei|Städte")
Q(O, "Hilfsfrist: Wo festgelegt, und wofür dient sie?", "Im Bedarfsplan des Trägers; dient der Bedarfsplanung und der Vorhaltung von Rettungsmitteln.",
  "Bedarfsplan;Vorhaltung|Rettungsmittel")
Q(O, "Welche Qualifikation befugt in NRW zum Notarztdienst?", "Zusatzweiterbildung Notfallmedizin oder (alt) Fachkunde Rettungsdienst.", "Zusatzweiterbildung|ZWB;Fachkunde")
Q(O, "Rendezvous-System: Was ist das, und welcher Vorteil?", "NEF und RTW fahren getrennt und treffen sich am Einsatzort; NEF ist schneller wieder frei.",
  "getrennt|separat;Einsatzort|treffen;frei|einsatzbereit|schneller", 2)
Q(O, "Aufgaben des ÄLRD?", "Medizinische Verantwortung, SOPs, Vorabdelegation an NotSan, Qualitätsmanagement.",
  "medizinisch|Verantwortung;SOP;Delegation|Vorabdelegation;Qualität", 3)
Q(O, "Betäubungsmittel: Wer trägt die Verantwortung, wie wird Verwurf dokumentiert?", "Der Notarzt; Verwurf dokumentiert nach dem Vier-Augen-Prinzip; nicht an Klinikpersonal übergeben.",
  "Notarzt;Vier Augen|4 Augen")
Q(O, "Betäubungsmittel: Darfst du BtM an Klinikpersonal übergeben?", "Nein.", "nein|nicht")
Q(O, "Medizingeräte auf dem NEF: Was ist vor der ersten Anwendung Pflicht?", "Einweisung nach Medizinprodukte-Betreiberverordnung (MPBetreibV).", "Einweisung;Medizinprodukte|MPBetreibV|Betreiber")
Q(O, "Einsatznachbesprechung: Wie?", "Strukturiert, zeitnah, Team und Belastung ansprechen, ggf. PSNV anbieten.", "strukturiert;zeitnah;Belastung|Team;PSNV", 3)

# ───────────────────────── Recht in NRW ─────────────────────────
L = "Recht NRW"
Q(L, "Rechtliche Kernfrage im Notfall?", "Ist der Patient einwilligungsfähig?", "einwilligungsfähig|Einwilligungsfähigkeit")
Q(L, "Was bedeutet Einwilligungsfähigkeit?", "Der Patient versteht Art, Bedeutung und Tragweite der Maßnahme und kann seinen Willen danach bestimmen.",
  "Art;Bedeutung;Tragweite;Wille", 3)
Q(L, "Einwilligungsfähigkeit – mit welchem Begriff nicht verwechseln?", "Geschäftsfähigkeit.", "Geschäftsfähig")
Q(L, "Was prüfst du zur Einwilligungsfähigkeit?", "Orientierung, GCS, Blutzucker, Intoxikation, zerebrale Minderperfusion.",
  "Orientierung|orientiert;GCS;Blutzucker|BZ;Intox;Perfusion|Minderperfusion", 4)
Q(L, "Einwilligungsfähiger Patient willigt ein: Rechtsgrundlage?", "Einwilligung (§ 630d BGB) nach Aufklärung (§ 630e BGB).", "630d;630e")
Q(L, "Einwilligungsfähiger Patient lehnt ab: Rechtsgrundlage?", "Selbstbestimmungsrecht (Art. 2 GG), „Recht auf Unvernunft“.", "Selbstbestimmung|Art 2|GG;Unvernunft", 1)
Q(L, "Einwilligungsfähiger Patient lehnt ab: Vorgehen?", "Konkret aufklären, Kompromisse anbieten, dokumentieren, nicht zwingen (sonst § 223 StGB).",
  "aufklären|Aufklärung;Kompromiss;dokument;nicht zwingen|zwingen|223", 3)
Q(L, "Nicht einwilligungsfähiger Patient im Notfall: Rechtsgrundlage und Vorgehen?", "Mutmaßliche Einwilligung, notfalls rechtfertigender Notstand (§ 34 StGB); behandeln und transportieren.",
  "mutmaßlich;34|Notstand;behandeln|transportieren", 2)
Q(L, "Nicht einwilligungsfähig, Bevollmächtigter/Betreuer da: Rechtsgrundlage und wer entscheidet?", "Vorsorgevollmacht (§ 1820 BGB) / Betreuung; der Vertreter entscheidet nach dem Willen des Patienten.",
  "1820|Vorsorgevollmacht|Betreu;Vertreter|Bevollmächtigte|Betreuer;Wille", 2)
Q(L, "Patientenverfügung trifft auf die Situation zu: Paragraf und Bindung?", "§ 1827 BGB – bindend, auch für den Notarzt.", "1827;bindend|verbindlich")
Q(L, "PsychKG NRW: Voraussetzungen?", "Psychische Erkrankung oder Sucht mit akuter erheblicher Selbst- oder Fremdgefährdung.",
  "psychisch|Sucht;Gefährdung|gefährdet|Selbstgefährdung|Fremdgefährdung")
Q(L, "PsychKG NRW: Ablauf?", "Ärztliches Zeugnis, Anordnung durch die örtliche Ordnungsbehörde, Polizei unterstützt, Gericht entscheidet spätestens bis zum Ende des folgenden Tages.",
  "Zeugnis|Attest;Ordnungsbehörde|Ordnungsamt;Polizei;Gericht|Richter;folgenden|nächsten", 4)
Q(L, "PsychKG: Bis wann muss das Gericht entscheiden?", "Spätestens bis zum Ende des folgenden Tages.", "folgend|nächst|Ende")
Q(L, "Bewusstseinsstörung durch Hypoglykämie, Bradykardie oder Intox: PsychKG?", "Nein – PsychKG nur bei psychischer Ursache; hier mutmaßliche Einwilligung.", "mutmaßlich|nein")
Q(L, "Ab wann gilt die Vorsorgevollmacht?", "Erst wenn der Patient selbst nicht mehr einwilligungsfähig ist.", "nicht mehr einwilligungsfähig|einwilligungsunfähig|nicht einwilligungsfähig")
Q(L, "Seit wann gibt es keine „Entmündigung“ mehr?", "Seit 1992.", "1992")
Q(L, "Transportverweigerung: Was dokumentierst du?", "Befunde zur Einwilligungsfähigkeit, Vitalwerte, EKG, Inhalt der Aufklärung mit konkret genannten Risiken bis zum Tod, angebotene Alternativen, Zeugen mit Namen, Unterschrift (bzw. Verweigerung), Hinweis auf erneuten Notruf.",
  "Einwilligungsfähig;Vital;EKG;Aufklärung|Risiken;Tod;Alternativ;Zeugen;Unterschrift;Notruf", 6)
Q(L, "Transportverweigerung: Ist die Unterschrift des Patienten Pflicht?", "Nein – Verweigerung der Unterschrift ebenfalls dokumentieren.", "nein|nicht")
Q(L, "Garantenstellung: Paragraf und Bedeutung?", "§ 13 StGB – der Notarzt ist für den Patienten verantwortlich, Unterlassen kann strafbar sein.", "13;Unterlassen|verantwortlich", 1)
Q(L, "§ 323c StGB?", "Unterlassene Hilfeleistung.", "unterlassene Hilfeleistung|unterlassen")
Q(L, "Unterlassene Hilfeleistung: Paragraf?", "§ 323c StGB.", "323 c|323c|323")
Q(L, "§ 222 und § 229 StGB?", "Fahrlässige Tötung / fahrlässige Körperverletzung (z. B. nach mangelhafter Aufklärung).", "fahrlässig;Tötung;Körperverletzung")
Q(L, "§ 223 StGB?", "Körperverletzung – auch eine Behandlung gegen den Willen eines Einwilligungsfähigen.", "Körperverletzung")
Q(L, "Behandlung gegen den Willen eines Einwilligungsfähigen: Welcher Straftatbestand?", "Körperverletzung (§ 223 StGB).", "Körperverletzung|223")
Q(L, "§ 203 StGB?", "Schweigepflicht – auch gegenüber der Polizei (außer z. B. rechtfertigender Notstand).", "Schweigepflicht")
Q(L, "Gilt die Schweigepflicht auch gegenüber der Polizei?", "Ja (§ 203 StGB), außer z. B. bei rechtfertigendem Notstand.", "ja")
Q(L, "Sichere Todeszeichen?", "Totenflecke, Totenstarre, Fäulnis, mit dem Leben nicht vereinbare Verletzung.",
  "Totenfleck|Livor;Totenstarre|Rigor;Fäulnis|Verwesung;Verletzung", 3)
Q(L, "Muss der Notarzt im Einsatz die vollständige Leichenschau/Todesbescheinigung machen?", "Nein (laut Münster-Protokoll), damit er schnell wieder einsatzbereit ist; auch die Polizei kann ihn nicht dazu zwingen.",
  "nein|nicht")
Q(L, "Nicht natürlicher oder ungeklärter Tod: Vorgehen?", "Polizei informieren, Leichnam nicht verändern.", "Polizei;verändern|nicht bewegen|Spuren")
Q(L, "Klinik ist abgemeldet (IG NRW): Gilt das für vital bedrohte Patienten?", "Nein.", "nein|nicht")
Q(L, "Vital bedrohter Patient, Klinik abgemeldet: Vorgehen?", "Über die Leitstelle mit Arzt-zu-Arzt-Voranmeldung ins nächstgeeignete Krankenhaus.",
  "Leitstelle;Arzt zu Arzt|Voranmeldung;nächstgeeignet|geeignet", 2)
Q(L, "Klinik öffnet trotz vital bedrohtem Patienten nicht: Was tust du?", "Du bleibst Garant, Polizei (Amtshilfe) hinzuziehen, alles dokumentieren.",
  "Garant;Polizei|Amtshilfe;dokument", 2)
Q(L, "Kindeswohlgefährdung: Nach welchem Gesetz dürfen Ärzte das Jugendamt informieren?", "§ 4 KKG.", "KKG")

if __name__ == "__main__":
    # stabile IDs aus Fragetext
    def h(s):
        x = 5381
        for c in s.encode("utf-8"):
            x = ((x * 33) ^ c) & 0xFFFFFFFF
        return format(x, "08x")
    ids = set()
    for d in QS:
        d["id"] = h(d["t"] + "|" + d["q"])
        assert d["id"] not in ids, d["q"]
        ids.add(d["id"])
        if "m" in d:
            assert 1 <= d["m"] <= len(d["k"]), d["q"]
    out = sys.argv[1] if len(sys.argv) > 1 else "app/src/main/assets/www/questions.js"
    with open(out, "w", encoding="utf-8") as f:
        f.write("window.QUESTIONS=" + json.dumps(QS, ensure_ascii=False) + ";\n")
    from collections import Counter
    print(len(QS), Counter(d["t"] for d in QS))
