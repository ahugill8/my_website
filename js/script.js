/* =========================================================================
   SITE SCRIPT
   Shared interactive behavior for every page: mobile nav toggle, the
   sliding red "help!" tab (home page), and the publications orbit layout.
   See INSTRUCTIONS.md if you want to tweak timings or behavior.
   ========================================================================= */

document.addEventListener('DOMContentLoaded', function () {

  /* ---- Mobile nav toggle ------------------------------------------------ */
  var toggle = document.querySelector('.nav__toggle');
  var links = document.querySelector('.nav__links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      links.classList.toggle('is-open');
      var expanded = links.classList.contains('is-open');
      toggle.setAttribute('aria-expanded', expanded);
    });
  }

  /* ---- Help tab (home page) --------------------------------------------
     Starts mostly hidden off the right edge. Clicking slides it fully
     into view; clicking again slides it back out. */
  var helpTab = document.querySelector('.help-tab');
  if (helpTab) {
    helpTab.addEventListener('click', function () {
      helpTab.classList.toggle('is-open');
    });
  }

  /* ---- Publications orbit layout ----------------------------------------
     Positions each .pub-logo evenly around the circle defined by
     .pub-orbit, purely with JS math so you can add/remove logos in the
     HTML and they'll auto-space themselves. */
  var orbit = document.querySelector('.pub-orbit');
  if (orbit) {
    var logos = orbit.querySelectorAll('.pub-logo');
    var count = logos.length;
    var radiusPercent = 42; // how far from center, as % of orbit width
    logos.forEach(function (logo, i) {
      var angle = (i / count) * 2 * Math.PI - Math.PI / 2; // start at top
      var x = 50 + radiusPercent * Math.cos(angle);
      var y = 50 + radiusPercent * Math.sin(angle);
      logo.style.left = x + '%';
      logo.style.top = y + '%';
      logo.style.transform = 'translate(-50%, -50%)';
    });
  }

});
