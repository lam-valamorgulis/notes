/* ============================================================
   quiz.js — reusable retrieval-practice widgets for the course.
   Two components, both self-styled (theme via base.css variables):

   1) renderQuiz(selector, questions, opts)
        questions: [{ q, options:[...], answer:<index>, why,
                      rationales:[...] }]   // optional, one per option
        opts:      { title, sub }           // optional block heading
        Multiple choice with instant right/wrong feedback + score.
        rationales let a question explain each WRONG option in place —
        the "why the other three are worse" drill the exam is built on.
        Leave a rationale empty ('') to show nothing for that option.

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
  /* pre-line keeps the blank line between a long scenario and its final question.
     Short one-line questions have no newlines, so nothing changes for them. */
  .q-text { font-weight: 600; margin-bottom: .7rem; white-space: pre-line; }
  .opt-wrap { margin: .4rem 0; }
  .opt-wrap .opt { margin: 0; }
  .rat {
    display: none; font-size: .82rem; line-height: 1.45; color: var(--ink-soft);
    margin: .3rem 0 .55rem .8rem; padding-left: .7rem; border-left: 2px solid var(--rule);
  }
  .rat.show { display: block; }
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

  window.renderQuiz = function (selector, questions, opts) {
    var root = document.querySelector(selector);
    if (!root) return;
    opts = opts || {};
    var answered = 0, correct = 0, total = questions.length;
    var head = document.createElement('div'); head.className = 'quiz-head';
    head.textContent = opts.title || 'Check yourself';
    var sub = document.createElement('div'); sub.className = 'quiz-sub';
    sub.textContent = opts.sub || 'Answer from memory first. Feedback appears instantly.';
    var score = document.createElement('div'); score.className = 'score';
    root.classList.add('quiz'); root.appendChild(head); root.appendChild(sub);

    questions.forEach(function (item) {
      var q = document.createElement('div'); q.className = 'q';
      var qt = document.createElement('div'); qt.className = 'q-text'; qt.textContent = item.q; q.appendChild(qt);
      var why = document.createElement('div'); why.className = 'why'; why.textContent = item.why;
      var locked = false;
      // Shuffle options each render so the correct answer is never always in the same slot
      // (kills the "always A" tell and stops position-memorisation across repeat practice).
      // Text + its rationale + correctness travel together as one pair, so shuffling
      // can never detach an explanation from the option it belongs to.
      var pairs = [];
      for (var p = 0; p < item.options.length; p++) {
        pairs.push({
          text: item.options[p],
          rat: item.rationales ? item.rationales[p] : '',
          correct: p === item.answer
        });
      }
      for (var s = pairs.length - 1; s > 0; s--) {
        var r = Math.floor(Math.random() * (s + 1));
        var tmp = pairs[s]; pairs[s] = pairs[r]; pairs[r] = tmp;
      }
      var correctBtn = null;
      pairs.forEach(function (pair) {
        var wrap = document.createElement('div'); wrap.className = 'opt-wrap';
        var b = document.createElement('button'); b.className = 'opt'; b.textContent = pair.text;
        wrap.appendChild(b);
        if (pair.correct) correctBtn = b;
        if (pair.rat) {
          var rat = document.createElement('div'); rat.className = 'rat'; rat.textContent = pair.rat;
          wrap.appendChild(rat);
        }
        b.addEventListener('click', function () {
          if (locked) return; locked = true;
          answered++;
          Array.prototype.forEach.call(q.querySelectorAll('.opt'), function (x) { x.disabled = true; });
          if (pair.correct) { b.classList.add('correct'); correct++; }
          else { b.classList.add('wrong'); if (correctBtn) correctBtn.classList.add('correct'); }
          Array.prototype.forEach.call(q.querySelectorAll('.rat'), function (x) { x.classList.add('show'); });
          why.classList.add('show');
          score.textContent = 'Score: ' + correct + ' / ' + answered + (answered === total ? '  — done. Now say each answer out loud.' : '');
        });
        q.appendChild(wrap);
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
