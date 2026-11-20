(function () {
  // Sticky header shadow
  var header = document.querySelector('.site-header');
  var onScroll = function () { if (header) header.classList.toggle('scrolled', window.scrollY > 8); };
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  // Mobile nav
  var burger = document.querySelector('.burger');
  var nav = document.querySelector('.nav');
  if (burger && nav) {
    burger.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  document.querySelectorAll('.nav .dd > button').forEach(function (b) {
    b.addEventListener('click', function (e) {
      e.stopPropagation();
      var dd = b.parentElement; var open = dd.classList.toggle('open');
      b.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  document.addEventListener('click', function (e) {
    document.querySelectorAll('.nav .dd.open').forEach(function (dd) {
      if (!dd.contains(e.target) && !(nav && nav.classList.contains('open'))) dd.classList.remove('open');
    });
  });

  // Reveal on scroll
  var els = document.querySelectorAll('.rv');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    els.forEach(function (el) { io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add('in'); }); }

  // Element wheel: hover updates core text
  var core = document.querySelector('.wheel .core');
  if (core) {
    var def = core.innerHTML;
    document.querySelectorAll('.wheel .seg').forEach(function (s) {
      var show = function () {
        core.innerHTML = '<div><small style="color:' + s.dataset.color + '">' + s.dataset.name + '</small><strong>' + s.dataset.title + '</strong><span>' + s.dataset.desc + '</span></div>';
      };
      s.addEventListener('mouseenter', show);
      s.addEventListener('focus', show);
      s.addEventListener('mouseleave', function () { core.innerHTML = def; });
      s.addEventListener('blur', function () { core.innerHTML = def; });
    });
  }

  // Tabs
  document.querySelectorAll('[data-tabs]').forEach(function (root) {
    var tabs = root.querySelectorAll('.tab');
    tabs.forEach(function (t) {
      t.addEventListener('click', function () {
        tabs.forEach(function (x) { x.setAttribute('aria-selected', x === t ? 'true' : 'false'); });
        root.querySelectorAll('.panel').forEach(function (p) { p.classList.toggle('on', p.id === t.getAttribute('aria-controls')); });
      });
    });
  });

  // Enquiry form -> opens email app with details filled in (static site, no server)
  document.querySelectorAll('form[data-enquiry]').forEach(function (f) {
    var params = new URLSearchParams(location.search);
    var pre = params.get('interest');
    if (pre) { var cb = f.querySelector('input[name="interest"][value="' + pre + '"]'); if (cb) cb.checked = true; }
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!f.reportValidity()) return;
      var d = new FormData(f);
      var interests = d.getAll('interest').join(', ') || 'General';
      var lines = [
        'Name: ' + (d.get('name') || ''),
        'Company: ' + (d.get('company') || ''),
        'Phone: ' + (d.get('phone') || ''),
        'Email: ' + (d.get('email') || ''),
        'City: ' + (d.get('city') || ''),
        'Interested in: ' + interests,
        '',
        (d.get('message') || '')
      ];
      var subject = 'Website enquiry: ' + interests + ' (' + (d.get('name') || '') + ')';
      var href = 'mailto:salesinfo.isepl@gmail.com?cc=isepl.india@gmail.com&subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(lines.join('\n'));
      window.location.href = href;
      var ok = f.querySelector('.ok'); if (ok) ok.classList.add('show');
    });
  });

  // Notify form on coming-soon page
  document.querySelectorAll('form[data-notify]').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var v = f.querySelector('input').value;
      window.location.href = 'mailto:isepl.india@gmail.com?subject=' + encodeURIComponent('Notify me: ISEPL Solar / Sky solutions') + '&body=' + encodeURIComponent('Please keep me updated on ISEPL solar solutions.\nContact: ' + v);
    });
  });

  var y = document.getElementById('yr'); if (y) y.textContent = new Date().getFullYear();
})();
