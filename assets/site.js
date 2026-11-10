/* Prestia site: theme toggle, mobile menu, copy buttons and the FAQ accordion. */
(function () {
  'use strict';
  var root = document.documentElement;
  var KEY = 'prestia-theme';
  var media = window.matchMedia ? window.matchMedia('(prefers-color-scheme: dark)') : null;

  function effectiveTheme() {
    var set = root.getAttribute('data-theme');
    if (set === 'light' || set === 'dark') return set;
    return media && media.matches ? 'dark' : 'light';
  }

  function syncToggle() {
    var next = effectiveTheme() === 'dark' ? 'light' : 'dark';
    var text = 'Switch to ' + next + ' mode';
    document.querySelectorAll('[data-theme-toggle]').forEach(function (b) {
      b.setAttribute('aria-label', text);
      b.setAttribute('title', text);
    });
  }

  document.querySelectorAll('[data-theme-toggle]').forEach(function (b) {
    b.addEventListener('click', function () {
      var next = effectiveTheme() === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem(KEY, next); } catch (e) { /* storage may be blocked */ }
      syncToggle();
    });
  });
  if (media) {
    var onChange = function () { syncToggle(); };
    if (media.addEventListener) media.addEventListener('change', onChange);
    else if (media.addListener) media.addListener(onChange);
  }
  syncToggle();

  // Mobile menu
  var menuBtn = document.querySelector('[data-menu-toggle]');
  var menu = document.getElementById('mobile-menu');
  function setMenu(open) {
    if (!menuBtn || !menu) return;
    menu.hidden = !open;
    menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    menuBtn.textContent = open ? 'Close' : 'Menu';
  }
  if (menuBtn && menu) {
    menuBtn.addEventListener('click', function () { setMenu(menu.hidden); });
    menu.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !menu.hidden) { setMenu(false); menuBtn.focus(); }
    });
    window.addEventListener('resize', function () { if (window.innerWidth > 760 && !menu.hidden) setMenu(false); });
  }

  // Copy email buttons
  var status = document.querySelector('[data-copy-status]');
  document.querySelectorAll('[data-copy]').forEach(function (btn) {
    var timer;
    btn.addEventListener('click', function () {
      var value = btn.getAttribute('data-copy');
      var done = function () {
        btn.textContent = 'Copied';
        if (status) status.textContent = 'Email address copied';
        clearTimeout(timer);
        timer = setTimeout(function () {
          btn.textContent = 'Copy';
          if (status) status.textContent = '';
        }, 1600);
      };
      try {
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(value).then(done, function () { fallbackCopy(value) && done(); });
        } else if (fallbackCopy(value)) {
          done();
        }
      } catch (e) { /* nothing to copy with */ }
    });
  });
  function fallbackCopy(text) {
    try {
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.setAttribute('readonly', '');
      ta.style.position = 'fixed';
      ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      var ok = document.execCommand('copy');
      document.body.removeChild(ta);
      return ok;
    } catch (e) { return false; }
  }

  // FAQ: one open at a time, the first open to begin with.
  document.querySelectorAll('[data-accordion]').forEach(function (group) {
    var items = group.querySelectorAll('.faq');
    function set(item, open) {
      item.classList.toggle('open', open);
      var q = item.querySelector('.faq-q');
      q.setAttribute('aria-expanded', open ? 'true' : 'false');
      item.querySelector('.faq-mark').textContent = open ? '–' : '+';
    }
    items.forEach(function (item) {
      item.querySelector('.faq-q').addEventListener('click', function () {
        var opening = !item.classList.contains('open');
        items.forEach(function (other) { set(other, false); });
        if (opening) set(item, true);
      });
    });
  });
})();
