/* ============================================================
   ERRORS2EXPERTS — MODERN JS ENHANCEMENT
   Drop-in enhancement; safe on all pages.
   ============================================================ */

(function () {
  'use strict';

  /* ── SCROLL PROGRESS BAR ── */
  const bar = document.createElement('div');
  bar.id = 'scroll-progress';
  document.body.prepend(bar);

  /* ── BACK TO TOP ── */
  const btn = document.createElement('button');
  btn.id = 'back-to-top';
  btn.setAttribute('aria-label', 'Back to top');
  btn.innerHTML = '↑';
  document.body.appendChild(btn);
  btn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  /* ── SCROLL EVENTS ── */
  let ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      const scrolled = window.scrollY;
      const total = document.documentElement.scrollHeight - window.innerHeight;
      const pct = total > 0 ? (scrolled / total) * 100 : 0;

      // Progress bar
      bar.style.width = pct + '%';

      // Back to top visibility
      if (scrolled > 400) btn.classList.add('visible');
      else btn.classList.remove('visible');

      // Navbar shrink
      const nav = document.querySelector('.navbar');
      if (nav) {
        if (scrolled > 60) nav.classList.add('scrolled');
        else nav.classList.remove('scrolled');
      }

      ticking = false;
    });
  }
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ── ACTIVE NAV LINK ── */
  const currentPath = window.location.pathname;
  document.querySelectorAll('.navbar .nav-link').forEach(link => {
    const href = link.getAttribute('href');
    if (href && (currentPath === href || (href !== '/' && currentPath.startsWith(href)))) {
      link.classList.add('active');
    }
  });

  /* ── INTERSECTION OBSERVER – REVEAL ── */
  const revealSelectors = '.reveal, .reveal-left, .reveal-right, .reveal-scale, .stagger-children';
  const revealEls = document.querySelectorAll(revealSelectors);

  if (revealEls.length > 0) {
    const revealObs = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          revealObs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    revealEls.forEach(el => revealObs.observe(el));
  }

  /* ── COUNTER ANIMATION ── */
  function animateCounter(el, target, duration) {
    const start = performance.now();
    const startVal = 0;
    function update(now) {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      // Ease out cubic
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = Math.round(startVal + (target - startVal) * eased);
      el.textContent = current;
      if (progress < 1) requestAnimationFrame(update);
      else el.textContent = target;
    }
    requestAnimationFrame(update);
  }

  const counterObs = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = parseInt(el.dataset.target || el.textContent.replace(/\D/g, ''), 10);
        if (!isNaN(target) && target > 0) {
          animateCounter(el, target, 1800);
        }
        counterObs.unobserve(el);
      }
    });
  }, { threshold: 0.5 });

  document.querySelectorAll('.counter-number').forEach(el => {
    const val = parseInt(el.textContent.replace(/\D/g, ''), 10);
    if (!isNaN(val) && val > 0) {
      el.dataset.target = val;
      el.textContent = '0';
      counterObs.observe(el);
    }
  });

  /* ── HERO MESH INJECT ── */
  const heroSlide = document.querySelector('.hero-slide');
  if (heroSlide) {
    const mesh = document.createElement('div');
    mesh.className = 'hero-mesh';
    heroSlide.prepend(mesh);

    // Scroll indicator
    const indicator = document.createElement('div');
    indicator.className = 'hero-scroll-indicator';
    indicator.innerHTML = `
      <div class="scroll-dot"></div>
      <span>Scroll</span>
    `;
    indicator.addEventListener('click', () => {
      const next = document.querySelector('#about, .auto-course-section, section:not(.hero-slider)');
      if (next) next.scrollIntoView({ behavior: 'smooth' });
    });
    heroSlide.appendChild(indicator);
  }

  /* ── AUTO-ADD REVEAL CLASSES to existing AOS elements ── */
  document.querySelectorAll('[data-aos="fade-right"]').forEach(el => {
    if (!el.classList.contains('reveal-left')) el.classList.add('reveal-left');
  });
  document.querySelectorAll('[data-aos="fade-left"]').forEach(el => {
    if (!el.classList.contains('reveal-right')) el.classList.add('reveal-right');
  });
  document.querySelectorAll('[data-aos="zoom-in"], [data-aos="fade-up"]').forEach(el => {
    if (!el.classList.contains('reveal')) el.classList.add('reveal');
  });

  /* ── STAGGER SERVICE / COURSE CARDS ── */
  ['#courses .row', '.services-section .row', '.career-row'].forEach(sel => {
    const row = document.querySelector(sel);
    if (row && !row.classList.contains('stagger-children')) {
      row.classList.add('stagger-children');
      const revealObs2 = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            revealObs2.unobserve(entry.target);
          }
        });
      }, { threshold: 0.08 });
      revealObs2.observe(row);
    }
  });

  /* ── CONTACT FORM WRAPPER CLASS ── */
  document.querySelectorAll('.contact form, form.col-md-6').forEach(form => {
    const wrapper = form.closest('.col-md-6') || form.parentElement;
    if (wrapper) wrapper.classList.add('contact-form-wrapper');
    // Also add class to the form itself for input targeting
    form.classList.add('contact-form-wrapper');
  });

  /* ── SMOOTH DEMOFORM SUBMIT – SAFE CHECK ── */
  const demoForm = document.getElementById('demoForm');
  if (demoForm) {
    // Already handled in base.html, just ensure it doesn't error
  }

  /* ── COUNTER SECTION WRAPPER UPGRADE ── */
  // Find the inline counter div and upgrade it
  document.querySelectorAll('[style*="text-align:center"][style*="padding:40px"]').forEach(div => {
    div.classList.add('counter-section');
    div.removeAttribute('style');

    const h1 = div.querySelector('h1');
    const p  = div.querySelector('p');
    if (h1) { h1.className = 'counter-number'; }
    if (p)  { p.className = 'counter-label'; }
  });

})();


// kalam page counts

document.addEventListener('DOMContentLoaded', function () {
  var counters = document.querySelectorAll('.kalam-hero-section .counter-value');
  if (!counters.length) return;

  var animated = false;

  function animateCounters() {
    if (animated) return;
    animated = true;
    counters.forEach(function (el) {
      var target = parseInt(el.getAttribute('data-target'), 10) || 0;
      var suffix = el.getAttribute('data-suffix') || '';
      if (target === 0) { return; }
      var duration = 1400;
      var startTime = null;

      function step(timestamp) {
        if (!startTime) startTime = timestamp;
        var progress = Math.min((timestamp - startTime) / duration, 1);
        var eased = 1 - Math.pow(1 - progress, 3);
        el.textContent = Math.floor(eased * target) + suffix;
        if (progress < 1) {
          requestAnimationFrame(step);
        } else {
          el.textContent = target + suffix;
        }
      }
      requestAnimationFrame(step);
    });
  }

  var section = document.querySelector('.kalam-hero-section');
  if (!section) return;

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        animateCounters();
        observer.disconnect();
      }
    });
  }, { threshold: 0.3 });

  observer.observe(section);
});