(function () {
  'use strict';

  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  const SCRAMBLE_CHARS = '!<>-_\\/[]{}—=+*^?#________';

  /* ──────────────────────────────────────────
   * SPLIT TEXT — wrap each char in <span class="char">
   * ──────────────────────────────────────────*/
  document.querySelectorAll('[data-split]').forEach((el) => {
    const text = el.textContent;
    el.textContent = '';
    [...text].forEach((ch, i) => {
      const span = document.createElement('span');
      span.className = 'char';
      span.style.transitionDelay = (0.04 * i) + 's';
      span.textContent = ch === ' ' ? ' ' : ch;
      el.appendChild(span);
    });
  });

  /* ──────────────────────────────────────────
   * REVEAL ON SCROLL
   * ──────────────────────────────────────────*/
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -10% 0px' });

  document.querySelectorAll('.reveal, .reveal-stagger, .char-reveal').forEach((el) => io.observe(el));

  const heroName = document.getElementById('hero-name');
  if (heroName) requestAnimationFrame(() => heroName.classList.add('is-visible'));

  /* ──────────────────────────────────────────
   * KINETIC PARALLAX — letters follow cursor
   * ──────────────────────────────────────────*/
  if (heroName && fine && !reduced) {
    const chars = heroName.querySelectorAll('.char');
    const STRENGTH = 22;
    let raf = null, mx = 0, my = 0;

    window.addEventListener('mousemove', (e) => {
      mx = e.clientX; my = e.clientY;
      if (!raf) raf = requestAnimationFrame(updateParallax);
    });

    function updateParallax() {
      raf = null;
      chars.forEach((ch) => {
        const r = ch.getBoundingClientRect();
        const dx = (mx - (r.left + r.width / 2)) / window.innerWidth;
        const dy = (my - (r.top + r.height / 2)) / window.innerHeight;
        ch.style.transform = `translate(${dx * STRENGTH}px, ${dy * STRENGTH}px)`;
      });
    }
  }

  /* ──────────────────────────────────────────
   * SCRAMBLE TEXT — utility
   * ──────────────────────────────────────────*/
  function scrambleText(el, finalText, duration = 700) {
    const len = finalText.length;
    let frame = 0;
    const totalFrames = Math.ceil(duration / 40);
    const lockFrames = new Array(len).fill(0).map((_, i) =>
      Math.floor((i / len) * totalFrames * 0.7) + Math.floor(Math.random() * 6)
    );

    cancelAnimationFrame(el._scrambleRAF);

    function tick() {
      let out = '';
      for (let i = 0; i < len; i++) {
        if (frame >= lockFrames[i]) {
          out += finalText[i];
        } else if (finalText[i] === ' ') {
          out += ' ';
        } else {
          out += SCRAMBLE_CHARS[Math.floor(Math.random() * SCRAMBLE_CHARS.length)];
        }
      }
      el.textContent = out;
      frame++;
      if (frame <= totalFrames) {
        el._scrambleRAF = requestAnimationFrame(() => setTimeout(tick, 30));
      } else {
        el.textContent = finalText;
      }
    }
    tick();
  }

  /* ──────────────────────────────────────────
   * ROLE SHUFFLE (hero subtitle cycler)
   * ──────────────────────────────────────────*/
  const roleEl = document.getElementById('role-shuffle');
  if (roleEl && !reduced) {
    let roles;
    try { roles = JSON.parse(roleEl.dataset.roles); } catch { roles = []; }
    if (roles.length > 1) {
      let idx = 0;
      setInterval(() => {
        idx = (idx + 1) % roles.length;
        scrambleText(roleEl, roles[idx], 800);
      }, 2800);
    }
  }

  /* ──────────────────────────────────────────
   * SCRAMBLE on WATERMARK hover
   * ──────────────────────────────────────────*/
  document.querySelectorAll('.section-watermark').forEach((el) => {
    const original = el.textContent.trim();
    let scrambling = false;
    el.style.cursor = 'pointer';
    el.style.pointerEvents = 'auto';
    el.addEventListener('mouseenter', () => {
      if (scrambling) return;
      scrambling = true;
      scrambleText(el, original, 600);
      setTimeout(() => { scrambling = false; }, 700);
    });
  });

  /* ──────────────────────────────────────────
   * CUSTOM CURSOR + TRAIL
   * ──────────────────────────────────────────*/
  if (fine && !reduced) {
    const dot = document.getElementById('cursor-dot');
    const ring = document.getElementById('cursor-ring');
    if (dot && ring) {
      let mx = 0, my = 0, rx = 0, ry = 0;
      let lastTrailTime = 0;

      window.addEventListener('mousemove', (e) => {
        mx = e.clientX; my = e.clientY;
        dot.style.transform = `translate3d(${mx}px, ${my}px, 0) translate(-50%, -50%)`;

        // Trail particle every 50ms
        const now = performance.now();
        if (now - lastTrailTime > 50) {
          spawnTrail(mx, my);
          lastTrailTime = now;
        }
      });

      function tick() {
        rx += (mx - rx) * 0.18;
        ry += (my - ry) * 0.18;
        ring.style.transform = `translate3d(${rx}px, ${ry}px, 0) translate(-50%, -50%)`;
        requestAnimationFrame(tick);
      }
      tick();

      const hoverables = 'a, button, [data-magnetic], input, .project-card, .section-watermark';
      document.querySelectorAll(hoverables).forEach((el) => {
        el.addEventListener('mouseenter', () => {
          ring.classList.add('is-hover');
          dot.classList.add('is-hover');
        });
        el.addEventListener('mouseleave', () => {
          ring.classList.remove('is-hover');
          dot.classList.remove('is-hover');
        });
      });
    }

    function spawnTrail(x, y) {
      const t = document.createElement('span');
      t.className = 'cursor-trail';
      t.style.left = x + 'px';
      t.style.top = y + 'px';
      document.body.appendChild(t);
      setTimeout(() => t.remove(), 700);
    }
  }

  /* ──────────────────────────────────────────
   * MAGNETIC BUTTONS
   * ──────────────────────────────────────────*/
  if (fine && !reduced) {
    document.querySelectorAll('[data-magnetic]').forEach((el) => {
      const STRENGTH = 0.3;
      el.addEventListener('mousemove', (e) => {
        const rect = el.getBoundingClientRect();
        const cx = rect.left + rect.width / 2;
        const cy = rect.top + rect.height / 2;
        el.style.transform = `translate(${(e.clientX - cx) * STRENGTH}px, ${(e.clientY - cy) * STRENGTH}px)`;
      });
      el.addEventListener('mouseleave', () => { el.style.transform = ''; });
    });
  }

  /* ──────────────────────────────────────────
   * COUNTERS
   * ──────────────────────────────────────────*/
  const counterIO = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      const el = entry.target;
      const target = parseInt(el.dataset.target, 10);
      const start = performance.now();
      function step(now) {
        const t = Math.min(1, (now - start) / 1400);
        const eased = 1 - Math.pow(1 - t, 3);
        el.textContent = Math.floor(eased * target) + '+';
        if (t < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
      counterIO.unobserve(el);
    });
  }, { threshold: 0.5 });
  document.querySelectorAll('[data-counter]').forEach((el) => counterIO.observe(el));

  /* ──────────────────────────────────────────
   * HUD WIDGET — live clock + scroll-spy
   * ──────────────────────────────────────────*/
  const hudClock = document.getElementById('hud-clock');
  const hudSection = document.getElementById('hud-section');
  if (hudClock) {
    function updateClock() {
      const now = new Date();
      const madrid = new Intl.DateTimeFormat('es-ES', {
        timeZone: 'Europe/Madrid',
        hour12: false,
        hour: '2-digit', minute: '2-digit', second: '2-digit',
      }).format(now);
      hudClock.textContent = madrid;
    }
    updateClock();
    setInterval(updateClock, 1000);
  }

  if (hudSection) {
    const sections = document.querySelectorAll('section[data-hud]');
    const sectionIO = new IntersectionObserver((entries) => {
      // Pick the most-visible intersecting section
      let best = null;
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          if (!best || entry.intersectionRatio > best.intersectionRatio) best = entry;
        }
      });
      if (best) hudSection.textContent = best.target.dataset.hud;
    }, { threshold: [0.25, 0.5, 0.75] });
    sections.forEach((s) => sectionIO.observe(s));
  }

  /* ──────────────────────────────────────────
   * HEADER SCROLL STATE
   * ──────────────────────────────────────────*/
  const header = document.getElementById('site-header');
  if (header) {
    const onScroll = () => {
      if (window.scrollY > 40) {
        header.style.backgroundColor = 'color-mix(in oklab, var(--bg) 80%, transparent)';
        header.style.backdropFilter = 'blur(12px)';
        header.style.borderBottom = '1px solid var(--line)';
      } else {
        header.style.backgroundColor = '';
        header.style.backdropFilter = '';
        header.style.borderBottom = '';
      }
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ──────────────────────────────────────────
   * MOBILE MENU
   * ──────────────────────────────────────────*/
  const mobBtn = document.getElementById('mobile-menu-btn');
  const mobMenu = document.getElementById('mobile-menu');
  const mobClose = document.getElementById('mobile-menu-close');
  if (mobBtn && mobMenu) {
    const openMenu = () => {
      mobMenu.classList.add('is-open');
      document.body.classList.add('menu-open');
      mobBtn.setAttribute('aria-expanded', 'true');
      mobMenu.setAttribute('aria-hidden', 'false');
    };
    const closeMenu = () => {
      mobMenu.classList.remove('is-open');
      document.body.classList.remove('menu-open');
      mobBtn.setAttribute('aria-expanded', 'false');
      mobMenu.setAttribute('aria-hidden', 'true');
    };
    mobBtn.addEventListener('click', openMenu);
    mobClose && mobClose.addEventListener('click', closeMenu);
    mobMenu.querySelectorAll('a[href^="#"]').forEach((a) =>
      a.addEventListener('click', closeMenu)
    );
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mobMenu.classList.contains('is-open')) closeMenu();
    });
  }

  /* ──────────────────────────────────────────
   * EASTER EGG — triple-click DC logo for confetti
   * ──────────────────────────────────────────*/
  const logo = document.querySelector('a[aria-label="Home"]');
  if (logo) {
    let clicks = 0, timer;
    logo.addEventListener('click', (e) => {
      clicks++;
      clearTimeout(timer);
      if (clicks >= 3) {
        e.preventDefault();
        clicks = 0;
        burstConfetti();
      } else {
        timer = setTimeout(() => { clicks = 0; }, 600);
      }
    });
  }

  function burstConfetti() {
    const root = document.body;
    const COUNT = 32;
    for (let i = 0; i < COUNT; i++) {
      const p = document.createElement('span');
      p.className = 'confetti-particle';
      const angle = Math.random() * Math.PI * 2;
      const dist = 80 + Math.random() * 220;
      const dx = Math.cos(angle) * dist;
      const dy = Math.sin(angle) * dist - 60;
      p.style.setProperty('--dx', dx + 'px');
      p.style.setProperty('--dy', dy + 'px');
      p.style.setProperty('--rot', (Math.random() * 720 - 360) + 'deg');
      p.style.left = '32px';
      p.style.top = '50px';
      root.appendChild(p);
      setTimeout(() => p.remove(), 1100);
    }
  }
})();
