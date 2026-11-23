// NotarztDrill – tolerante Antwortbewertung
(function (root) {
  "use strict";

  function canonNum(tok) {
    if (/^\d+(\.\d+)?(-\d+(\.\d+)?)?$/.test(tok)) {
      return tok.split("-").map(function (p) { return String(parseFloat(p)); }).join("-");
    }
    return tok;
  }

  function normalize(s) {
    s = String(s || "").toLowerCase();
    s = s.replace(/[₀-₉]/g, function (d) { return String.fromCharCode(d.charCodeAt(0) - 0x2080 + 48); });
    s = s.replace(/ä/g, "ae").replace(/ö/g, "oe").replace(/ü/g, "ue").replace(/ß/g, "ss");
    s = s.normalize("NFD").replace(/[̀-ͯ]/g, "");
    // Einheiten und Synonyme
    s = s.replace(/[µμ]\s?g/g, "ug").replace(/\bmcg\b/g, "ug");
    s = s.replace(/mikrogramm\w*/g, "ug").replace(/milligramm\w*/g, "mg").replace(/\bgramm\b/g, "g");
    s = s.replace(/milliliter\w*/g, "ml").replace(/\bjoule\b/g, "j");
    s = s.replace(/\bminuten?\b/g, "min").replace(/\bsekunden?\b/g, "s").replace(/\bstunden?\b/g, "h");
    s = s.replace(/\bepinephrin\b/g, "adrenalin").replace(/\bsuprarenin\b/g, "adrenalin");
    s = s.replace(/\bnorepinephrin\b/g, "noradrenalin").replace(/\barterenol\b/g, "noradrenalin");
    // Applikationswege
    s = s.replace(/\bi\.\s?n\b\.?/g, " intranasal ");
    s = s.replace(/\bi\.\s?v\b\.?/g, " iv ").replace(/\bi\.\s?o\b\.?/g, " io ").replace(/\bi\.\s?m\b\.?/g, " im ");
    s = s.replace(/\bs\.\s?l\b\.?/g, " sl ").replace(/\bp\.\s?o\b\.?/g, " po ").replace(/\bs\.\s?c\b\.?/g, " sc ");
    // Zahlen
    s = s.replace(/\b([1-9]\d{0,2})\.(\d{3})\b/g, "$1$2");   // 4.500 -> 4500
    s = s.replace(/(\d),(\d)/g, "$1.$2");             // 0,5 -> 0.5
    s = s.replace(/[–—−]/g, "-");
    s = s.replace(/\bbis\b/g, "-");
    s = s.replace(/\bpro\b/g, " ");
    s = s.replace(/[×*]/g, " x ");
    s = s.replace(/(\d)([a-z])/g, "$1 $2").replace(/([a-z])(\d)/g, "$1 $2");
    s = s.replace(/\s*-\s*/g, "-");
    s = s.replace(/(\d)-(?=\d)/g, "$1~");
    s = s.replace(/-/g, " ").replace(/~/g, "-");
    s = s.replace(/\//g, " ");
    s = s.replace(/(\d)\.(?!\d)/g, "$1 ");
    s = s.replace(/[^a-z0-9.\- ]/g, " ");
    s = s.replace(/(^|[^\d])\.|\.(?!\d)/g, "$1 ");
    return s.split(/\s+/).filter(Boolean).map(canonNum);
  }

  function lev(a, b) {
    if (a === b) return 0;
    var m = a.length, n = b.length;
    if (!m) return n; if (!n) return m;
    var prev = new Array(n + 1), cur = new Array(n + 1), i, j;
    for (j = 0; j <= n; j++) prev[j] = j;
    for (i = 1; i <= m; i++) {
      cur[0] = i;
      for (j = 1; j <= n; j++) {
        cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
      }
      var t = prev; prev = cur; cur = t;
    }
    return prev[n];
  }

  function isNum(t) { return /\d/.test(t); }

  function tokenMatch(k, t) {
    if (k === t) return true;
    if (isNum(k) || isNum(t)) return false;
    var L = k.length;
    if (L <= 2) return false;
    if (L === 3) return t.length <= 5 && t.indexOf(k) === 0;
    if (t.indexOf(k) === 0) return true;
    if (L >= 5 && t.indexOf(k) >= 0) return true;
    var tol = L >= 8 ? 2 : (L >= 5 ? 1 : 0);
    if (tol === 0) return false;
    if (lev(k, t) <= tol) return true;
    if (t.length > L && lev(k, t.slice(0, L)) <= tol) return true;
    return false;
  }

  function altMatch(altToks, ansToks, ansCompact) {
    if (!altToks.length) return false;
    for (var i = 0; i + altToks.length <= ansToks.length; i++) {
      var ok = true;
      for (var j = 0; j < altToks.length; j++) {
        if (!tokenMatch(altToks[j], ansToks[i + j])) { ok = false; break; }
      }
      if (ok) return true;
    }
    var compact = altToks.join("");
    if (altToks.length > 1 && compact.length >= 5 && !/\d/.test(compact) && ansCompact.indexOf(compact) >= 0) return true;
    return false;
  }

  var cache = {};
  function normKey(s) { return cache[s] || (cache[s] = normalize(s)); }

  // q: {k:[[alt,...],...], m?}
  function grade(q, answer) {
    var toks = normalize(answer);
    var compact = toks.join("");
    var res = q.k.map(function (group) {
      var hit = group.some(function (alt) { return altMatch(normKey(alt), toks, compact); });
      return { label: group[0], hit: hit };
    });
    var hits = res.filter(function (r) { return r.hit; }).length;
    var need = q.m || q.k.length;
    return { ok: toks.length > 0 && hits >= need, hits: hits, need: need, total: q.k.length, groups: res };
  }

  var api = { normalize: normalize, grade: grade, lev: lev };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.Grader = api;
})(this);
