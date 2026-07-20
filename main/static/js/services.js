/**
 * ERRORS2EXPERTS — SERVICES PAGE JS  v1.0
 * Drop into: main/static/js/services_enhanced.js
 * Loaded only on services.html via the {% static %} tag.
 *
 * Features:
 *  • openServiceDetail()  – slides in the detail panel
 *  • closeServiceDetail() – slides it out
 *  • Filter tabs (category filtering)
 *  • FAQ accordion
 *  • "View Details" also triggered by clicking card image overlay
 *  • Body scroll lock while panel open
 *  • ESC key closes panel
 *  • Register buttons inside panel set the service name on the booking modal
 *  • Lightweight scroll-reveal for modal inner sections
 */

(function () {
  'use strict';

  /* ═══════════════════════════════════════════
     ELEMENTS
  ═══════════════════════════════════════════ */
  var overlay  = document.getElementById('svcDetailModal');
  var panel    = document.getElementById('svcDetailPanel');
  var scrollEl = document.getElementById('svcDetailScroll');
  var heroImg  = document.getElementById('svcDetailHeroImg');
  var titleEl  = document.getElementById('svcDetailTitle');
  var tagline  = document.getElementById('svcDetailTagline');
  var descEl   = document.getElementById('svcDetailDesc');

  /* Register buttons inside the detail panel */
  var registerBtnTop    = document.getElementById('svcDetailRegisterBtn');
  var registerBtnBottom = document.getElementById('svcDetailRegisterBtnBottom');

  /* ═══════════════════════════════════════════
     OPEN / CLOSE
  ═══════════════════════════════════════════ */
  var currentServiceName = '';

  /**
   * Called by both the "View Details" button and the image overlay click.
   * @param {HTMLElement} triggerEl - the button that was clicked (inside .svc-card)
   */
  window.openServiceDetail = function (triggerEl) {
    var card = triggerEl.closest('.svc-card');
    if (!card) return;

    var title  = card.dataset.title  || 'Service Details';
    var desc   = card.dataset.desc   || '';
    var img    = card.dataset.img    || '';

    currentServiceName = title;

    /* Populate hero */
    titleEl.textContent  = title;
    descEl.textContent   = desc;
    tagline.textContent  = 'Professional · Certified · E2E Guaranteed';
    heroImg.src          = img;
    heroImg.alt          = title;

    /* Wire register buttons inside panel to the booking modal */
    _wireRegisterBtns(title);

    /* Show overlay */
    overlay.style.display = 'flex';
    document.body.style.overflow = 'hidden';

    /* Trigger slide-in on next paint */
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        panel.classList.add('open');
        /* Announce to screen readers */
        panel.setAttribute('aria-label', 'Service details: ' + title);
        /* Focus close button */
        var closeBtn = document.getElementById('svcDetailClose');
        if (closeBtn) closeBtn.focus();
        /* Reset scroll */
        if (scrollEl) scrollEl.scrollTop = 0;
        /* Run inner reveal */
        _revealModalSections();
      });
    });
  };

  window.closeServiceDetail = function () {
    panel.classList.remove('open');
    document.body.style.overflow = '';

    /* Wait for slide-out animation then hide */
    panel.addEventListener('transitionend', function _onEnd () {
      overlay.style.display = 'none';
      panel.removeEventListener('transitionend', _onEnd);
    });
  };

  /* Click outside panel to close */
  overlay.addEventListener('click', function (e) {
    if (e.target === overlay) window.closeServiceDetail();
  });

  /* ESC key */
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && overlay.style.display !== 'none') {
      window.closeServiceDetail();
    }
  });

  /* Image overlay also opens detail */
  document.querySelectorAll('.svc-card-img-overlay').forEach(function (ov) {
    ov.addEventListener('click', function () {
      var card = ov.closest('.svc-card');
      if (!card) return;
      /* Find the "View Details" button in this card */
      var btn = card.querySelector('.btn-svc-detail');
      if (btn) window.openServiceDetail(btn);
    });
  });

  /* ═══════════════════════════════════════════
     WIRE REGISTER BUTTONS INSIDE PANEL
  ═══════════════════════════════════════════ */
  function _wireRegisterBtns (serviceName) {
    [registerBtnTop, registerBtnBottom].forEach(function (btn) {
      if (!btn) return;
      /* Remove old listeners by cloning */
      var fresh = btn.cloneNode(true);
      btn.parentNode.replaceChild(fresh, btn);

      /* Re-grab references */
      if (btn === registerBtnTop) registerBtnTop = fresh;
      else registerBtnBottom = fresh;

      fresh.addEventListener('click', function () {
        /* Set service name on the hidden input of the booking modal */
        var input = document.getElementById('serviceNameInput');
        if (input) input.value = serviceName;
        /* Close detail panel */
        window.closeServiceDetail();
        /* Open booking modal via Bootstrap */
        var bsModal = new bootstrap.Modal(
          document.getElementById('serviceBookingModal')
        );
        bsModal.show();
      });
    });
  }

  /* ═══════════════════════════════════════════
     FILTER TABS
  ═══════════════════════════════════════════ */
  var tabs  = document.querySelectorAll('.svc-tab');
  var cards = document.querySelectorAll('.svc-card');

  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      var filter = tab.dataset.filter;

      /* Update active state */
      tabs.forEach(function (t) {
        t.classList.remove('active');
        t.setAttribute('aria-selected', 'false');
      });
      tab.classList.add('active');
      tab.setAttribute('aria-selected', 'true');

      /* Filter cards */
      cards.forEach(function (card) {
        if (filter === 'all') {
          card.classList.remove('hidden');
        } else {
          /* Check if card category contains filter keyword */
          var cat = (card.dataset.category || '').toLowerCase();
          var title = (card.dataset.title || '').toLowerCase();
          var match = cat.includes(filter) || title.includes(filter);
          card.classList.toggle('hidden', !match);
        }
      });
    });
  });

  /* ═══════════════════════════════════════════
     FAQ ACCORDION
  ═══════════════════════════════════════════ */
  document.querySelectorAll('.svc-faq-question').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var answer = btn.nextElementSibling;
      var isOpen = btn.getAttribute('aria-expanded') === 'true';

      /* Close all others */
      document.querySelectorAll('.svc-faq-question').forEach(function (b) {
        b.setAttribute('aria-expanded', 'false');
        var a = b.nextElementSibling;
        if (a) a.style.display = 'none';
      });

      /* Toggle clicked */
      if (!isOpen) {
        btn.setAttribute('aria-expanded', 'true');
        if (answer) answer.style.display = 'block';
      }
    });
  });

  /* ═══════════════════════════════════════════
     INNER SCROLL REVEAL (inside modal)
  ═══════════════════════════════════════════ */
  function _revealModalSections () {
    if (!scrollEl) return;
    var sections = scrollEl.querySelectorAll('.svc-detail-section, .svc-detail-stats, .svc-detail-cta');

    /* Reset */
    sections.forEach(function (s) {
      s.style.opacity = '0';
      s.style.transform = 'translateY(20px)';
      s.style.transition = 'none';
    });

    var delay = 0.08;
    sections.forEach(function (s, i) {
      /* Use scroll observer for sections visible in viewport */
      setTimeout(function () {
        s.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        s.style.opacity = '1';
        s.style.transform = 'translateY(0)';
      }, i * 80);
    });
  }

  /* ═══════════════════════════════════════════
     TECH BADGE HOVER — ripple colour pulse
  ═══════════════════════════════════════════ */
  document.querySelectorAll('.svc-tech-badge').forEach(function (badge) {
    badge.addEventListener('mouseenter', function () {
      badge.style.zIndex = '2';
    });
    badge.addEventListener('mouseleave', function () {
      badge.style.zIndex = '';
    });
  });

  /* ═══════════════════════════════════════════
     setServiceName – keep existing compatibility
  ═══════════════════════════════════════════ */
  window.setServiceName = function (name) {
    var input = document.getElementById('serviceNameInput');
    if (input) input.value = name;
  };

})();