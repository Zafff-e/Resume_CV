/* ==========================================================================
   AHM ZAFIR HASAN — CV Interactive Script
   Handles: scroll animations, skill bar fills, dark mode, print
   ========================================================================== */

(function () {
  'use strict';

  // Remove no-js class to enable CSS animations
  document.documentElement.classList.remove('no-js');

  // ==========================================================================
  // INTERSECTION OBSERVER — Fade-in sections on scroll
  // ==========================================================================
  const sections = document.querySelectorAll('.content-section');

  if ('IntersectionObserver' in window) {
    const sectionObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            sectionObserver.unobserve(entry.target);
          }
        });
      },
      {
        root: null,
        rootMargin: '0px 0px -60px 0px',
        threshold: 0.1,
      }
    );

    sections.forEach((section) => sectionObserver.observe(section));
  } else {
    // Fallback: just show everything
    sections.forEach((section) => section.classList.add('visible'));
  }

  // ==========================================================================
  // SKILL BAR ANIMATION — Fill bars when they enter viewport
  // ==========================================================================
  const skillBars = document.querySelectorAll('.skill-bar__fill[data-width]');

  if ('IntersectionObserver' in window && skillBars.length) {
    const barObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const targetWidth = entry.target.getAttribute('data-width');
            // Small delay for a staggered effect
            const index = Array.from(skillBars).indexOf(entry.target);
            setTimeout(() => {
              entry.target.style.width = targetWidth + '%';
            }, index * 120);
            barObserver.unobserve(entry.target);
          }
        });
      },
      {
        root: null,
        rootMargin: '0px',
        threshold: 0.3,
      }
    );

    skillBars.forEach((bar) => barObserver.observe(bar));
  } else {
    // Fallback: set widths immediately
    skillBars.forEach((bar) => {
      bar.style.width = bar.getAttribute('data-width') + '%';
    });
  }

  // ==========================================================================
  // DARK MODE TOGGLE
  // ==========================================================================
  const themeToggle = document.getElementById('themeToggle');
  const themeLabel = themeToggle ? themeToggle.querySelector('span') : null;
  const themeSvg = themeToggle ? themeToggle.querySelector('svg') : null;

  // Check saved preference
  const savedTheme = localStorage.getItem('cv-theme');
  if (savedTheme === 'dark') {
    document.body.classList.add('dark-mode');
    updateThemeButton(true);
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const isDark = document.body.classList.toggle('dark-mode');
      localStorage.setItem('cv-theme', isDark ? 'dark' : 'light');
      updateThemeButton(isDark);
    });
  }

  function updateThemeButton(isDark) {
    if (themeLabel) {
      themeLabel.textContent = isDark ? 'Light Mode' : 'Dark Mode';
    }
    if (themeSvg) {
      if (isDark) {
        // Sun icon
        themeSvg.innerHTML =
          '<circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>';
      } else {
        // Moon icon
        themeSvg.innerHTML =
          '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>';
      }
    }
  }

  // ==========================================================================
  // PRINT BUTTON
  // ==========================================================================
  const printBtn = document.getElementById('printBtn');

  if (printBtn) {
    printBtn.addEventListener('click', () => {
      // Temporarily ensure all sections are visible for printing
      sections.forEach((section) => section.classList.add('visible'));

      // Ensure skill bars are filled for print
      skillBars.forEach((bar) => {
        bar.style.width = bar.getAttribute('data-width') + '%';
      });

      // Small delay to let styles apply
      setTimeout(() => {
        window.print();
      }, 100);
    });
  }

  // ==========================================================================
  // STAGGERED ANIMATION for sidebar elements
  // ==========================================================================
  const sidebarItems = document.querySelectorAll(
    '.sidebar-section, .contact-list__item, .profile'
  );

  sidebarItems.forEach((item, index) => {
    item.style.opacity = '0';
    item.style.transform = 'translateY(15px)';
    item.style.transition = `opacity 0.5s ease ${index * 0.08}s, transform 0.5s ease ${index * 0.08}s`;

    // Trigger after a short delay
    setTimeout(() => {
      item.style.opacity = '1';
      item.style.transform = 'translateY(0)';
    }, 100);
  });

  // ==========================================================================
  // HOVER RIPPLE EFFECT for project cards
  // ==========================================================================
  const cards = document.querySelectorAll('.project-card, .timeline-item, .education-item');

  cards.forEach((card) => {
    card.addEventListener('mouseenter', function (e) {
      const rect = this.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      this.style.setProperty('--ripple-x', x + 'px');
      this.style.setProperty('--ripple-y', y + 'px');
    });
  });

})();
