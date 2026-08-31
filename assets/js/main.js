document.addEventListener('DOMContentLoaded', function () {
  var config = window.CRM_CONFIG || {};
  var contactEmail = config.contactEmail || 'hello@carerm.co.uk';

  // ---- Mobile nav toggle -------------------------------------------------
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    function setNavOpen(open) {
      nav.classList.toggle('open', open);
      document.body.classList.toggle('nav-open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    }

    toggle.addEventListener('click', function () {
      setNavOpen(!nav.classList.contains('open'));
    });

    nav.addEventListener('click', function (event) {
      if (event.target.closest('a')) setNavOpen(false);
    });

    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && nav.classList.contains('open')) {
        setNavOpen(false);
        toggle.focus();
      }
    });

    window.addEventListener('resize', function () {
      if (window.innerWidth > 1080 && nav.classList.contains('open')) {
        setNavOpen(false);
      }
    });
  }

  // ---- FAQ accordion -----------------------------------------------------
  var faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(function (item) {
    var question = item.querySelector('.faq-question');
    if (!question) return;
    question.addEventListener('click', function () {
      var isOpen = item.classList.contains('open');
      faqItems.forEach(function (i) {
        i.classList.remove('open');
        var q = i.querySelector('.faq-question');
        if (q) q.setAttribute('aria-expanded', 'false');
      });
      if (!isOpen) {
        item.classList.add('open');
        question.setAttribute('aria-expanded', 'true');
      }
    });
  });

  // ---- Contact form ------------------------------------------------------
  var form = document.querySelector('.contact-form');
  if (!form) return;

  var status = form.querySelector('.form-status');
  var submitBtn = form.querySelector('button[type="submit"]');
  var confirmation = document.querySelector('.form-confirmation');
  var endpoint = config.formEndpoint || '';
  var mailto = '<a href="mailto:' + contactEmail + '">' + contactEmail + '</a>';

  function setStatus(message, kind) {
    if (!status) return;
    status.innerHTML = message;
    status.className = 'form-status' + (kind ? ' is-' + kind : '');
  }

  // No endpoint configured: say so up front rather than letting someone type
  // out an enquiry that has nowhere to go.
  if (!endpoint) {
    var warning = document.createElement('div');
    warning.className = 'notice notice-warning';
    warning.innerHTML =
      '<strong>This form isn\'t connected yet.</strong> Please email us directly at ' +
      mailto + ' and we\'ll reply within one working day.';
    form.parentNode.insertBefore(warning, form);
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    if (!form.checkValidity()) {
      form.reportValidity();
      setStatus('Please fill in the highlighted fields so we can reply to you.', 'error');
      return;
    }

    // Honeypot: a real person never fills this in. Pretend all is well so the
    // bot doesn't retry, but send nothing.
    if (form.querySelector('[name="company-website"]').value) {
      form.style.display = 'none';
      if (confirmation) confirmation.style.display = 'block';
      return;
    }

    if (!endpoint) {
      setStatus(
        'This form isn\'t connected to an inbox yet, so nothing was sent. ' +
        'Please email ' + mailto + ' instead — sorry about that.',
        'error'
      );
      return;
    }

    var originalLabel = submitBtn ? submitBtn.textContent : '';
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.textContent = 'Sending…';
    }
    setStatus('Sending your enquiry…', '');

    fetch(endpoint, {
      method: 'POST',
      body: new FormData(form),
      headers: { Accept: 'application/json' }
    })
      .then(function (response) {
        if (!response.ok) throw new Error('Request failed with status ' + response.status);
        // Only now, having actually delivered it, do we say it's on its way.
        form.style.display = 'none';
        if (confirmation) confirmation.style.display = 'block';
        if (confirmation) confirmation.focus();
      })
      .catch(function () {
        setStatus(
          'Sorry, we couldn\'t send that just now. Please try again, or email ' +
          mailto + ' and we\'ll pick it up straight away.',
          'error'
        );
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.textContent = originalLabel;
        }
      });
  });
});
