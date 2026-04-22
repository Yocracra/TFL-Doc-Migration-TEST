(() => {
  const collapseSidebar = () => {
    document.querySelectorAll('.md-nav__toggle').forEach((toggle) => {
      toggle.checked = false;
    });
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      requestAnimationFrame(collapseSidebar);
    });
  } else {
    requestAnimationFrame(collapseSidebar);
  }

  window.addEventListener('load', collapseSidebar);
})();