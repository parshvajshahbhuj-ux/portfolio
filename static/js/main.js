/**
 * Parshva Shah Portfolio — Main JavaScript
 * Handles: loader, navbar, scroll progress, typing, animations, theme, interactions
 */

(function () {
  "use strict";

  /* ---- Page Loader ---- */
  const loader = document.getElementById("page-loader");
  window.addEventListener("load", () => {
    setTimeout(() => loader && loader.classList.add("hidden"), 400);
  });

  /* ---- Scroll Progress Bar ---- */
  const progressBar = document.getElementById("scroll-progress");
  function updateProgress() {
    if (!progressBar) return;
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    progressBar.style.width = docHeight > 0 ? (scrollTop / docHeight) * 100 + "%" : "0%";
  }
  window.addEventListener("scroll", updateProgress, { passive: true });

  /* ---- Navbar scroll effect ---- */
  const navbar = document.getElementById("navbar");
  function handleNavbarScroll() {
    if (!navbar) return;
    navbar.classList.toggle("scrolled", window.scrollY > 20);
  }
  window.addEventListener("scroll", handleNavbarScroll, { passive: true });

  /* ---- Active nav link ---- */
  const navLinks = document.querySelectorAll(".nav-link");
  const currentPath = window.location.pathname;
  navLinks.forEach((link) => {
    const href = link.getAttribute("href");
    if (!href) return;
    const isHome = href === "/" && currentPath === "/";
    const isOther = href !== "/" && currentPath.startsWith(href);
    if (isHome || isOther) link.classList.add("active");
  });

  /* ---- Mobile Menu ---- */
  const hamburger = document.getElementById("hamburger");
  const mobileMenu = document.getElementById("mobile-menu");
  if (hamburger && mobileMenu) {
    hamburger.addEventListener("click", () => {
      const isOpen = !mobileMenu.hidden;
      mobileMenu.hidden = isOpen;
      hamburger.setAttribute("aria-expanded", String(!isOpen));
    });
    // Close on link click
    mobileMenu.querySelectorAll(".nav-link").forEach((link) => {
      link.addEventListener("click", () => {
        mobileMenu.hidden = true;
        hamburger.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* ---- Dark / Light Theme Toggle ---- */
  const themeBtn = document.getElementById("theme-toggle");
  const html = document.documentElement;
  const savedTheme = localStorage.getItem("theme") || "dark";
  html.setAttribute("data-theme", savedTheme);

  if (themeBtn) {
    themeBtn.addEventListener("click", () => {
      const current = html.getAttribute("data-theme");
      const next = current === "dark" ? "light" : "dark";
      html.setAttribute("data-theme", next);
      localStorage.setItem("theme", next);
    });
  }

  /* ---- Typing Animation ---- */
  const typingEl = document.getElementById("typing-text");
  const roles = window.typingRoles || [];
  if (typingEl && roles.length) {
    let roleIdx = 0, charIdx = 0, deleting = false;
    const TYPE_SPEED = 80, DELETE_SPEED = 40, PAUSE = 2000;

    function type() {
      const current = roles[roleIdx];
      if (deleting) {
        typingEl.textContent = current.slice(0, --charIdx);
        if (charIdx === 0) {
          deleting = false;
          roleIdx = (roleIdx + 1) % roles.length;
          setTimeout(type, 400);
          return;
        }
        setTimeout(type, DELETE_SPEED);
      } else {
        typingEl.textContent = current.slice(0, ++charIdx);
        if (charIdx === current.length) {
          deleting = true;
          setTimeout(type, PAUSE);
          return;
        }
        setTimeout(type, TYPE_SPEED);
      }
    }
    setTimeout(type, 800);
  }

  /* ---- Scroll-based Fade-in ---- */
  const fadeEls = document.querySelectorAll(".fade-in");
  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry, i) => {
          if (entry.isIntersecting) {
            // Stagger delay for grid children
            const delay = entry.target.closest(".projects-grid, .skills-grid, .stats__grid")
              ? Array.from(entry.target.parentElement.children).indexOf(entry.target) * 80
              : 0;
            setTimeout(() => entry.target.classList.add("visible"), delay);
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.1, rootMargin: "0px 0px -40px 0px" }
    );
    fadeEls.forEach((el) => observer.observe(el));
  } else {
    // Fallback for older browsers
    fadeEls.forEach((el) => el.classList.add("visible"));
  }

  /* ---- Clickable Project Cards ---- */
  document.querySelectorAll(".project-card[data-href]").forEach((card) => {
    card.addEventListener("click", (e) => {
      // Don't navigate if clicking a button/link inside the card
      if (e.target.closest("a, button")) return;
      window.location.href = card.dataset.href;
    });
  });

  /* ---- Project Tech Filter ---- */
  const filterBtns = document.querySelectorAll(".filter-btn");
  const filterEmpty = document.getElementById("filter-empty");
  if (filterBtns.length) {
    filterBtns.forEach((btn) => {
      btn.addEventListener("click", () => {
        filterBtns.forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");

        const filter = btn.dataset.filter;
        const cards = document.querySelectorAll("#projects-grid .project-card");
        let visible = 0;

        cards.forEach((card) => {
          const tags = card.dataset.tags || "";
          const match = filter === "all" || tags.includes(filter);
          card.style.display = match ? "" : "none";
          if (match) visible++;
        });

        if (filterEmpty) filterEmpty.hidden = visible > 0;
      });
    });
  }

  /* ---- Back to Top ---- */
  const backToTop = document.getElementById("back-to-top");
  if (backToTop) {
    window.addEventListener("scroll", () => {
      backToTop.hidden = window.scrollY < 400;
    }, { passive: true });
    backToTop.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  /* ---- Skeleton loading for project cards ---- */
  // Inject skeletons before real cards are visible, remove once images/content settle
  const projectsGrid = document.getElementById("projects-grid") ||
                       document.querySelector(".projects-grid");
  if (projectsGrid) {
    const cards = projectsGrid.querySelectorAll(".project-card");
    cards.forEach((card) => {
      card.classList.add("card-loading");
      // Remove skeleton shimmer once the card's fade-in fires (content is ready)
      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            setTimeout(() => card.classList.remove("card-loading"), 300);
            observer.unobserve(card);
          }
        });
      }, { threshold: 0.1 });
      observer.observe(card);
    });
  }

  /* ---- Alert Close Buttons ---- */
  document.querySelectorAll(".alert-close").forEach((btn) => {
    btn.addEventListener("click", () => {
      btn.closest(".alert")?.remove();
    });
  });

  /* ---- Auto-dismiss alerts ---- */
  setTimeout(() => {
    document.querySelectorAll(".alert").forEach((alert) => {
      alert.style.transition = "opacity 0.4s ease";
      alert.style.opacity = "0";
      setTimeout(() => alert.remove(), 400);
    });
  }, 5000);

})();
