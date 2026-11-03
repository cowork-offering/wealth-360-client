/* ============================================================
   THE GATE, IN THE PRODUCT'S LANGUAGE.

   Loaded synchronously in <head>. If the visitor holds no valid unlock the
   page is hidden from first paint (no flash) and the Cowork greeting stands
   alone on the cream: "Morning.", the composer, the chevron.

   Wrong phrase: the composer moves 2 px, once, and says "Not on the list."
   Right phrase: the composer types itself out to the film's own prompt,
   sends, and the connector rows resolve one by one. Then the door hands the
   page its mark: see THE HANDOFF at the bottom of this file.

   Client-side only. This is a courtesy lock for an invited audience, not a
   security boundary: GitHub Pages serves static files and anyone with the
   bundle can read this script. The phrase itself is never in the repo, only
   the salted SHA-256 of it. Access is remembered on this device for 30 days.
   Append ?lock to any URL to re-lock (booth reset), or call c360Gate.lock().
   ============================================================ */
(function () {
  'use strict';
  var KEY = 'w360c.gate.v1';
  var SALT = 'w360-client:';
  var HASH = 'ceecd9a8875f919d66605e80d3839806012a199d60236d1e97134e75d2017897';
  var TTL = 30 * 24 * 3600 * 1000;
  var PROMPT = 'Open Credit 360 for my book';
  var root = document.documentElement;
  var RM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function lock() {
    try { localStorage.removeItem(KEY); } catch (e) {}
    location.href = location.pathname;
  }
  function unlocked() {
    try {
      var v = JSON.parse(localStorage.getItem(KEY) || 'null');
      return !!(v && v.h === HASH && v.t > Date.now());
    } catch (e) { return false; }
  }
  try { if (/[?&]lock(=|&|$)/.test(location.search)) { localStorage.removeItem(KEY); } } catch (e) {}

  var waiters = [];
  var api = {
    locked: !unlocked(),
    lock: lock,
    whenOpen: function (fn) { if (api.locked) { waiters.push(fn); } else { fn(); } }
  };
  window.c360Gate = api;
  if (!api.locked) { return; }

  /* hide the page from first paint, before any of it can render */
  root.classList.add('locked');

  /* SHA-256: WebCrypto where it exists, a pure-JS fallback for file:// previews */
  function sha256js(str) {
    var K = [0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
    var H = [0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19];
    var b = unescape(encodeURIComponent(str)), l = b.length, w = [], i;
    for (i = 0; i < l; i++) { w[i >> 2] |= b.charCodeAt(i) << (24 - (i % 4) * 8); }
    w[l >> 2] |= 0x80 << (24 - (l % 4) * 8);
    w[((l + 8 >> 6) << 4) + 15] = l * 8;
    var W = new Array(64), r = function (x, n) { return (x >>> n) | (x << (32 - n)); };
    for (var j = 0; j < w.length; j += 16) {
      var a = H[0], bb = H[1], c = H[2], d = H[3], e = H[4], f = H[5], g = H[6], h = H[7];
      for (var t = 0; t < 64; t++) {
        W[t] = t < 16 ? (w[j + t] | 0) : ((r(W[t-2],17) ^ r(W[t-2],19) ^ (W[t-2] >>> 10)) + W[t-7] + (r(W[t-15],7) ^ r(W[t-15],18) ^ (W[t-15] >>> 3)) + W[t-16]) | 0;
        var T1 = (h + (r(e,6) ^ r(e,11) ^ r(e,25)) + ((e & f) ^ (~e & g)) + K[t] + W[t]) | 0;
        var T2 = ((r(a,2) ^ r(a,13) ^ r(a,22)) + ((a & bb) ^ (a & c) ^ (bb & c))) | 0;
        h = g; g = f; f = e; e = (d + T1) | 0; d = c; c = bb; bb = a; a = (T1 + T2) | 0;
      }
      H[0]=(H[0]+a)|0; H[1]=(H[1]+bb)|0; H[2]=(H[2]+c)|0; H[3]=(H[3]+d)|0;
      H[4]=(H[4]+e)|0; H[5]=(H[5]+f)|0; H[6]=(H[6]+g)|0; H[7]=(H[7]+h)|0;
    }
    return H.map(function (x) { return ('00000000' + (x >>> 0).toString(16)).slice(-8); }).join('');
  }
  function digest(str) {
    if (window.crypto && crypto.subtle && window.TextEncoder) {
      return crypto.subtle.digest('SHA-256', new TextEncoder().encode(str)).then(function (buf) {
        return Array.prototype.map.call(new Uint8Array(buf), function (x) { return ('0' + x.toString(16)).slice(-2); }).join('');
      }).catch(function () { return sha256js(str); });
    }
    return Promise.resolve(sha256js(str));
  }

  function mount() {
    var gate = document.getElementById('gate');
    if (!gate) { root.classList.remove('locked'); api.locked = false; return; }
    gate.hidden = false;

    var form = document.getElementById('g-form');
    var input = document.getElementById('g-input');
    var send = document.getElementById('g-send');
    var msg = document.getElementById('g-msg');
    var hint = document.getElementById('g-hint');
    var typed = document.getElementById('g-typed');
    var typedT = document.getElementById('g-typed-t');
    var composer = gate.querySelector('.composer');
    var rows = Array.prototype.slice.call(document.querySelectorAll('#g-rows .runrow'));

    setTimeout(function () { try { input.focus({ preventScroll: true }); } catch (e) {} }, RM ? 30 : 260);
    input.addEventListener('input', function () { msg.textContent = ''; });

    var busy = false;
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      if (busy) { return; }
      var v = input.value.trim();
      if (!v) { input.focus(); return; }
      busy = true;
      digest(SALT + v.toLowerCase()).then(function (h) {
        if (h === HASH) { open(); return; }
        busy = false;
        msg.textContent = 'Not on the list.';
        composer.classList.remove('shake'); void composer.offsetWidth; composer.classList.add('shake');
        input.select();
      });
    });

    /* the door sequence, as live HTML: the mark strikes, the prompt types, it
       sends, the rows resolve, and then the door hands the mark to the hero */
    function open() {
      try { localStorage.setItem(KEY, JSON.stringify({ h: HASH, t: Date.now() + TTL })); } catch (e) {}
      input.blur();
      input.hidden = true;
      typed.hidden = false;
      hint.textContent = 'Opening your book';
      msg.textContent = '';

      /* two frames to full purple: the endcard's own strike, not a fade */
      gate.classList.add('striking');

      /* the visitor is through, so the hero's own plate may start loading. It
         has to be RUNNING by the time the opening puts it on the screen, and
         the run is four and a half seconds of head start. */
      window.dispatchEvent(new CustomEvent('gate:accepted'));

      if (RM) { typedT.textContent = PROMPT; run(); return; }

      /* THE PANE STAYS. It used to leave the frame on frame 8, sliding out
         while the composer glided to the centre of the paper, which spent the
         mark before the run it was waiting on had even started. It stands
         through the whole run now and veils to cream at the end, so the mark
         is still on the screen when there is somewhere for it to go. */
      setTimeout(type, 560);
    }

    function type() {
      var i = 0;
      /* 24 characters a second, the film's own rate and the page's only one */
      var tick = setInterval(function () {
        typedT.textContent = PROMPT.slice(0, ++i);
        if (i >= PROMPT.length) {
          clearInterval(tick);
          setTimeout(function () {
            send.classList.add('fire');
            /* the rows fade in over .3s, which IS the hold: see HOLD below */
            gate.classList.add('running');
            run();
          }, 180);
        }
      }, 42);
    }

    /* THE HOLDS OF THE RUN.

       The run used to start 140 ms after the send and resolve a row every
       100 ms, so all six were ticked inside 640 ms: the eye had not registered
       that anything was loading before the loading was over. Every row was a
       tick that had never visibly been a spinner. The same gesture is spent
       where it can be read instead.

         HOLD  the beat between the send and the rows standing on the paper.
               The rows fade in over exactly this (.3s on #gate.running), so
               the hold is motion rather than a gap in it.
         SPIN  how long the first row stands as a spinner before it ticks, so
               no row is ever a tick that was never a loader. Every row after
               it spins for this plus its own place in the queue.
         STEP  one row resolving to the next.
         TAIL  the beat after the last tick, before the page continues.

       Nothing here is longer than 500 ms, so the unlock is still ONE motion
       and never a pause: 300 to the rows, 350 to the first tick, 320 between
       ticks, 500 to the page. From the send that is 2750 ms.

       Under reduce there are no holds at all: the six are resolved on the
       spot and the page continues, exactly as before. */
    var HOLD = 300, SPIN = 350, STEP = 320, TAIL = 500;

    function run() {
      /* the rows resolve top to bottom, exactly as shot 11 cuts them */
      if (RM) {
        rows.forEach(function (row) { row.classList.add('done'); });
        setTimeout(release, 60);
        return;
      }
      rows.forEach(function (row, n) {
        setTimeout(function () { row.classList.add('done'); }, HOLD + SPIN + n * STEP);
      });
      setTimeout(release, HOLD + SPIN + (rows.length - 1) * STEP + TAIL);
    }

    /* THE HANDOFF.

       The door used to end by cutting itself away: the page was unhidden, the
       gate cross-faded out over 340 ms and the hero was simply there, finished,
       with its mark already struck. The one thing the visitor had been looking
       at for five seconds, the chevron standing on the pane, went out with the
       gate and a second copy of it appeared in the lockup.

       It is one mark now, and it is handed over rather than replaced. The page
       is unhidden BEHIND the gate, which is still standing and still cream, and
       the opening is then offered to whoever owns the hero. Taking the offer
       (preventDefault) makes that listener the owner of the gate element from
       here, including removing it. If nobody takes it, if the visitor has asked
       for less motion, or if the hero is not on the screen to fly to, the door
       cross-fades exactly as it always did. */
    function release() {
      api.locked = false;
      root.classList.remove('locked');
      var taken = false;
      if (!RM) {
        taken = !window.dispatchEvent(new CustomEvent('gate:opening', {
          cancelable: true,
          detail: { gate: gate, mark: gate.querySelector('.gmark-c') }
        }));
      }
      window.dispatchEvent(new CustomEvent('gate:unlocked'));
      var w = waiters.splice(0);
      for (var i = 0; i < w.length; i++) { try { w[i](); } catch (e) {} }
      if (taken) { return; }
      gate.classList.add('gone');
      setTimeout(function () { gate.remove(); }, RM ? 200 : 420);
    }
  }

  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', mount); }
  else { mount(); }
})();
