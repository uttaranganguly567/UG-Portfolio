(function(){const t=document.createElement("link").relList;if(t&&t.supports&&t.supports("modulepreload"))return;for(const e of document.querySelectorAll('link[rel="modulepreload"]'))a(e);new MutationObserver(e=>{for(const s of e)if(s.type==="childList")for(const o of s.addedNodes)o.tagName==="LINK"&&o.rel==="modulepreload"&&a(o)}).observe(document,{childList:!0,subtree:!0});function n(e){const s={};return e.integrity&&(s.integrity=e.integrity),e.referrerPolicy&&(s.referrerPolicy=e.referrerPolicy),e.crossOrigin==="use-credentials"?s.credentials="include":e.crossOrigin==="anonymous"?s.credentials="omit":s.credentials="same-origin",s}function a(e){if(e.ep)return;e.ep=!0;const s=n(e);fetch(e.href,s)}})();document.addEventListener("DOMContentLoaded",()=>{u(),v(),g(),h(),f(),b(),A()});function u(){const i=()=>{const t=window.innerWidth<=768;document.documentElement.classList.toggle("device-mobile",t),document.documentElement.classList.toggle("device-desktop",!t)};window.addEventListener("resize",i),i()}function v(){const i=document.getElementById("cursor-dot"),t=document.getElementById("cursor-ring");if(!i||!t)return;if(window.matchMedia("(pointer: coarse)").matches){i.style.display="none",t.style.display="none";return}let n=-100,a=-100,e=-100,s=-100,o=!1;window.addEventListener("mousemove",l=>{n=l.clientX,a=l.clientY,o||(o=!0,i.style.opacity="1",t.style.opacity="1",e=n,s=a),i.style.transform=`translate3d(${n}px, ${a}px, 0) translate(-50%, -50%)`}),document.addEventListener("mouseleave",()=>{o=!1,i.style.opacity="0",t.style.opacity="0"}),document.addEventListener("mouseenter",()=>{o=!0,i.style.opacity="1",t.style.opacity="1"});function c(){o&&(e+=(n-e)*.18,s+=(a-s)*.18,t.style.transform=`translate3d(${e}px, ${s}px, 0) translate(-50%, -50%)`),requestAnimationFrame(c)}requestAnimationFrame(c);const r="a, button, input, textarea, select, .btn-symmetric, .sys-filter-tab, .system-item-card, .sym-card, .arsenal-sym-card, .btn-modal-open, .nav-icon-btn, .modal-close-btn, .conn-item";function d(){document.querySelectorAll(r).forEach(m=>{m.addEventListener("mouseenter",()=>{i.classList.add("cursor-hover"),t.classList.add("cursor-hover")}),m.addEventListener("mouseleave",()=>{i.classList.remove("cursor-hover"),t.classList.remove("cursor-hover")})})}d(),window.addEventListener("mousedown",()=>{t.classList.add("cursor-click")}),window.addEventListener("mouseup",()=>{t.classList.remove("cursor-click")})}function g(){document.querySelectorAll(".sym-card, .system-item-card, .arsenal-sym-card").forEach(t=>{t.addEventListener("mousemove",n=>{const a=t.getBoundingClientRect(),e=n.clientX-a.left,s=n.clientY-a.top;t.style.setProperty("--mouse-x",`${e}px`),t.style.setProperty("--mouse-y",`${s}px`)})})}function h(){const i=document.querySelectorAll(".sys-filter-tab"),t=document.querySelectorAll(".system-item-card");i.forEach(n=>{n.addEventListener("click",()=>{i.forEach(e=>e.classList.remove("active")),n.classList.add("active");const a=n.getAttribute("data-filter");t.forEach(e=>{const s=e.getAttribute("data-category");a==="all"||s===a?(e.style.display="block",e.style.opacity="0",e.style.transform="translateY(12px)",setTimeout(()=>{e.style.transition="opacity 0.25s ease, transform 0.25s ease",e.style.opacity="1",e.style.transform="translateY(0)"},20)):e.style.display="none"})})})}const y={hyperverse:{badge:"⚡ LIGHTSHIFT STUDIO CLIENT FLAGSHIP",title:"HyperVerse — Architecture & Telemetry Pipeline",tagline:"Biomechanics fitness ecosystem powered by Google Gemini Multimodal AI & real-time telemetry.",content:`
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
    `},"convo-capsule":{badge:"🔬 ACADEMIC FINAL YEAR RESEARCH · 4-MEMBER TEAM",title:"Convo Capsule (MoM Generator) — Autonomous Speech AI Pipeline",tagline:"Autonomous audio-to-document pipeline transforming unstructured meeting recordings into structured Minutes of Meeting.",content:`
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
    `},"campus-core":{badge:"🔬 5TH SEMESTER SE PROJECT · 3-MEMBER TEAM",title:"Campus Core — Python Full-Stack Architecture & AI Risk Index",tagline:"High-throughput institutional management platform featuring predictive academic risk analytics.",content:`
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
    `},"legacy-club":{badge:"⚡ LIGHTSHIFT STUDIO CLIENT FLAGSHIP",title:"Legacy Club — Headless E-Commerce & 3D Studio",tagline:"Direct-to-consumer card wraps platform featuring Notion-backed catalog sync and 3D preview physics.",content:`
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
    `}};function f(){const i=document.getElementById("arch-modal-overlay"),t=document.getElementById("modal-content"),n=document.getElementById("modal-close-btn"),a=document.querySelectorAll(".btn-modal-open");if(!i||!t||!n)return;a.forEach(s=>{s.addEventListener("click",o=>{o.preventDefault();const c=s.getAttribute("data-project"),r=y[c];r&&(t.innerHTML=`
          <span class="modal-header-badge">${r.badge}</span>
          <h2 class="modal-title">${r.title}</h2>
          <p class="modal-tagline">${r.tagline}</p>
          ${r.content}
        `,i.classList.add("open"),document.body.style.overflow="hidden")})});function e(){i.classList.remove("open"),document.body.style.overflow=""}n.addEventListener("click",e),i.addEventListener("click",s=>{s.target===i&&e()}),window.addEventListener("keydown",s=>{s.key==="Escape"&&i.classList.contains("open")&&e()})}function b(){const i=document.getElementById("navbar"),t=document.querySelectorAll(".nav-menu .nav-link"),n=document.querySelectorAll("section[id]"),a=document.getElementById("mobile-menu-btn"),e=document.getElementById("nav-menu");window.addEventListener("scroll",()=>{window.scrollY>40?i.classList.add("scrolled"):i.classList.remove("scrolled");let s="";const o=window.scrollY+200;n.forEach(r=>{const d=r.offsetTop,l=r.offsetHeight;o>=d&&o<d+l&&(s=r.getAttribute("id"))}),t.forEach(r=>{r.classList.remove("active"),r.getAttribute("href")===`#${s}`&&r.classList.add("active")}),document.querySelectorAll(".mobile-quick-dock .dock-item").forEach(r=>{r.classList.remove("active"),r.getAttribute("data-dock")===s&&r.classList.add("active")})}),a&&e&&(a.addEventListener("click",o=>{o.stopPropagation(),e.classList.toggle("open"),a.classList.toggle("open")}),e.querySelectorAll("a").forEach(o=>{o.addEventListener("click",()=>{e.classList.remove("open"),a.classList.remove("open")})}),document.addEventListener("click",o=>{i.contains(o.target)||(e.classList.remove("open"),a.classList.remove("open"))}))}function A(){const i=document.getElementById("contact-form"),t=document.getElementById("copy-email-btn");t&&t.addEventListener("click",()=>{navigator.clipboard.writeText("uttaranganguly20@gmail.com").then(()=>{p("Email address copied to clipboard! 📋"),t.innerText="Copied!",setTimeout(()=>t.innerText="Copy",2200)})}),i&&i.addEventListener("submit",n=>{n.preventDefault();const a=document.getElementById("f-name").value.trim(),e=document.getElementById("f-email").value.trim(),s=document.getElementById("f-subject").value.trim(),o=document.getElementById("f-message").value.trim();if(!a||!e||!s||!o){p("Please fill out all transmission fields.");return}p("Transmission initiated! Opening mail client... 🚀");const c=`mailto:uttaranganguly20@gmail.com?subject=${encodeURIComponent(`[Inquiry] ${s}`)}&body=${encodeURIComponent(`Sender: ${a} (${e})

${o}`)}`;setTimeout(()=>{window.location.href=c,i.reset(),p("Direct client launched! ✉️")},600)})}function p(i){const t=document.getElementById("toast-container");if(!t)return;const n=document.createElement("div");n.className="toast",n.innerHTML=`
    <span style="color: var(--neon-cyan);">⚡</span>
    <span>${i}</span>
  `,t.appendChild(n),setTimeout(()=>{n.style.transition="opacity 0.35s ease, transform 0.35s ease",n.style.opacity="0",n.style.transform="translateX(50px)",setTimeout(()=>n.remove(),350)},3500)}
