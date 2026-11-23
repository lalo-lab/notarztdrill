// NotarztDrill – App-Logik (Spaced Repetition, Abfrage, Fortschritt)
(function () {
  "use strict";
  var QS = window.QUESTIONS, G = window.Grader;
  var BY_ID = {}; QS.forEach(function (q) { BY_ID[q.id] = q; });
  var TOPICS = []; QS.forEach(function (q) { if (TOPICS.indexOf(q.t) < 0) TOPICS.push(q.t); });
  var KEY = "notarztdrill_v1";
  var DAY = 86400000;
  var LADDER = [1, 3, 7, 16, 35, 80, 180];
  var REQUEUE_GAP = 4;

  var $ = function (id) { return document.getElementById(id); };

  // ───────── Speicher ─────────
  function load() {
    var s = null;
    try { s = JSON.parse(localStorage.getItem(KEY)); } catch (e) { s = null; }
    if (!s || typeof s !== "object") s = {};
    s.cards = s.cards || {};
    s.order = s.order || [];
    s.counter = s.counter || 0;
    s.requeue = s.requeue || [];
    // Neue Fragen (z. B. nach Update) in zufälliger Reihenfolge anhängen
    var known = {}; s.order.forEach(function (id) { known[id] = 1; });
    var fresh = QS.map(function (q) { return q.id; }).filter(function (id) { return !known[id]; });
    shuffle(fresh);
    s.order = s.order.filter(function (id) { return BY_ID[id]; }).concat(fresh);
    s.requeue = s.requeue.filter(function (r) { return BY_ID[r.id]; });
    return s;
  }
  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) { toast("Speichern fehlgeschlagen"); }
  }
  function shuffle(a) {
    for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; }
    return a;
  }
  var S = load();

  // ───────── Spaced Repetition ─────────
  function startOfDay(t) { var d = new Date(t); d.setHours(0, 0, 0, 0); return d.getTime(); }
  function nextInterval(iv) {
    if (!iv) return 1;
    for (var i = 0; i < LADDER.length; i++) if (LADDER[i] > iv) return LADDER[i];
    return Math.round(iv * 2.2);
  }
  function isDue(c, now) { return c && c.n > 0 && c.due <= now; }

  function pickNext(lastId) {
    var now = Date.now();
    var rq = S.requeue.filter(function (r) { return r.after <= S.counter && r.id !== lastId; });
    if (rq.length) return { id: rq[0].id, kind: "rep" };
    var inRq = {}; S.requeue.forEach(function (r) { inRq[r.id] = 1; });
    var due = S.order.filter(function (id) { return isDue(S.cards[id], now) && id !== lastId && !inRq[id]; });
    if (due.length) {
      due.sort(function (a, b) {
        var A = S.cards[a], B = S.cards[b];
        var pa = A.last === "bad" ? 0 : 1, pb = B.last === "bad" ? 0 : 1;
        return pa - pb || A.due - B.due;
      });
      return { id: due[0], kind: "rep" };
    }
    for (var i = 0; i < S.order.length; i++) {
      var id = S.order[i];
      if (!S.cards[id] && id !== lastId) return { id: id, kind: "new" };
    }
    // Alles gelernt und nichts fällig: Wartende aus der Sitzung, sonst die nächsten Wiederholungen vorziehen
    var waiting = S.requeue.filter(function (r) { return r.id !== lastId; });
    if (waiting.length) return { id: waiting[0].id, kind: "rep" };
    var seen = S.order.filter(function (id) { return S.cards[id] && id !== lastId; });
    if (!seen.length) return lastId ? { id: lastId, kind: "rep" } : null;
    seen.sort(function (a, b) { return S.cards[a].due - S.cards[b].due; });
    return { id: seen[0], kind: "early" };
  }

  function applyAnswer(id, correct) {
    var now = Date.now();
    var c = S.cards[id] || { n: 0, ok: 0, lapses: 0, iv: 0, due: now, last: null };
    c.n += 1;
    S.requeue = S.requeue.filter(function (r) { return r.id !== id; });
    if (correct) {
      c.ok += 1;
      c.last = "ok";
      c.iv = nextInterval(c.iv);
      c.due = startOfDay(now) + c.iv * DAY;
    } else {
      c.lapses += 1;
      c.last = "bad";
      c.iv = 0;
      c.due = now;
      S.requeue.push({ id: id, after: S.counter + REQUEUE_GAP });
    }
    c.at = now;
    S.cards[id] = c;
  }

  // ───────── Zählung ─────────
  function counts(filterTopic) {
    var g = 0, r = 0, n = 0, due = 0, now = Date.now();
    QS.forEach(function (q) {
      if (filterTopic && q.t !== filterTopic) return;
      var c = S.cards[q.id];
      if (!c) n++; else if (c.last === "ok") g++; else r++;
      if (isDue(c, now)) due++;
    });
    return { g: g, r: r, n: n, due: due, total: g + r + n };
  }
  function paintBar(el, c) {
    var parts = el.querySelectorAll("i");
    parts[0].style.width = (100 * c.g / c.total) + "%";
    parts[1].style.width = (100 * c.r / c.total) + "%";
  }
  function renderHeader() {
    var c = counts();
    paintBar($("mainBar"), c);
    $("mainLegend").innerHTML =
      '<span><i class="dot" style="background:var(--ok)"></i><b>' + c.g + '</b> richtig</span>' +
      '<span><i class="dot" style="background:var(--bad)"></i><b>' + c.r + '</b> falsch</span>' +
      '<span><i class="dot" style="background:var(--gray)"></i><b>' + c.n + '</b> offen</span>' +
      '<span style="margin-left:auto">' + Math.round(100 * c.g / c.total) + ' %</span>';
  }

  // ───────── Ansichten ─────────
  var VIEWS = ["vHome", "vQuiz", "vMenu"];
  function show(v) {
    VIEWS.forEach(function (x) { $(x).classList.toggle("hidden", x !== v); });
    $("btnHome").classList.toggle("hidden", v === "vHome");
    $("btnMenu").classList.toggle("hidden", v === "vMenu");
    window.scrollTo(0, 0);
  }

  function renderHome() {
    var c = counts();
    var dueTotal = c.due;
    $("sDue").textContent = dueTotal;
    $("sNew").textContent = c.n;
    $("sOk").textContent = c.g;
    var started = c.g + c.r > 0;
    $("btnStart").textContent = started ? "Weiter lernen" : "Lernen";
    var t;
    if (dueTotal) t = dueTotal + " Wiederholung" + (dueTotal === 1 ? "" : "en") + " fällig – die kommen zuerst, danach neue Fragen.";
    else if (c.n) t = "Keine Wiederholung fällig. Weiter mit neuen Fragen (" + c.n + " offen).";
    else t = "Alle Fragen gesehen und nichts fällig. Du kannst Wiederholungen vorziehen.";
    $("heroText").textContent = t;
    var html = "";
    TOPICS.forEach(function (tp) {
      var k = counts(tp);
      html += '<div class="topic"><div class="name">' + esc(tp) + '</div>' +
        '<div class="bar"><i class="g" style="width:' + (100 * k.g / k.total) + '%"></i><i class="r" style="width:' + (100 * k.r / k.total) + '%"></i></div>' +
        '<div class="num">' + k.g + '/' + k.total + '</div></div>';
    });
    $("topics").innerHTML = html;
    renderHeader();
  }

  // ───────── Abfrage ─────────
  var cur = null;      // {id, kind}
  var lastId = null;
  var result = null;   // {ok, snapshot}
  var phase = "ask";

  function nextQuestion() {
    cur = pickNext(lastId);
    if (!cur) { location.hash = "#home"; return; }
    var q = BY_ID[cur.id];
    $("qTopic").textContent = q.t;
    var kind = $("qKind");
    kind.className = "chip " + (cur.kind === "new" ? "new" : "rep");
    kind.textContent = cur.kind === "new" ? "Neu" : (cur.kind === "early" ? "Vorgezogen" : "Wiederholung");
    $("qText").textContent = q.q;
    $("answer").value = "";
    $("askBox").classList.remove("hidden");
    $("resultBox").classList.add("hidden");
    phase = "ask";
    renderHeader();
    setTimeout(function () { $("answer").focus(); }, 30);
  }

  function snapshot(id) {
    return { card: S.cards[id] ? JSON.parse(JSON.stringify(S.cards[id])) : null, requeue: S.requeue.slice(), counter: S.counter };
  }
  function restore(id, snap) {
    if (snap.card) S.cards[id] = snap.card; else delete S.cards[id];
    S.requeue = snap.requeue;
    S.counter = snap.counter;
  }

  function check(skip) {
    if (phase !== "ask") return;
    var q = BY_ID[cur.id];
    var ans = skip ? "" : $("answer").value.trim();
    if (!skip && !ans) { $("answer").focus(); return; }
    var g = G.grade(q, ans);
    var snap = snapshot(cur.id);
    S.counter += 1;
    applyAnswer(cur.id, g.ok);
    save();
    result = { ok: g.ok, snap: snap, grade: g, ans: ans, skip: skip };
    phase = "result";
    lastId = cur.id;
    renderResult();
    renderHeader();
    $("answer").blur();
  }

  function renderResult() {
    var q = BY_ID[cur.id];
    var v = $("verdict");
    v.className = "verdict " + (result.ok ? "ok" : "bad");
    var info = result.skip ? "" : '<small>' + result.grade.hits + '/' + result.grade.total + ' Begriffe' + (result.grade.need < result.grade.total ? ' · ' + result.grade.need + ' nötig' : '') + '</small>';
    v.innerHTML = (result.ok ? "✓ Richtig" : "✗ Falsch") + (result.overridden ? ' <small>korrigiert</small>' : info);
    $("yoursWrap").classList.toggle("hidden", result.skip);
    $("yours").textContent = result.ans;
    $("keysWrap").classList.toggle("hidden", result.skip);
    $("keys").innerHTML = result.grade.groups.map(function (gr) {
      return '<span class="key ' + (gr.hit ? "hit" : "miss") + '">' + (gr.hit ? "✓ " : "✗ ") + esc(gr.label) + '</span>';
    }).join("");
    $("solution").textContent = q.a;
    var ob = $("btnOverride");
    if (result.skip) ob.classList.add("hidden");
    else {
      ob.classList.remove("hidden");
      ob.textContent = result.ok ? "Doch falsch" : "Ich hatte recht";
    }
    $("askBox").classList.add("hidden");
    $("resultBox").classList.remove("hidden");
    setTimeout(function () { $("btnNext").focus(); }, 30);
  }

  function override() {
    if (phase !== "result" || result.skip) return;
    restore(cur.id, result.snap);
    S.counter += 1;
    result.ok = !result.ok;
    result.overridden = true;
    applyAnswer(cur.id, result.ok);
    save();
    renderResult();
    renderHeader();
    toast(result.ok ? "Als richtig gewertet" : "Als falsch gewertet");
  }

  // ───────── Sichern / Wiederherstellen ─────────
  var ioMode = null;
  function openIO(mode) {
    ioMode = mode;
    $("ioBox").classList.remove("hidden");
    if (mode === "export") {
      $("ioLabel").textContent = "Dein Fortschritt (Text kopieren und z. B. in Notizen speichern)";
      $("ioText").value = btoa(unescape(encodeURIComponent(JSON.stringify({ app: "NotarztDrill", v: 1, s: S }))));
      $("ioBtn").textContent = "Kopieren";
    } else {
      $("ioLabel").textContent = "Gesicherten Text hier einfügen";
      $("ioText").value = "";
      $("ioBtn").textContent = "Wiederherstellen";
    }
  }
  function ioAction() {
    var ta = $("ioText");
    if (ioMode === "export") {
      ta.focus(); ta.select();
      var done = false;
      try { done = document.execCommand("copy"); } catch (e) { done = false; }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(ta.value).then(function () { toast("Kopiert"); }, function () { toast(done ? "Kopiert" : "Bitte manuell kopieren"); });
      } else toast(done ? "Kopiert" : "Bitte manuell kopieren");
    } else {
      try {
        var obj = JSON.parse(decodeURIComponent(escape(atob(ta.value.trim()))));
        if (!obj || obj.app !== "NotarztDrill" || !obj.s || !obj.s.cards) throw new Error("x");
        localStorage.setItem(KEY, JSON.stringify(obj.s));
        S = load(); save();
        toast("Fortschritt wiederhergestellt");
        location.hash = "#home";
      } catch (e) { toast("Text ungültig"); }
    }
  }

  // ───────── Hilfen ─────────
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  var toastT;
  function toast(msg) {
    var t = $("toast"); t.textContent = msg; t.classList.add("show");
    clearTimeout(toastT); toastT = setTimeout(function () { t.classList.remove("show"); }, 1800);
  }

  // ───────── Routing ─────────
  function route() {
    var h = location.hash || "#home";
    if (h === "#quiz") { show("vQuiz"); if (!cur || phase === "result") nextQuestion(); else renderHeader(); }
    else if (h === "#menu") { show("vMenu"); $("ioBox").classList.add("hidden"); renderHeader(); }
    else { show("vHome"); renderHome(); }
  }
  window.addEventListener("hashchange", route);

  // ───────── Events ─────────
  $("btnStart").onclick = function () { cur = null; location.hash = "#quiz"; };
  $("btnHome").onclick = function () { location.hash = "#home"; };
  $("btnMenu").onclick = function () { location.hash = "#menu"; };
  $("btnCheck").onclick = function () { check(false); };
  $("btnSkip").onclick = function () { check(true); };
  $("btnNext").onclick = function () { if (phase === "result") nextQuestion(); };
  $("btnOverride").onclick = override;
  $("answer").addEventListener("keydown", function (e) {
    if ((e.key === "Enter" || e.keyCode === 13) && !e.shiftKey) { e.preventDefault(); e.stopPropagation(); check(false); }
  });
  document.addEventListener("keydown", function (e) {
    if (phase === "result" && (e.key === "Enter" || e.keyCode === 13) && e.target !== $("answer") && e.target !== $("ioText") && location.hash === "#quiz") {
      e.preventDefault(); nextQuestion();
    }
  });
  $("mExport").onclick = function () { openIO("export"); };
  $("mImport").onclick = function () { openIO("import"); };
  $("ioBtn").onclick = ioAction;
  $("mReset").onclick = function () {
    if (window.confirm("Gesamten Fortschritt löschen? Das kann nicht rückgängig gemacht werden.")) {
      localStorage.removeItem(KEY); S = load(); save(); cur = null; lastId = null;
      toast("Zurückgesetzt"); location.hash = "#home";
    }
  };
  document.addEventListener("visibilitychange", function () { if (!document.hidden && location.hash !== "#quiz") route(); });

  save();
  route();
})();
