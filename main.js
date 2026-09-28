/* ==========================================================================
   UTTARAN GANGULY — SYMMETRICAL ARCHITECTURAL JAVASCRIPT
   Features: Spotlight Card Borders, Project Category Filters,
             Architecture Deep-Dive Modal, Copy Email & Form Dispatcher
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initDeviceAdaptation();
  initCyberCursor();
  initCardPhysicsAndSpotlight();
  initSystemFilters();
  initArchitectureModal();
  initNavigationScrollSpy();
  initScrollReveals();
  initNumberCounters();
  initScrollToTopHUD();
  initContactUtilities();
});

/* ==========================================================================
   -1. RESPONSIVE DEVICE ADAPTATION
   ========================================================================== */
function initDeviceAdaptation() {
  const checkDevice = () => {
    const isMobile = window.innerWidth <= 768;
    document.documentElement.classList.toggle('device-mobile', isMobile);
    document.documentElement.classList.toggle('device-desktop', !isMobile);
  };
  window.addEventListener('resize', checkDevice);
  checkDevice();
}

/* ==========================================================================
   0. CUSTOM CYBERNETIC CURSOR (ANIMATED & THEMED)
   ========================================================================== */
function initCyberCursor() {
  const dot = document.getElementById('cursor-dot');
  const ring = document.getElementById('cursor-ring');

  if (!dot || !ring) return;

  // On touch/mobile devices, disable the custom cursor
  if (window.matchMedia('(pointer: coarse)').matches) {
    dot.style.display = 'none';
    ring.style.display = 'none';
    return;
  }

  let mouseX = -100;
  let mouseY = -100;
  let ringX = -100;
  let ringY = -100;
  let isVisible = false;

  window.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;

    if (!isVisible) {
      isVisible = true;
      dot.style.opacity = '1';
      ring.style.opacity = '1';
      ringX = mouseX;
      ringY = mouseY;
    }

    dot.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0) translate(-50%, -50%)`;
  });

  document.addEventListener('mouseleave', () => {
    isVisible = false;
    dot.style.opacity = '0';
    ring.style.opacity = '0';
  });

  document.addEventListener('mouseenter', () => {
    isVisible = true;
    dot.style.opacity = '1';
    ring.style.opacity = '1';
  });

  // Smooth lerp loop for the cybernetic ring
  function renderCursor() {
    if (isVisible) {
      ringX += (mouseX - ringX) * 0.18;
      ringY += (mouseY - ringY) * 0.18;
      ring.style.transform = `translate3d(${ringX}px, ${ringY}px, 0) translate(-50%, -50%)`;
    }
    requestAnimationFrame(renderCursor);
  }
  requestAnimationFrame(renderCursor);

  // Hover expansion on interactive elements
  const hoverSelectors = 'a, button, input, textarea, select, .btn-symmetric, .sys-filter-tab, .system-item-card, .sym-card, .arsenal-sym-card, .btn-modal-open, .nav-icon-btn, .modal-close-btn, .conn-item';
  
  function attachHoverListeners() {
    const targets = document.querySelectorAll(hoverSelectors);
    targets.forEach((el) => {
      el.addEventListener('mouseenter', () => {
        dot.classList.add('cursor-hover');
        ring.classList.add('cursor-hover');
      });
      el.addEventListener('mouseleave', () => {
        dot.classList.remove('cursor-hover');
        ring.classList.remove('cursor-hover');
      });
    });
  }
  attachHoverListeners();

  // Burst effect on mousedown
  window.addEventListener('mousedown', () => {
    ring.classList.add('cursor-click');
  });
  window.addEventListener('mouseup', () => {
    ring.classList.remove('cursor-click');
  });
}

/* ==========================================================================
   1. CARD PHYSICS: SPOTLIGHT RADIAL GLOW & 3D GYROSCOPIC TILT
   ========================================================================== */
function initCardPhysicsAndSpotlight() {
  const cards = document.querySelectorAll('.sym-card, .system-item-card, .arsenal-sym-card, .metric-hud-card');
  const isTouch = window.matchMedia('(pointer: coarse)').matches;

  cards.forEach((card) => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      // Update spotlight radial glow position
      card.style.setProperty('--mouse-x', `${x}px`);
      card.style.setProperty('--mouse-y', `${y}px`);

      // On fine-pointer desktop, add subtle 3D gyroscopic tilt
      if (!isTouch) {
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        const rotateX = ((y - centerY) / centerY) * -5; // max 5deg
        const rotateY = ((x - centerX) / centerX) * 5;

        card.style.transform = `perspective(1000px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg) translateZ(6px)`;
      }
    });

    card.addEventListener('mouseleave', () => {
      if (!isTouch) {
        card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateZ(0px)';
      }
    });
  });
}

/* ==========================================================================
   2. SYSTEM CATEGORY FILTER TABS
   ========================================================================== */
function initSystemFilters() {
  const tabs = document.querySelectorAll('.sys-filter-tab');
  const cards = document.querySelectorAll('.system-item-card');

  tabs.forEach((tab) => {
    tab.addEventListener('click', () => {
      tabs.forEach((t) => t.classList.remove('active'));
      tab.classList.add('active');

      const filter = tab.getAttribute('data-filter');

      cards.forEach((card) => {
        const cat = card.getAttribute('data-category');
        if (filter === 'all' || cat === filter) {
          card.style.display = 'block';
          card.style.opacity = '0';
          card.style.transform = 'translateY(12px)';
          setTimeout(() => {
            card.style.transition = 'opacity 0.25s ease, transform 0.25s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          }, 20);
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

/* ==========================================================================
   3. ARCHITECTURE DEEP-DIVE MODAL SPECIFICATIONS
   ========================================================================== */
const projectDetails = {
  hyperverse: {
    badge: '⚡ LIGHTSHIFT STUDIO CLIENT FLAGSHIP',
    title: 'HyperVerse — Architecture & Telemetry Pipeline',
    tagline: 'Biomechanics fitness ecosystem powered by Google Gemini Multimodal AI & real-time telemetry.',
    content: `
      <div class="modal-section-title">🤖 Multimodal AI Coaching Architecture</div>
      <p>
        HyperVerse integrates Google's Gemini Multimodal AI engine with a specialized system prompt modeling head coach Carlos Andrei's 14+ years of biomechanics expertise. The engine injects active member telemetry (streak status, lean body mass, personal records, recovery scores) into prompt context for personalized responses.
      </p>

      <div class="pipeline-steps">
        <div class="pipeline-step">
          <div class="step-number">01</div>
          <div class="step-content">
            <h4>Meal Vision Multimodal Analysis</h4>
            <p>Athletes upload meal photos directly to the chat interface. Gemini processes the image along with user dietary constraints, breaking down calories, macronutrients (protein, carbs, fats), ingredient quality scores, and custom feedback in Carlos's coaching tone.</p>
          </div>
        </div>
        <div class="pipeline-step">
          <div class="step-number">02</div>
          <div class="step-content">
            <h4>Universal 9-Language Bidirectional Index</h4>
            <p>Pre-computes a universal bidirectional phrase index covering English, Turkish, Hindi, Russian, Japanese, Chinese, Spanish, French, and RTL Arabic. Allows instant, zero-latency in-memory translation across all 12 platform views without external translation API overhead.</p>
          </div>
        </div>
        <div class="pipeline-step">
          <div class="step-number">03</div>
          <div class="step-content">
            <h4>Telemetry Streak & Decay Engine</h4>
            <p>Implements a strict athletic consistency model: completed workouts automatically advance streaks; up to 2 rest days per week can be declared; unexcused missed days reset streaks to zero and penalize leaderboard power scores.</p>
          </div>
        </div>
        <div class="pipeline-step">
          <div class="step-number">04</div>
          <div class="step-content">
            <h4>Edge Serverless & Webhook Automation</h4>
            <p>Vercel Edge functions listen for Whop payment webhooks to provision instant access across 4 tiers ($24.99–$199). Two automated daily cron jobs trigger Resend API email reminders (8:00 AM workout briefing and 1:00 PM meal logging).</p>
          </div>
        </div>
      </div>

      <div class="modal-section-title">⚙️ Infrastructure & Technology Stack</div>
      <table class="modal-specs-table">
        <tr><th>Layer</th><th>Technology</th><th>Implementation Detail</th></tr>
        <tr><td>Frontend</td><td>React 18 + Vite</td><td>Custom Context Router, Tailwind v4, Responsive SPAs</td></tr>
        <tr><td>AI / Vision</td><td>Google Gemini API</td><td>Multimodal Meal Vision, live member telemetry injection</td></tr>
        <tr><td>Database & Auth</td><td>Firebase</td><td>Realtime Firestore athlete records & authentication</td></tr>
        <tr><td>Monetization</td><td>Whop API</td><td>Webhook-provisioned coaching tiers & VIP channels</td></tr>
        <tr><td>Automation</td><td>Vercel Edge + Resend</td><td>Automated 8am/1pm cron email dispatchers</td></tr>
      </table>
    `
  },

  'convo-capsule': {
    badge: '🔬 ACADEMIC FINAL YEAR RESEARCH · 4-MEMBER TEAM',
    title: 'Convo Capsule (MoM Generator) — Autonomous Speech AI Pipeline',
    tagline: 'Autonomous audio-to-document pipeline transforming unstructured meeting recordings into structured Minutes of Meeting.',
    content: `
      <div class="modal-section-title">🎙️ Autonomous Speech-to-Document Pipeline Architecture</div>
      <p>
        Engineered to eliminate manual transcription and documentation overhead by connecting automatic speech recognition, acoustic speaker clustering, and sequence synthesis into structured Minutes of Meeting.
      </p>

      <div class="pipeline-steps">
        <div class="pipeline-step">
          <div class="step-number">01</div>
          <div class="step-content">
            <h4>Whisper ASR & Multilingual Recognition</h4>
            <p>Meeting audio is processed via OpenAI Whisper models, performing automatic language identification across 90+ languages and transcribing speech into structured text.</p>
          </div>
        </div>
        <div class="pipeline-step">
          <div class="step-number">02</div>
          <div class="step-content">
            <h4>Acoustic Speaker Clustering</h4>
            <p>Partitions audio streams into overlapping temporal segments and performs unsupervised clustering to segregate distinct speaker voices without requiring prior speaker counts.</p>
          </div>
        </div>
        <div class="pipeline-step">
          <div class="step-number">03</div>
          <div class="step-content">
            <h4>Biometric Voiceprint Enrollment</h4>
            <p>Compares acoustic signatures against registered participant profiles. Matches meeting similarity thresholds automatically map utterances to participant identities.</p>
          </div>
        </div>
        <div class="pipeline-step">
          <div class="step-number">04</div>
          <div class="step-content">
            <h4>Temporal Alignment & Attribution</h4>
            <p>Synchronizes word-level timestamps with speech boundaries, attributing each conversational turn to its identified speaker.</p>
          </div>
        </div>
        <div class="pipeline-step">
          <div class="step-number">05</div>
          <div class="step-content">
            <h4>Conversational Text Cleaning</h4>
            <p>Eliminates filler words, conversational pauses, and speech hesitations to produce clean, legible prose suitable for corporate records.</p>
          </div>
        </div>
        <div class="pipeline-step">
          <div class="step-number">06</div>
          <div class="step-content">
            <h4>Action Item & Decision Extraction</h4>
            <p>Analyzes conversational consensus cues to extract approved decisions, assign action items, and register deliverables with assigned stakeholders.</p>
          </div>
        </div>
        <div class="pipeline-step">
          <div class="step-number">07</div>
          <div class="step-content">
            <h4>Hierarchical Abstractive Summarization</h4>
            <p>Processes lengthy conversational transcripts using sequence models, producing concise executive summaries that capture core meeting outcomes.</p>
          </div>
        </div>
        <div class="pipeline-step">
          <div class="step-number">08</div>
          <div class="step-content">
            <h4>Document Structuring & Synthesis</h4>
            <p>Formats output into standardized MoM sections: Meeting Title, Date, Attendees, Agenda, Executive Summary, Decisions Log, and Action Item Table.</p>
          </div>
        </div>
        <div class="pipeline-step">
          <div class="step-number">09</div>
          <div class="step-content">
            <h4>Multi-Format Document Export</h4>
            <p>Generates downloadable files in Microsoft Word (.docx), PDF, and Markdown for seamless distribution to stakeholders.</p>
          </div>
        </div>
      </div>

      <div style="margin-top: 2rem; text-align: center;">
        <a href="https://github.com/uttaranganguly567/Convo-Capsule" target="_blank" rel="noopener noreferrer" class="btn-symmetric btn-purple" style="display: inline-flex; align-items: center; gap: 0.6rem; padding: 0.85rem 1.8rem;">
          <span>Explore Convo-Capsule Repository on GitHub</span>
          <span class="ext-icon">↗</span>
        </a>
      </div>
    `
  },

  'campus-core': {
    badge: '🔬 5TH SEMESTER SE PROJECT · 3-MEMBER TEAM',
    title: 'Campus Core — Python Full-Stack Architecture & AI Risk Index',
    tagline: 'High-throughput institutional management platform featuring predictive academic risk analytics.',
    content: `
      <div class="modal-section-title">⚡ Python & SQLAlchemy Architecture</div>
      <p>
        Built to digitize campus operations across students, faculty, and administrators. Engineered using Python backend services with SQLAlchemy ORM and transactional SQLite storage.
      </p>

      <div class="pipeline-steps">
        <div class="pipeline-step">
          <div class="step-number">01</div>
          <div class="step-content">
            <h4>Predictive AI Academic Risk Index</h4>
            <p>An administrative early-intervention algorithm evaluating three weighted vectors: (1) cumulative GPA decay, (2) strict attendance triggers falling below 75%, and (3) outstanding tuition arrears. Scores classify students into Low, Medium, or High Risk tiers with proactive dashboard alerts.</p>
          </div>
        </div>
        <div class="pipeline-step">
          <div class="step-number">02</div>
          <div class="step-content">
            <h4>Granular Role-Based Access Control (RBAC)</h4>
            <p>Three strictly segregated operational domains: Administrator (directory CRUD, fee auditing, system purging), Faculty (course management, assignment grading), and Student (course enrollment, submissions, financial ledger).</p>
          </div>
        </div>
        <div class="pipeline-step">
          <div class="step-number">03</div>
          <div class="step-content">
            <h4>Dynamic Server-Side UX with HTMX & Jinja2</h4>
            <p>Combines Jinja2 server templates with HTMX attributes to enable single-page dynamic swaps without full browser reloads, styled with a modern glassmorphism aesthetic.</p>
          </div>
        </div>
        <div class="pipeline-step">
          <div class="step-number">04</div>
          <div class="step-content">
            <h4>Zero-Setup Idempotent Database Seeding</h4>
            <p>Automatic database initialization on first launch checks for existing schemas and idempotently seeds default admin, teacher, and student credentials with sample academic ledgers.</p>
          </div>
        </div>
      </div>
    `
  },

  'legacy-club': {
    badge: '⚡ LIGHTSHIFT STUDIO CLIENT FLAGSHIP',
    title: 'Legacy Club — Headless E-Commerce & 3D Studio',
    tagline: 'Direct-to-consumer card wraps platform featuring Notion-backed catalog sync and 3D preview physics.',
    content: `
      <div class="modal-section-title">🎨 Interactive 3D Customizer & Headless Architecture</div>
      <p>
        A bespoke e-commerce application selling custom and catalog decorative wraps for bank cards. Built with HTML5, vanilla JavaScript, and Tailwind CSS with GSAP scroll physics.
      </p>

      <div class="pipeline-steps">
        <div class="pipeline-step">
          <div class="step-number">01</div>
          <div class="step-content">
            <h4>Interactive 3D Card Skin Studio</h4>
            <p>Users upload custom front and back card artwork directly to Cloudinary. The client studio renders a real-time 3D card model featuring realistic tilt physics and glare lighting shaders responding to mouse trajectory.</p>
          </div>
        </div>
        <div class="pipeline-step">
          <div class="step-number">02</div>
          <div class="step-content">
            <h4>Headless Notion Database Catalog Sync</h4>
            <p>Product inventories, categories, and granular promo codes (with MaxUsers caps and expiry dates) are synchronized in real-time with Notion databases, backed by hardcoded fallback arrays for 100% uptime.</p>
          </div>
        </div>
        <div class="pipeline-step">
          <div class="step-number">03</div>
          <div class="step-content">
            <h4>Server-Verified Razorpay Checkout</h4>
            <p>Python serverless functions verify cart prices on the server to prevent client-side manipulation, generate Razorpay orders, and validate HMAC-SHA256 signatures before automatically writing verified orders into Notion.</p>
          </div>
        </div>
        <div class="pipeline-step">
          <div class="step-number">04</div>
          <div class="step-content">
            <h4>Conversion-Optimized Cart Drawer</h4>
            <p>Interactive slide-out drawer featuring a live free-shipping progress indicator (orders above ₹129 get free delivery), instant promo validation, and express shipping add-ons.</p>
          </div>
        </div>
      </div>
    `
  }
};

function initArchitectureModal() {
  const modalOverlay = document.getElementById('arch-modal-overlay');
  const modalContent = document.getElementById('modal-content');
  const closeBtn = document.getElementById('modal-close-btn');
  const triggerBtns = document.querySelectorAll('.btn-modal-open');

  if (!modalOverlay || !modalContent || !closeBtn) return;

  triggerBtns.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const projKey = btn.getAttribute('data-project');
      const data = projectDetails[projKey];

      if (data) {
        modalContent.innerHTML = `
          <span class="modal-header-badge">${data.badge}</span>
          <h2 class="modal-title">${data.title}</h2>
          <p class="modal-tagline">${data.tagline}</p>
          ${data.content}
        `;
        modalOverlay.classList.add('open');
        document.body.style.overflow = 'hidden';
      }
    });
  });

  function closeModal() {
    modalOverlay.classList.remove('open');
    document.body.style.overflow = '';
  }

  closeBtn.addEventListener('click', closeModal);
  modalOverlay.addEventListener('click', (e) => {
    if (e.target === modalOverlay) closeModal();
  });

  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modalOverlay.classList.contains('open')) {
      closeModal();
    }
  });
}

/* ==========================================================================
   4. NAVIGATION SCROLL-SPY & MOBILE MENU
   ========================================================================== */
function initNavigationScrollSpy() {
  const navbar = document.getElementById('navbar');
  const navLinks = document.querySelectorAll('.nav-menu .nav-link');
  const sections = document.querySelectorAll('section[id]');
  const mobileToggle = document.getElementById('mobile-menu-btn');
  const navMenu = document.getElementById('nav-menu');

  const progressBar = document.getElementById('scroll-progress');
  const scrollTopBtn = document.getElementById('hud-scroll-top');
  const orbCyan = document.querySelector('.orb-cyan');
  const orbPurple = document.querySelector('.orb-purple');

  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;

    // 1. Navbar Glassmorph Scrolled State
    if (scrollY > 40) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }

    // 2. Top Scroll Progress Indicator Bar
    if (progressBar) {
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const progress = docHeight > 0 ? (scrollY / docHeight) * 100 : 0;
      progressBar.style.width = `${progress}%`;
    }

    // 3. Floating Back-to-Top HUD Button Visibility
    if (scrollTopBtn) {
      if (scrollY > 380) {
        scrollTopBtn.classList.add('visible');
      } else {
        scrollTopBtn.classList.remove('visible');
      }
    }

    // 4. Subtle Parallax for Ambient Glowing Orbs
    if (orbCyan) {
      orbCyan.style.transform = `translate3d(0, ${scrollY * -0.06}px, 0)`;
    }
    if (orbPurple) {
      orbPurple.style.transform = `translate3d(0, ${scrollY * 0.05}px, 0)`;
    }

    // 5. Active Section Scroll-Spy
    let currentId = '';
    const scrollPos = scrollY + 220;

    sections.forEach((sec) => {
      const top = sec.offsetTop;
      const height = sec.offsetHeight;
      if (scrollPos >= top && scrollPos < top + height) {
        currentId = sec.getAttribute('id');
      }
    });

    navLinks.forEach((link) => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${currentId}`) {
        link.classList.add('active');
      }
    });

    // Synchronize Mobile Floating Quick Dock
    const dockItems = document.querySelectorAll('.mobile-quick-dock .dock-item');
    dockItems.forEach((dock) => {
      dock.classList.remove('active');
      if (dock.getAttribute('data-dock') === currentId) {
        dock.classList.add('active');
      }
    });
  }, { passive: true });

  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', (e) => {
      e.stopPropagation();
      navMenu.classList.toggle('open');
      mobileToggle.classList.toggle('open');
    });

    // Close when clicking any link inside the nav menu
    const allDrawerLinks = navMenu.querySelectorAll('a');
    allDrawerLinks.forEach((link) => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('open');
        mobileToggle.classList.remove('open');
      });
    });

    // Close when clicking outside of navbar
    document.addEventListener('click', (e) => {
      if (!navbar.contains(e.target)) {
        navMenu.classList.remove('open');
        mobileToggle.classList.remove('open');
      }
    });
  }
}

/* ==========================================================================
   5. CONTACT UTILITIES & TOASTS
   ========================================================================== */
function initContactUtilities() {
  const form = document.getElementById('contact-form');
  const copyBtn = document.getElementById('copy-email-btn');

  // Copy Email Button
  if (copyBtn) {
    copyBtn.addEventListener('click', () => {
      const email = 'uttaranganguly20@gmail.com';
      navigator.clipboard.writeText(email).then(() => {
        showToast('Email address copied to clipboard! 📋');
        copyBtn.innerText = 'Copied!';
        setTimeout(() => (copyBtn.innerText = 'Copy'), 2200);
      });
    });
  }

  // Form Submission Mailto Dispatcher
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('f-name').value.trim();
      const email = document.getElementById('f-email').value.trim();
      const subject = document.getElementById('f-subject').value.trim();
      const message = document.getElementById('f-message').value.trim();

      if (!name || !email || !subject || !message) {
        showToast('Please fill out all transmission fields.');
        return;
      }

      showToast(`Transmission initiated! Opening mail client... 🚀`);

      const mailto = `mailto:uttaranganguly20@gmail.com?subject=${encodeURIComponent(
        `[Inquiry] ${subject}`
      )}&body=${encodeURIComponent(`Sender: ${name} (${email})\n\n${message}`)}`;

      setTimeout(() => {
        window.location.href = mailto;
        form.reset();
        showToast('Direct client launched! ✉️');
      }, 600);
    });
  }
}

function showToast(message) {
  const container = document.getElementById('toast-container');
  if (!container) return;

  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.innerHTML = `
    <span style="color: var(--neon-cyan);">⚡</span>
    <span>${message}</span>
  `;

  container.appendChild(toast);

  setTimeout(() => {
    toast.style.transition = 'opacity 0.35s ease, transform 0.35s ease';
    toast.style.opacity = '0';
    toast.style.transform = 'translateX(50px)';
    setTimeout(() => toast.remove(), 350);
  }, 3500);
}

/* ==========================================================================
   6. SCROLL-TRIGGERED REVEAL ANIMATIONS (INTERSECTION OBSERVER)
   ========================================================================== */
function initScrollReveals() {
  const revealElements = document.querySelectorAll('.reveal-on-scroll');
  if (!revealElements.length) return;

  // Immediately reveal elements already near or inside viewport
  const revealIfVisible = (el) => {
    const rect = el.getBoundingClientRect();
    if (rect.top < window.innerHeight * 0.95 && rect.bottom > 0) {
      el.classList.add('revealed');
    }
  };

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          obs.unobserve(entry.target);
        }
      });
    }, {
      root: null,
      threshold: 0.08,
      rootMargin: '0px 0px -40px 0px'
    });

    revealElements.forEach((el) => {
      revealIfVisible(el);
      observer.observe(el);
    });
  } else {
    // Fallback for older browsers
    revealElements.forEach((el) => el.classList.add('revealed'));
  }
}

/* ==========================================================================
   7. HIGH-VELOCITY NUMBER COUNTERS (ROLL ANIMATION ON SCROLL)
   ========================================================================== */
function initNumberCounters() {
  const metricValues = document.querySelectorAll('.metric-hud-val');
  if (!metricValues.length) return;

  let hasAnimated = false;
  const metricsSection = document.getElementById('metrics');

  const startCounters = () => {
    if (hasAnimated) return;
    hasAnimated = true;

    metricValues.forEach((el) => {
      const target = parseInt(el.getAttribute('data-target'), 10) || 0;
      const suffix = el.getAttribute('data-suffix') || '';
      const duration = 1500;
      const startTime = performance.now();

      const updateCount = (currentTime) => {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        // Exponential ease-out
        const ease = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
        const current = Math.floor(ease * target);

        el.textContent = `${current}${suffix}`;

        if (progress < 1) {
          requestAnimationFrame(updateCount);
        } else {
          el.textContent = `${target}${suffix}`;
        }
      };

      requestAnimationFrame(updateCount);
    });
  };

  if (metricsSection && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          startCounters();
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });

    observer.observe(metricsSection);
  } else {
    setTimeout(startCounters, 600);
  }
}

/* ==========================================================================
   8. SCROLL-TO-TOP FLOATING HUD BUTTON
   ========================================================================== */
function initScrollToTopHUD() {
  const btn = document.getElementById('hud-scroll-top');
  if (!btn) return;

  btn.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}

