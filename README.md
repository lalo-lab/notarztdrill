# NotarztDrill

Android-Lern-App (Deutsch) für die ZWB Notfallmedizin (ÄKWL Münster): Dosen, Indikationen, Abkürzungen, Trauma, Reanimation, Atemweg, Pädiatrie, MANV, Organisation und Recht – 305 offene Fragen mit sofortiger, toleranter Bewertung und Spaced Repetition.

## APK herunterladen

Jeder Push auf `main` baut automatisch eine neue APK (GitHub Actions) und veröffentlicht sie unter **Releases**:

`https://github.com/<benutzer>/<repo>/releases/latest/download/NotarztDrill.apk`

Auf dem Handy öffnen, „Installation aus unbekannten Quellen“ für den Browser erlauben, installieren. Updates werden über die alte Version installiert – der Fortschritt bleibt erhalten (feste Signatur in `keystore/`).

## Aufbau

- `app/src/main/assets/www/` – die eigentliche App (HTML/JS, offline)
  - `questions.js` – Fragenkatalog (generiert)
  - `grader.js` – tolerante Bewertung (Schlüsselbegriffe, Tippfehler, Einheiten, Zahlenformate)
  - `app.js` – Abfrage, Spaced Repetition (Falsch → nach 4 Fragen + nächster Tag; Richtig → 1, 3, 7, 16, 35, 80, 180 Tage), Fortschrittsbalken
- `tools/questions.py` – Quelle des Fragenkatalogs. Nach Änderungen:
  `python3 tools/questions.py app/src/main/assets/www/questions.js && node tools/test_grader.js`
- `app/src/main/java/.../MainActivity.java` – WebView-Hülle

Fortschritt wird lokal auf dem Gerät gespeichert; Sicherung/Wiederherstellung über das Menü (☰).

Inhalt: Lernskript ZWB Notfallmedizin – ÄKWL Münster. Dosen immer mit der SOP des eigenen Rettungsdienstbereichs abgleichen.
