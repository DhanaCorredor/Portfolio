(function () {
  'use strict';

  /* Reveal on scroll */
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -10% 0px' });

  document.querySelectorAll('.reveal').forEach((el) => io.observe(el));

  /* Header background on scroll */
  const header = document.getElementById('site-header');
  let onHeaderScroll = null;
  if (header) {
    onHeaderScroll = () => {
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
    onHeaderScroll();
    window.addEventListener('scroll', onHeaderScroll, { passive: true });
  }

  /* Theme toggle (light/dark) */
  const themeBtn = document.getElementById('theme-toggle');
  if (themeBtn) {
    const sunIcon = themeBtn.querySelector('.theme-icon-sun');
    const moonIcon = themeBtn.querySelector('.theme-icon-moon');
    const syncIcons = () => {
      const isLight = document.documentElement.classList.contains('light');
      sunIcon.classList.toggle('hidden', isLight);
      moonIcon.classList.toggle('hidden', !isLight);
    };
    syncIcons();
    themeBtn.addEventListener('click', () => {
      const next = document.documentElement.classList.toggle('light') ? 'light' : 'dark';
      try { localStorage.setItem('theme', next); } catch(e){}
      syncIcons();
      if (onHeaderScroll) onHeaderScroll();
    });
  }

  /* Copy email button */
  const copyBtn = document.getElementById('copy-email');
  if (copyBtn && navigator.clipboard) {
    const label = copyBtn.querySelector('.copy-label');
    const original = label ? label.textContent : '';
    copyBtn.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(copyBtn.dataset.email);
        if (label) label.textContent = 'Copied ✓';
        copyBtn.disabled = true;
        setTimeout(() => {
          if (label) label.textContent = original;
          copyBtn.disabled = false;
        }, 1800);
      } catch(e) {
        if (label) label.textContent = 'Press Ctrl+C';
      }
    });
  }

  /* Mobile menu */
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
})();
