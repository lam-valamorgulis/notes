/* ============================================================
   quiz.js — reusable retrieval-practice widgets for the course.
   Two components, both self-styled (theme via base.css variables):

   1) renderQuiz(selector, questions)
        questions: [{ q, options:[...], answer:<index>, why }]
        Multiple choice with instant right/wrong feedback + score.

   2) renderRecall(selector, cards)
        cards: [{ prompt, answer }]
        "Say it out loud, THEN flip." Free-recall for spoken
        interview answers — the highest-value practice for this mission.
   ============================================================ */
(function () {
  var css = `
  .quiz, .recall { font-family: var(--font-sans); margin: 1.6rem 0; }
  .quiz-head, .recall-head { font-weight: 700; font-size: 1.05rem; margin-bottom: .4rem; color: var(--accent); }
  .quiz-sub { font-size: .85rem; color: var(--ink-faint); margin-bottom: 1rem; }
  .q { background: var(--card-bg); border-radius: 8px; padding: 1rem 1.1rem; margin-bottom: 1rem; }
  .q-text { font-weight: 600; margin-bottom: .7rem; }
  .opt {
    display: block; width: 100%; text-align: left; font: inherit; cursor: pointer;
    background: var(--paper); color: var(--ink); border: 1.5px solid var(--rule);
    border-radius: 6px; padding: .55rem .8rem; margin: .4rem 0; transition: all .12s;
  }
  .opt:hover:not(:disabled) { border-color: var(--accent); }
  .opt:disabled { cursor: default; opacity: .9; }
  .opt.correct { border-color: var(--good); background: color-mix(in srgb, var(--good) 14%, var(--paper)); font-weight: 600; }
  .opt.wrong   { border-color: var(--warn); background: color-mix(in srgb, var(--warn) 12%, var(--paper)); }
  .why {
    font-size: .88rem; line-height: 1.5; margin-top: .6rem; padding: .6rem .8rem;
    border-left: 3px solid var(--accent); background: var(--paper); border-radius: 0 5px 5px 0; display: none;
  }
  .why.show { display: block; }
  .score { font-weight: 700; margin-top: .5rem; color: var(--accent); }
  .card {
    background: var(--card-bg); border-radius: 8px; padding: 1rem 1.1rem; margin-bottom: .9rem;
    cursor: pointer; border: 1.5px solid var(--rule); transition: border-color .12s;
  }
  .card:hover { border-color: var(--accent-2); }
  .card .prompt { font-weight: 600; }
  .card .hint { font-size: .78rem; color: var(--ink-faint); margin-top: .35rem; }
  .card .ans { font-size: .92rem; line-height: 1.55; margin-top: .7rem; padding-top: .7rem; border-top: 1px dashed var(--rule); display: none; }
  .card.open .ans { display: block; }
  .card.open .hint { display: none; }
  `;
  var style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);

  window.renderQuiz = function (selector, questions) {
    var root = document.querySelector(selector);
    if (!root) return;
    var answered = 0, correct = 0, total = questions.length;
    var head = document.createElement('div'); head.className = 'quiz-head'; head.textContent = 'Check yourself';
    var sub = document.createElement('div'); sub.className = 'quiz-sub';
    sub.textContent = 'Answer from memory first. Feedback appears instantly.';
    var score = document.createElement('div'); score.className = 'score';
    root.classList.add('quiz'); root.appendChild(head); root.appendChild(sub);

    questions.forEach(function (item) {
      var q = document.createElement('div'); q.className = 'q';
      var qt = document.createElement('div'); qt.className = 'q-text'; qt.textContent = item.q; q.appendChild(qt);
      var why = document.createElement('div'); why.className = 'why'; why.textContent = item.why;
      var locked = false;
      // Shuffle options each render so the correct answer is never always in the same slot
      // (kills the "always A" tell and stops position-memorisation across repeat practice).
      var correctText = item.options[item.answer];
      var opts = item.options.slice();
      for (var s = opts.length - 1; s > 0; s--) {
        var r = Math.floor(Math.random() * (s + 1));
        var tmp = opts[s]; opts[s] = opts[r]; opts[r] = tmp;
      }
      var correctIdx = opts.indexOf(correctText);
      opts.forEach(function (opt, i) {
        var b = document.createElement('button'); b.className = 'opt'; b.textContent = opt;
        b.addEventListener('click', function () {
          if (locked) return; locked = true;
          answered++;
          Array.prototype.forEach.call(q.querySelectorAll('.opt'), function (x) { x.disabled = true; });
          if (i === correctIdx) { b.classList.add('correct'); correct++; }
          else { b.classList.add('wrong'); q.querySelectorAll('.opt')[correctIdx].classList.add('correct'); }
          why.classList.add('show');
          score.textContent = 'Score: ' + correct + ' / ' + answered + (answered === total ? '  — done. Now say each answer out loud.' : '');
        });
        q.appendChild(b);
      });
      q.appendChild(why); root.appendChild(q);
    });
    root.appendChild(score);
  };

  window.renderRecall = function (selector, cards) {
    var root = document.querySelector(selector);
    if (!root) return;
    root.classList.add('recall');
    var head = document.createElement('div'); head.className = 'recall-head'; head.textContent = 'Say it out loud, then flip';
    var sub = document.createElement('div'); sub.className = 'quiz-sub';
    sub.textContent = 'Answer each aloud as if the interviewer asked it. Tap to reveal a model answer, then compare.';
    root.appendChild(head); root.appendChild(sub);
    cards.forEach(function (c) {
      var card = document.createElement('div'); card.className = 'card';
      var p = document.createElement('div'); p.className = 'prompt'; p.textContent = c.prompt;
      var h = document.createElement('div'); h.className = 'hint'; h.textContent = 'Tap to reveal model answer';
      var a = document.createElement('div'); a.className = 'ans'; a.innerHTML = c.answer;
      card.appendChild(p); card.appendChild(h); card.appendChild(a);
      card.addEventListener('click', function () { card.classList.toggle('open'); });
      root.appendChild(card);
    });
  };
})();
