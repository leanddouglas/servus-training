# Servus Floor Care Training Template
## Master Template Reference for All Future Servus Training Courses

> **Extracted from ALL 6 pages:** course_index.html, day1/index.html, day2/index.html, day3/index.html, day4/index.html, day5/index.html. This document defines every design token, component, pattern, and interaction used across the entire course. All future Servus training courses must follow this template exactly.

---

## Source Repository
- **Repo:** `leanddouglas/servus-training`
- **GitHub Pages:** `https://leanddouglas.github.io/servus-training/`
- **Netlify:** (deployed — see site URL after deployment)
- **Pages:** course_index.html, day1-5/index.html, fiber_identification_printable.html, sop/index.html, burn-test-visual-samples.html
- **Extracted from:** All pages (course index + 5 day pages + SOP reference + printables)

---

## 1. Brand Color Palette (CSS Custom Properties)

| Token | Value | Usage | Source |
|---|---|---|---|
| `--servus-navy` | `#0a4875` | Primary brand, headers, headings | All pages |
| `--servus-navy-dark` | `#062d4a` | Gradient starts, deep backgrounds | Index, Day2-5 |
| `--servus-blue` | `#005a87` | Table headers, borders, secondary | All pages |
| `--servus-blue-mid` | `#006ba1` | Module titles, gradient ends | All pages |
| `--servus-accent` | `#ff9900` | CTAs, accent bars, highlights, buttons | All pages |
| `--servus-accent-glow` | `#ffad33` | Hover state for accent | Index |
| `--servus-light-blue` | `#D3EEF5` | Cert strip background, table hover | All pages |
| `--servus-pale-blue` | `#F0FCFF` | Table even rows, icon backgrounds, open accordion | All pages |
| `--servus-cloud-blue` | `#F2F7FC` | Section backgrounds, callout boxes, walkthrough bg | All pages |
| `--servus-off-white` | `#FAFAFA` | Video container background | Day pages |
| `--servus-dark` | `#313131` | Footer gradient start | Day pages |
| `--servus-text` | `#333333` | Body text | All pages |
| `--servus-text-mid` | `#393939` / `#555555` | Secondary text (day pages / index) | All pages |
| `--servus-text-light` | `#777777` | Meta/label text | Index only |
| `--servus-success` | `#28a745` / `#007bff` | Success states | Index / Day1 |
| `--servus-link` | `#0056b3` | Link color | Day pages |
| `--servus-gradient` | `linear-gradient(135deg, #0a4875 0%, #005a87 50%, #006ba1 100%)` | Primary gradient | All pages |
| `--servus-gradient-dark` | `linear-gradient(135deg, #062d4a 0%, #0a4875 50%, #005a87 100%)` | Dark gradient (hero/header) | All pages |
| `--card-shadow` | `0 4px 24px rgba(10,72,117,0.10)` | Card resting state | Index |
| `--card-hover-shadow` | `0 12px 40px rgba(10,72,117,0.20)` | Card hover state | Index |

### Semantic Colors (not in :root, used inline)

| Color | Usage | Source |
|---|---|---|
| `#e3f2fd` bg / `#1565c0` text | Walkthrough "inspect" step, cat-foundations | Day1-5 |
| `#fff3e0` bg / `#e65100` text | Walkthrough "decide" step, cat-methods, g-cat-spot, g-cat-prof | Day1-5 |
| `#e8f5e9` bg / `#2e7d32` text | Walkthrough "action" step, cat-chemistry, grade-a | Day1-5 |
| `#f3e5f5` bg / `#7b1fa2` text | Walkthrough "complete" step, cat-professional | Day1, Day5 |
| `#fce4ec` bg / `#c62828` text | cat-spotting | Day5 |
| `#4caf50` | Success borders, correct answers | Day1-5 |
| `#e53935` | Error/incorrect answers | Day5 |
| `#ff9800` | Warning/skipped | Day5 |
| `#dc3545` | Pre-existing condition alerts | Day1 (form) |

---

## 2. Font Stack

```css
font-family: 'Myriad Variable Concept', 'Inter', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
line-height: 1.7;
```
- **Google Font load:** `Inter:wght@300;400;500;600;700;800` (days), add `900` for index
- **Course Index variant:** `'Inter', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif` (no Myriad)

---

## 3. Page Structure

### Course Index (Landing Page)
```
<section class="hero"> (full viewport, gradient + grid SVG overlay + bottom fade)
  <div class="hero-content">
    <img class="hero-logo"> (340px, border-radius 16px)
    <div class="hero-division"> ("Specialty Cleaning" uppercase spaced)
    <div class="hero-tagline"> ("At Your Service" italic orange)
    <div class="hero-title-bar"> (80px x 4px orange accent bar)
    <h2> (course title)
    <p class="hero-subtitle">
    <div class="hero-stats"> (flex row of stat cards)
    <a class="hero-cta"> (orange pill button)
  </div>
</section>
<div class="cert-strip">
<section class="about-section reveal">
<section class="outcomes-section"> (.outcomes-grid auto-fit cards)
<section class="curriculum-section">
  <div class="day-cards">
    <a class="day-card reveal"> (3-col grid: day-number / day-info / day-meta)
<section class="instructor-section"> (dark gradient, blockquote)
<section class="features-section"> (icon + text rows)
<section class="final-cta"> (dual CTA buttons)
<footer class="course-footer"> (dark gradient, contact, logos, disclaimer, dev credit)
```

### Day Pages (Content Pages)
```
<div> back-link bar (navy, white back arrow to course_index.html)
<header class="servus-header"> (gradient + grid SVG + bottom fade)
  <img class="hero-logo">
  <div class="hero-division">
  <div class="hero-tagline">
  <div class="accent-bar"> (80px x 4px orange)
  <h2> "Professional Carpet Care Certification"
  <div class="module-label"> (day title, white 85% opacity, text-shadow)
</header>
<div class="cert-strip">
<div class="content"> (max-width: 960px, padding: 30px 40px)
  <h2 class="section-title"> (navy, 3px orange bottom border)
  <h3 class="module-title"> (blue-mid, 4px orange left border)
  <div class="servus-callout">
  <table>
  <div class="video-container">
  <div class="cheat-sheet">
  <div class="walkthrough-container">
  <div class="accordion-item"> (Day 3+)
  <div class="scenario-card"> (Day 2)
  <div class="exam-section"> (Day 5 only)
</div><!-- end .content -->
<div class="glossary-widget">
<div class="servus-footer">
```

---

## 4. Components — By Source Page

### Shared Across All Pages

#### Header (`servus-header`)
- Gradient: `linear-gradient(135deg, #062d4a 0%, #005a87 100%)`
- SVG grid pattern overlay (opacity 0.05, repeating grid)
- Fade-to-white gradient at bottom (150px `::after`)
- Logo: 340px width, 220px on mobile
- Module label: `font-size: 1.2em; color: rgba(255,255,255,0.85); font-weight: 500; text-shadow: 0 1px 3px rgba(0,0,0,0.3);`

#### Certification Strip (`cert-strip`)
- Background: `var(--servus-light-blue)` (#D3EEF5)
- Items: COR logo + IICRC S100 Compliant + WorkSafeBC 2026 + COR Certified + CRI Standards
- Flex layout with bullet dividers, 30px gap

#### Footer (`servus-footer`)
```html
<div class="servus-footer">
    <strong style="font-size: 1.1em;">Servus Group</strong>
    <p style="color: #ccc; margin: 4px 0 12px;">Specialty Cleaning — [Course Name]</p>
    <p style="color: #ccc; margin: 4px 0;"><strong>Contact:</strong> <a href="tel:604-435-1135">604-435-1135</a> | <a href="mailto:info@servusgroup.com">info@servusgroup.com</a></p>
    <p style="color: #ccc; margin: 4px 0;">160-21900 Westminster Hwy, Richmond BC V6V 2K3 | <a href="https://servusgrouplowermainland.com">servusgrouplowermainland.com</a></p>
    <div class="footer-certs">
        <img src="[COR logo]" alt="COR Certified" style="filter: brightness(0) invert(1); opacity: 0.7; height: 40px;">
        <img src="../assets/iicrc-logo.png" alt="IICRC S100 Certified" style="filter: brightness(0) invert(1); opacity: 0.8; height: 38px;">
        <img src="../assets/cri-logo.png" alt="CRI" style="filter: brightness(0) invert(1); opacity: 0.8; height: 38px;">
        <img src="../assets/servus-logo-white.jpg" alt="Servus Group" style="height: 40px; border-radius: 6px;">
    </div>
    <div class="compliance-text" style="font-size: 0.7em; max-width: 700px; margin: 10px auto 0; line-height: 1.4; opacity: 0.6;">[Disclaimer text]</div>
</div>
```
- Dark gradient: `linear-gradient(135deg, var(--servus-dark) 0%, #1a1a2e 100%)`
- Dev credit "Douglas da Silva" — course_index.html ONLY

#### Callout Box (`servus-callout`)
```html
<div class="servus-callout">
    <div class="callout-label">Label Text</div>
    <p>Content text</p>
</div>
```
- Style: cloud-blue bg, 5px navy left border
- Icon approach varies: Day 1 uses `::before` pseudo, Day 2 uses `.servus-callout-label` with inline SVG, Day 3 hides via `.callout-icon { display: none }`, Day 5 hides via `.callout-svg-icon { display: none }`
- **Recommendation for new courses:** Use the Day 2 approach (inline SVG label)

#### Tables
- Header: `background: var(--servus-navy); color: white`
- Rows: `tr:nth-child(even) { background: var(--servus-pale-blue) }`
- Hover: `tr:hover { background: var(--servus-light-blue) }`
- Responsive: `overflow-x: auto` on mobile

#### Glossary Terms (Inline)
```html
<span class="glossary-term">Term Name<span class="tooltip">Definition text.</span></span>
```
- Dotted orange underline, CSS-only hover tooltip
- Tooltip: navy bg, white text, 260px wide, positioned above

#### Connector Text (`connector-text`)
- Pale-blue gradient background, orange 4px left border
- Used for transition text between sections

#### Horizontal Rule (`hr`)
- 3px solid, accent orange (#ff9900)

---

### Course Index Only

| Component | Class(es) | Purpose |
|---|---|---|
| Hero section | `.hero`, `.hero-content` | Full-viewport landing with stats |
| Hero badge | `.hero-badge` | Pill certification badge, orange border |
| Hero CTA | `.hero-cta` | Orange pill button, 50px radius |
| Hero stats | `.hero-stats`, `.stat-item` | Flex row of number+label cards |
| Section labels | `.section-label`, `.section-title`, `.section-bar` | Orange uppercase label + navy heading + accent bar |
| Outcome cards | `.outcomes-grid`, `.outcome-card` | Auto-fit grid of skill cards with icons |
| Day cards | `.day-cards`, `.day-card` | 3-column navigation cards (number/info/meta) |
| Module tags | `.mod-tag` | Pale-blue pill tags for module topics |
| Day number | `.day-number`, `.dn-label`, `.dn-num` | Navy gradient sidebar with day number |
| Day meta | `.day-meta`, `.meta-item` | Module count + terms count with SVG icons |
| Instructor | `.instructor-section`, `.instructor-quote` | Dark gradient section with blockquote |
| Features | `.features-section`, `.feature-item` | Icon + text feature rows |
| CTA buttons | `.cta-primary`, `.cta-secondary` | Orange pill / navy outline pill |
| Scroll reveal | `.reveal`, `.reveal.visible` | Scroll-triggered fade-in (opacity 0, translateY 30px) |

---

### Day 1 (Fiber Identification) — Unique Components

| Component | Class(es) | Purpose |
|---|---|---|
| Cheat sheet | `.cheat-sheet` | Centered image with shadow and border |
| Video container | `.video-container` | Centered iframe embed with off-white bg |
| Pre-inspection form | Interactive HTML form | Field documentation training tool |

---

### Day 2 (Chemistry) — Unique Components

| Component | Class(es) | Purpose |
|---|---|---|
| Scenario cards | `.scenario-card`, `.scenario-header`, `.scenario-toggle`, `.scenario-content` | Collapsible product protocol cards |
| Product steps | `.product-step`, `.product-name` | Numbered steps with orange circle counter via `data-step` |
| Tech tips | `.tech-tip` | Yellow-tinted tip box, orange left border |
| pH scale | `.ph-scale-bar`, `.ph-zone`, `.ph-zone-acid/neutral/alkaline` | Color-coded pH visualization bar |
| Flowchart | `.flowchart-container` | Cloud-blue bordered container for diagrams |
| Back link | `.back-link` | Navy bar with back navigation arrow |

---

### Day 3 (Methods & Equipment) — Unique Components

| Component | Class(es) | Purpose |
|---|---|---|
| Accordion system | `.accordion-section`, `.accordion-item`, `.accordion-label`, `.accordion-toggle`, `.accordion-body`, `.accordion-content` | Expandable/collapsible content sections |

**Accordion CSS detail:**
```css
.accordion-item {
    cursor: pointer; margin-bottom: 12px; padding: 14px 16px;
    background: white; border: 1px solid #d8d8d8;
    border-left: 4px solid var(--servus-navy);
    border-radius: 0 4px 4px 0; transition: all 0.2s;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08);
}
.accordion-item.open {
    background: var(--servus-pale-blue);
    border-left-color: var(--servus-accent);
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}
.accordion-toggle {
    width: 20px; height: 20px; background: var(--servus-accent);
    color: white; border-radius: 50%; font-weight: 700;
}
.accordion-item.open .accordion-toggle { transform: rotate(180deg); }
.accordion-body { max-height: 0; overflow: hidden; transition: max-height 0.3s ease; }
.accordion-item.open .accordion-body { max-height: 2000px; }
```
**JS:** `onclick="this.classList.toggle('open')"`

---

### Day 4 (Spotting & Stains) — Unique Components

| Component | Class(es) | Purpose |
|---|---|---|
| Content wrapper | `.content-wrapper` | Z-index stacking context wrapper |
| Glossary: Spotting | `.g-cat-spot` | Orange badge for spotting terms (`#fff3e0` / `#e65100`) |

---

### Day 5 (Professionalism & Certification) — Unique Components

#### Glossary Category
| Component | Class | Colors |
|---|---|---|
| Professional terms | `.g-cat-prof` | `#fff3e0` bg / `#e65100` text |

#### Exam System (Complete)

| Component | Class(es) | Purpose |
|---|---|---|
| Exam container | `.exam-section` | Pale-blue bg, navy left border, wrapper |
| Progress bar | `.exam-progress-bar`, `.exam-progress-fill`, `.exam-progress-text` | Orange gradient animated fill bar |
| Section nav | `.exam-section-nav`, `.section-nav-btn`, `.nav-score` | Pill buttons to filter by day/topic |
| Question cards | `.exam-question`, `.q-number`, `.q-category` | Cards with numbered badges and topic tags |
| Question states | `.exam-question.answered/correct/incorrect/skipped` | Border-left color changes per state |
| Category badges | `.cat-foundations` (blue), `.cat-chemistry` (green), `.cat-methods` (orange), `.cat-spotting` (red), `.cat-professional` (purple) | Color-coded topic labels |
| Answer styling | `.exam-question label`, `input[type="radio"]` | Hover highlight, accent-color navy |
| Correct indicator | `.correct-indicator`, `.correct-indicator.right/wrong` | Show/hide checkmark or X after grading |
| Submit button | `.exam-submit-area`, `.exam-submit-btn`, `.unanswered-warning` | Navy gradient, accent border, disabled state |

#### Results Dashboard (Day 5 Only)

| Component | Class(es) | Purpose |
|---|---|---|
| Results container | `.results-dashboard` | Hidden until submit, fadeInUp animation |
| Score hero | `.score-hero`, `.score-hero.pass/fail`, `.score-big`, `.score-fraction`, `.score-message` | Green (pass) or red (fail) gradient hero with animated score |
| Stats grid | `.stats-grid`, `.stat-card`, `.stat-number`, `.stat-label` | 4-column grid: correct/incorrect/skipped/total |
| Stat colors | `.stat-number.green/red/orange/blue` | Color-coded stat numbers |
| Section breakdown | `.section-breakdown`, `.section-row`, `.section-icon`, `.section-info`, `.section-name`, `.section-bar-bg`, `.section-bar-fill`, `.section-score-label`, `.section-grade` | Per-topic score bars with animated fill |
| Letter grades | `.grade-a` (green), `.grade-b` (blue), `.grade-c` (orange), `.grade-f` (red) | Grade badges |
| Recommendations | `.recommendations`, `.rec-item`, `.rec-icon`, `.rec-content`, `.rec-title`, `.rec-desc` | Prioritized study tips |
| Rec priorities | `.rec-item.priority-high` (red), `.priority-med` (orange), `.priority-low` (green) | Color-coded urgency |
| Certificate card | `.cert-card`, `.cert-subtitle`, `.cert-divider`, `.cert-title`, `.cert-detail`, `.cert-score-badge` | Navy-blue gradient card with diagonal stripes, accent border |
| Retry button | `.retry-btn` | Orange gradient, uppercase |
| Question map | `.question-map`, `.q-dot`, `.q-dot.correct/incorrect/skipped` | Grid of colored squares for at-a-glance review |

---

## 5. Glossary Category Badges — All Days

| Badge Class | Day(s) | Topic | Background | Text Color |
|---|---|---|---|---|
| `.g-cat-fiber` | Day 1 | Fiber types | `#e3f2fd` | `#1565c0` |
| `.g-cat-tech` | Day 1, 2 | Technical | `#fff3e0` | `#e65100` |
| `.g-cat-test` | Day 1 | Testing | `#f3e5f5` | `#7b1fa2` |
| `.g-cat-chem` | Day 2, 3 | Chemistry | `#e8f5e9` | `#2e7d32` |
| `.g-cat-safe` | Day 2, 3 | Safety | `#fce4ec` | `#c62828` |
| `.g-cat-spot` | Day 4 | Spotting | `#fff3e0` | `#e65100` |
| `.g-cat-prof` | Day 5 | Professional | `#fff3e0` | `#e65100` |

---

## 6. Walkthrough Engine (Day 1, Day 2, Day 4)

- Container: `.walkthrough-container` (cloud-blue bg, 2px blue border, 12px radius)
- Header: `.wt-header` (navy gradient, step counter pill)
- Breadcrumbs: `.wt-crumb` states: `.completed` (green), `.current` (orange pulsing), `.locked` (gray)
- Step card: `.wt-step-card` with slideIn animation
- Step types with color coding:
  - **inspect** — `#e3f2fd` bg, `#1565c0` text (blue)
  - **decide** — `#fff3e0` bg, `#e65100` text (orange)
  - **action** — `#e8f5e9` bg, `#2e7d32` text (green)
  - **complete** — `#f3e5f5` bg, `#7b1fa2` text (purple)
- Choice buttons: `.wt-choice-btn.yes` (green border) / `.wt-choice-btn.no` (red border)
- Continue: `.wt-continue-btn` (navy gradient, orange border)
- History: `.wt-history-item` (white card, green left border)
- Result: `.wt-result` (green gradient, checkmark)
- Restart: `.wt-restart-btn` (orange bg)
- JS: Step-based state machine with decision tree data, `getSvgIcon()` factory

---

## 7. Animations & Keyframes

| Name | Definition | Used In |
|---|---|---|
| `fadeInDown` | opacity 0 + translateY(-20px) → visible | Index hero |
| `fadeInUp` | opacity 0 + translateY(20px) → visible | Index hero, Day 5 results |
| `expandBar` | width 0 → 80px | Index title bar |
| `pulse` | box-shadow glow 0→6px→0 (orange) | Walkthrough current crumb |
| `slideIn` | opacity 0 + translateY(20px) → visible | Walkthrough steps, history |
| `countUp` | opacity 0 + scale(0.5) → visible + scale(1) | Day 5 score number |
| `slideRight` | width 0% → actual | Day 5 score bars |
| `.reveal` → `.visible` | opacity 0 + translateY(30px) → visible (scroll-triggered) | Index sections |

---

## 8. Interactive JS Patterns

- **Scroll reveal** (Index): getBoundingClientRect check on scroll, toggles `.visible`
- **Smooth scroll** (Index): `a[href^="#"]` → `scrollIntoView({ behavior: 'smooth' })`
- **Walkthrough engine** (Day 1, 2, 4): Step-based state machine with decision tree data, SVG icon factory via `getSvgIcon()`
- **Glossary** (All days): `toggleGlossary()`, `filterG(cat, btn)`, `searchGlossary(query)` — DOM manipulation
- **Accordion** (Day 3+): `onclick="this.classList.toggle('open')"` — CSS max-height transition
- **Scenario cards** (Day 2): `toggleScenario(header)` — similar accordion pattern
- **Exam engine** (Day 5): `filterSection()`, `submitExam()`, `retryExam()` — grading logic, results dashboard generation
- **Scroll restoration** (All days): `history.scrollRestoration = 'manual'; window.scrollTo(0, 0);`
- **Mermaid.js** (Day 1 only): ES module from CDN, themed to brand colors

---

## 9. Responsive Breakpoints

| Breakpoint | Changes |
|---|---|
| **768px** | Reduced header padding (50px 20px 40px), smaller logo (220px), smaller h2 (1.3em), walkthrough choices stack vertically, glossary panel full-width, day-card 2-column (80px + 1fr), footer logo goes static, exam stats grid → 2x2 |
| **480px** (Index) | Further hero compression, min-height auto, tighter section padding |

---

## 10. Print Styles

```css
@media print {
    body { max-width: 100%; padding: 0; }
    .servus-header, .servus-footer, .cert-strip {
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }
    .walkthrough-container, table, .servus-callout,
    .cheat-sheet, .accordion-item, .scenario-card, hr {
        page-break-inside: avoid;
    }
    .glossary-widget { display: none; }
    .hero { min-height: auto; padding: 40px 20px; }
    .hero::after { display: none; }
    .day-card { break-inside: avoid; box-shadow: none; border: 1px solid #ddd; }
}
```

---

## 11. Assets (in /assets/ folder)

| File | Purpose |
|---|---|
| `servus-cleaning-logo-colour.jpg` | Color logo with "Cleaning" descriptor |
| `servus-cleaning-logo-white.jpg` | White logo for dark backgrounds |
| `servus-logo-colour.jpg` | Logo without "Cleaning" descriptor |
| `servus-logo-white.jpg` | White version without descriptor |
| `iicrc-logo.png` | IICRC certification logo (from iicrc.org) |
| `cri-logo.png` | CRI Carpet & Rug Institute logo (from carpet-rug.org) |
| COR logo | Hosted externally: `servusgrouplowermainland.com/wp-content/uploads/2014/07/go2HR-CORLogo-K-300x283.png` |

---

## 12. Standardized Contact Info

- **Company:** Servus Group
- **Division:** Specialty Cleaning
- **Tagline:** "At Your Service"
- **Phone:** 604-435-1135
- **Email:** info@servusgroup.com
- **Address:** 160-21900 Westminster Hwy, Richmond BC V6V 2K3
- **Website:** servusgrouplowermainland.com
- **Dev credit:** Douglas da Silva (course_index only)
- **Certifications shown:** COR, IICRC S100, WorkSafeBC 2026, CRI Standards
- **NOT shown:** ISSA Canada (removed — not confirmed certified)

---

## 13. SOP (Standard Operating Procedures) System

### Overview
- **14 SOPs** numbered 001–014 across 5 training days
- **5 Categories:** Forms, Protocols, Decision Trees, Procedures, Checklists
- **SOP Color:** `#014870` (solid navy header, white text)
- **Dedicated SOP page:** `sop/index.html` (standalone reference)
- **SOP card in Training Roadmap** (course_index.html, after Day 5)

### SOP Banner Component (Per Day Page)
```css
.sop-system-card { border: 1.5px solid #014870; border-radius: 10px; overflow: hidden; margin-bottom: 24px; background: #f8fafc; }
.sop-system-card-header { background: #014870; color: white; padding: 10px 18px; display: flex; align-items: center; gap: 10px; }
.sop-chip { color: #014870; ... } /* Clickable <a href="#sop-XXX"> */
.sop-chip-num { background: #014870; color: white; ... }
.sop-section-tag { color: #014870; background: #e8f2f8; border: 1px solid #c5d9e6; ... } /* Discreet inline marker at each SOP location */
```

### SOP Anchor System
Each SOP content section has `id="sop-XXX"` for anchor navigation:
| SOP | Name | Day | Anchor Location |
|---|---|---|---|
| SOP-001 | Pre-Inspection Documentation | Day 1 | Pre-Inspection Form heading |
| SOP-002 | Burn Test Protocol | Day 1 | Burn Test Walkthrough heading |
| SOP-003 | 8-Step Cleaning Protocol | Day 2 | Module 8 heading |
| SOP-004 | Rinse & Neutralization | Day 2 | Module 5 heading |
| SOP-005 | HWE Setup & Operation | Day 3 | Module 1 heading |
| SOP-006 | Pre-Run Equipment Checklist | Day 3 | Pre-Run Checklist accordion |
| SOP-007 | Encapsulation (Whittaker) | Day 3 | Whittaker TRIO h3 |
| SOP-008 | Method Selection Decision Tree | Day 3 | Module 5 heading |
| SOP-009 | Spot vs Stain Classification | Day 4 | Module 1 heading |
| SOP-010 | Red Stain Emergency (Red Relief) | Day 4 | Module 4 heading |
| SOP-011 | Pet Damage Assessment | Day 4 | Module 3 heading |
| SOP-012 | Equipment Maintenance Schedule | Day 5 | Equipment Maintenance accordion |
| SOP-013 | Safety & WHMIS Compliance | Day 5 | Module 2 heading |
| SOP-014 | IICRC S100 Reference Guide | Day 5 | IICRC S100 h3 |

### SOP Page Structure (`sop/index.html`)
- Uses full `.servus-header` and `.servus-footer` template
- Stats bar: 14 Total SOPs, 5 Categories, 5 Training Days (orange `#ff9900` numbers)
- SOPs grouped by type with links to day page anchors (e.g., `../day1/#sop-001`)
- Each SOP shows: number badge, name, description, day tag, arrow

### For New Courses
- Number SOPs sequentially (e.g., SOP-015+ for Tile & Grout course)
- Use same SOP banner, chip, and section tag CSS pattern
- Create dedicated `sop/index.html` page following same structure
- Add SOP card to Training Roadmap in course_index.html

---

## 14. SVG Icon Standards

### Design Rules
- **NO emoji** — all icons must be inline SVG
- **Style:** Stroke-based, consistent stroke-width (2 or 2.5)
- **Sizes:** 16–24px depending on context
- **Colors:** Use brand CSS variables or explicit brand colors
- **Alignment:** `vertical-align: -2px` to `-4px` with `margin-right: 4px–6px`

### Color Usage in SVG Icons
| Context | Stroke Color |
|---|---|
| Section headings (navy bg) | `var(--servus-navy)` or `#0a4875` |
| On dark/colored backgrounds | `white` or `rgba(255,255,255,0.7)` |
| On buttons (orange bg) | `white` |
| Status: success/correct | `#4caf50` |
| Status: error/needs work | `#e53935` |
| Status: warning/review | `#ff9800` |
| Accent/highlight | `#ff9900` (filled star for awards) |
| Inside colored containers | `currentColor` (inherits parent color) |

### Common Icon Patterns (Exam Results)
| Icon | Purpose | Key SVG Element |
|---|---|---|
| Grid tiles | Question Map | 4 `<rect>` elements in 2x2 grid |
| Bar chart | Performance | 3 vertical `<line>` elements |
| Clipboard | Recommendations | `<path>` clipboard + `<rect>` paper + `<line>` text |
| Refresh arrows | Retry/Retake | `<polyline>` arrows + `<path>` arc |
| Warning triangle | Unanswered alert | `<path>` triangle + `<line>` exclamation |
| Star polygon | Award/perfect | `<polygon points="12 2 15.09 8.26 22 9.27...">` |
| Check-circle | Good/strong | `<circle>` + `<polyline>` checkmark |
| X-circle | Needs work | `<circle>` + 2 crossing `<line>` elements |
| Alert-circle | Review needed | `<circle>` + `<line>` exclamation |
| Book | Study | `<path>` book spine + page |
| Flask | Chemistry | `<path>` flask shape |
| Gear | Methods | `<circle>` center + `<path>` gear teeth |
| Target | Spotting | 3 concentric `<circle>` elements |
| Trophy | Professional | `<path>` cup + handles + base |
| Building blocks | Foundations | 3 `<rect>` elements of increasing height |

---

## 15. Important Rules for New Courses

1. **NEVER add ISSA** — certification not confirmed
2. **NEVER reference Dry Foam** — not a service Servus offers
3. **Email is `info@servusgroup.com`** — NOT info@servusgrouplowermainland.com
4. **Postal code is `V6V 2K3`** — use consistently
5. **Dev credit only on course_index** — not on day pages
6. **Footer logos use `filter: brightness(0) invert(1)`** — for white appearance on dark bg
7. **Module label style:** `color: rgba(255,255,255,0.85); text-shadow: 0 1px 3px rgba(0,0,0,0.3);`

---

## 16. How to Create a New Course

1. Copy `day1/index.html` as the base template for each day page
2. Update `<div class="module-label">` with new course day/title
3. Keep the header, cert-strip, and footer structure identical
4. Replace content between `<div class="content">` and `</div><!-- end .content -->`
5. Use the h2/h3/accordion/callout/table patterns documented above
6. Create course-specific glossary terms (new category badge colors as needed)
7. Build walkthrough scenarios relevant to the new topic
8. Add exam section on the final day (copy Day 5 exam structure)
9. Copy `course_index.html` and update hero stats, day cards, and outcomes
10. Create SOPs for the new course (see Section 13) — use same banner/chip/tag CSS
11. Create dedicated `sop/index.html` page and add SOP card to Training Roadmap
12. **Use inline SVG icons ONLY** — never use emoji (see Section 14)
13. Deploy to GitHub Pages and/or Netlify
14. Keep ALL branding, colors, fonts, and footer identical

---

*This template was extracted from ALL 6 pages of the Servus Professional Carpet Cleaning Training Course, April 2026. It serves as the master reference for all future Servus Group training courses.*
