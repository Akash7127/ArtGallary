/* Filter form: auto-submit on change, slide-in filter panel on phones. */
(function () {
  var form = document.querySelector('form[data-auto-submit]');
  if (!form) return;

  // Drop empty price inputs so URLs stay clean, then submit.
  function submit() {
    form.querySelectorAll('input[type="number"]').forEach(function (input) {
      input.disabled = input.value === '';
    });
    form.submit();
  }

  var timer;
  form.addEventListener('change', function (event) {
    if (!form.hasAttribute('data-auto-submit')) return;
    if (event.target.type === 'number') {
      clearTimeout(timer);
      timer = setTimeout(submit, 600);
    } else {
      submit();
    }
  });
  form.addEventListener('submit', function (event) {
    event.preventDefault();
    submit();
  });

  var toggle = form.querySelector('[data-filter-toggle]');
  var panel = toggle ? document.getElementById(toggle.getAttribute('aria-controls')) : null;
  function setOpen(open) {
    if (!toggle || !panel) return;
    panel.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', open);
    document.documentElement.classList.toggle('ag-lock', open);
    if (open) panel.querySelector('button, input, summary').focus();
  }
  if (toggle) toggle.addEventListener('click', function () { setOpen(true); });
  form.querySelectorAll('[data-filter-close]').forEach(function (button) {
    button.addEventListener('click', function () { setOpen(false); toggle.focus(); });
  });
  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && panel && panel.classList.contains('is-open')) {
      setOpen(false);
      toggle.focus();
    }
  });
})();
