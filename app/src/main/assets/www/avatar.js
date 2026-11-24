// NotarztDrill – Avatar, der mit dem Fortschritt aufsteigt
(function () {
  "use strict";
  var LEVELS = [
    { min: 0, name: "Famulus", txt: "Noch ohne Ausrüstung – nervös, aber motiviert." },
    { min: 10, name: "Assistenzarzt", txt: "Kittel und Stethoskop sind da." },
    { min: 25, name: "Notarzt", txt: "Einsatzjacke mit Reflexstreifen." },
    { min: 45, name: "Notarzt mit Helm", txt: "Bereit für die Einsatzstelle." },
    { min: 65, name: "Leitender Notarzt", txt: "Weste, Funkgerät, alles im Griff." },
    { min: 85, name: "Notfall-Legende", txt: "Sonnenbrille auf. Nichts kann dich mehr schocken." },
    { min: 100, name: "Notarzt-Gott", txt: "Alles grün. Mehr geht nicht." }
  ];

  function levelFor(pct) {
    var l = 0;
    for (var i = 0; i < LEVELS.length; i++) if (pct >= LEVELS[i].min) l = i;
    return l;
  }

  var SKIN = "#f1c27d", SKIN_D = "#d9a35f", HAIR = "#3b2a1e", INK = "#22223b";

  function svg(level) {
    var p = [];
    var bg = ["#e7eaef", "#e0efff", "#fde2e4", "#fde2e4", "#fff3cd", "#ffe8a3", "#ffd60a"][level];
    p.push('<circle cx="50" cy="50" r="50" fill="' + bg + '"/>');
    if (level >= 6) {
      p.push('<g stroke="#fff" stroke-width="3" opacity=".7">' +
        [0, 45, 90, 135, 180, 225, 270, 315].map(function (a) {
          var r = a * Math.PI / 180;
          return '<line x1="' + (50 + Math.cos(r) * 36) + '" y1="' + (50 + Math.sin(r) * 36) + '" x2="' + (50 + Math.cos(r) * 48) + '" y2="' + (50 + Math.sin(r) * 48) + '"/>';
        }).join("") + "</g>");
    }
    // Körper / Kleidung
    var body = "M14 100c0-22 14-34 36-34s36 12 36 34z";
    if (level === 0) {
      p.push('<path d="' + body + '" fill="#9aa5b1"/>');
      p.push('<path d="M42 67l8 8 8-8" fill="none" stroke="#7d8896" stroke-width="3"/>');
    } else if (level === 1) {
      p.push('<path d="' + body + '" fill="#ffffff" stroke="#c9ccd1" stroke-width="2"/>');
      p.push('<path d="M42 67l8 30 8-30z" fill="#93c5fd"/>');
      p.push('<path d="M38 70c0 14 6 18 12 18M62 70c0 10-2 14-6 16" fill="none" stroke="' + INK + '" stroke-width="2.5"/><circle cx="56" cy="88" r="3.5" fill="#9aa5b1"/>');
    } else {
      var jacket = "#e63946";
      p.push('<path d="' + body + '" fill="' + jacket + '"/>');
      p.push('<rect x="16" y="86" width="68" height="5" fill="#e7eaef" opacity=".95"/>');
      p.push('<path d="M50 68v32" stroke="#a4161a" stroke-width="2"/>');
      if (level >= 4) {
        p.push('<path d="M24 78c4-8 12-12 18-12l8 34H26z M76 78c-4-8-12-12-18-12l-8 34h24z" fill="#ffd60a"/>');
        p.push('<rect x="28" y="84" width="16" height="4" fill="#fff"/><rect x="56" y="84" width="16" height="4" fill="#fff"/>');
        p.push('<rect x="64" y="70" width="8" height="14" rx="2" fill="' + INK + '"/><rect x="66" y="64" width="2" height="7" fill="' + INK + '"/>');
      }
      if (level >= 5) {
        p.push('<path d="M38 70c4 10 20 10 24 0" fill="none" stroke="#e9b200" stroke-width="3"/><circle cx="50" cy="78" r="3" fill="#ffd60a" stroke="#c99700"/>');
      }
    }
    // Hals + Kopf
    p.push('<rect x="44" y="56" width="12" height="12" rx="4" fill="' + SKIN_D + '"/>');
    p.push('<ellipse cx="31" cy="42" rx="4" ry="6" fill="' + SKIN_D + '"/><ellipse cx="69" cy="42" rx="4" ry="6" fill="' + SKIN_D + '"/>');
    p.push('<circle cx="50" cy="40" r="19" fill="' + SKIN + '"/>');
    // Haare oder Helm
    if (level < 3) {
      if (level === 0) p.push('<path d="M31 38c-2-14 8-22 20-22 12 0 20 8 18 22-3-6-6-9-9-10-2 4-8 6-14 4-4-2-8 0-15 6z" fill="' + HAIR + '"/><path d="M46 16l-3-6M52 16l2-7M58 18l5-5" stroke="' + HAIR + '" stroke-width="3"/>');
      else p.push('<path d="M31 38c-2-14 8-22 20-22 12 0 20 8 18 22-4-8-10-10-18-10s-14 2-20 10z" fill="' + HAIR + '"/>');
    } else {
      p.push('<path d="M28 38c0-14 10-24 22-24s22 10 22 24z" fill="#ffffff" stroke="#c9ccd1" stroke-width="2"/>');
      p.push('<rect x="26" y="36" width="48" height="5" rx="2.5" fill="#d9dde3"/>');
      p.push('<path d="M47 20h6v5h5v6h-5v5h-6v-5h-5v-6h5z" fill="#e63946"/>');
    }
    // Gesicht
    if (level >= 5) {
      p.push('<path d="M33 40h34v3c0 6-4 9-9 9s-7-3-8-6c-1 3-3 6-8 6s-9-3-9-9z" fill="' + INK + '"/><path d="M37 42l6 0" stroke="#5c677d" stroke-width="2"/><path d="M55 42l6 0" stroke="#5c677d" stroke-width="2"/>');
      p.push('<path d="M42 51c4 4 12 4 18-1" stroke="' + INK + '" stroke-width="2.5" fill="none" stroke-linecap="round"/>');
    } else {
      p.push('<circle cx="43" cy="42" r="2.6" fill="' + INK + '"/><circle cx="57" cy="42" r="2.6" fill="' + INK + '"/>');
      if (level === 0) {
        p.push('<path d="M38 37l7-3M62 37l-7-3" stroke="' + INK + '" stroke-width="2" stroke-linecap="round"/>');
        p.push('<path d="M43 51c2-2 4 2 6 0s4 2 6 0 4 2 4 0" stroke="' + INK + '" stroke-width="2" fill="none"/>');
        p.push('<path d="M67 28c-3 4-3 6 0 7 3-1 3-3 0-7z" fill="#7dd3fc"/>');
      } else if (level <= 2) {
        p.push('<path d="M43 50c4 3 10 3 14 0" stroke="' + INK + '" stroke-width="2.5" fill="none" stroke-linecap="round"/>');
      } else {
        p.push('<path d="M42 49c4 5 12 5 16 0z" fill="' + INK + '"/><path d="M44 49h12" stroke="#fff" stroke-width="2"/>');
      }
    }
    if (level >= 5) p.push('<path d="M80 16l2 5 5 2-5 2-2 5-2-5-5-2 5-2z" fill="#fff"/><path d="M20 22l1.5 3.5 3.5 1.5-3.5 1.5-1.5 3.5-1.5-3.5-3.5-1.5 3.5-1.5z" fill="#fff"/>');
    return '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><defs><clipPath id="avc' + level + '"><circle cx="50" cy="50" r="50"/></clipPath></defs><g clip-path="url(#avc' + level + ')">' + p.join("") + "</g></svg>";
  }

  window.Avatar = { LEVELS: LEVELS, levelFor: levelFor, svg: svg };
})();
