# Servus Floor Care Training Template
## Master Template Reference for All Future Servus Training Courses

> This document defines the design system, page structure, and component library extracted from the Servus Professional Carpet Cleaning Training Course (5-day + course index). All future Servus training courses should follow this template exactly.

---

## Source Repository
- **Repo:** `leanddouglas/servus-training`
- **Live:** `https://leanddouglas.github.io/servus-training/`
- **Pages:** course_index.html, day1-5/index.html, fiber_identification_printable.html

---

## 1. Brand Color Palette

| Token | Value | Usage |
|---|---|---|
| `--servus-navy` | `#0a4875` | Primary brand, headers, headings |
| `--servus-navy-dark` | `#062d4a` | Gradient starts, footer |
| `--servus-blue` | `#005a87` | Table headers, borders |
| `--servus-blue-mid` | `#006ba1` | Module titles, gradient ends |
| `--servus-accent` | `#ff9900` | CTAs, accent bars, highlights, buttons |
| `--servus-accent-glow` | `#ffad33` | Hover state for accent |
| `--servus-light-blue` | `#D3EEF5` | Cert strip background |
| `--servus-pale-blue` | `#F0FCFF` | Table even rows, icon backgrounds |
| `--servus-cloud-blue` | `#F2F7FC` | Section backgrounds, callout boxes |
| `--servus-off-white` | `#FAFAFA` | Video containers |
| `--servus-dark` | `#313131` | Footer gradient start |
| `--servus-text` | `#333333` | Body text |
| `--servus-text-mid` | `#393939` | Secondary text |

## 2. Font Stack

```css
font-family: 'Myriad Variable Concept', 'Inter', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
line-height: 1.7;
```
Google Fonts: `Inter:wght@300;400;500;600;700;800`

## 3. Page Structure

### Course Index (Landing Page)
```
hero (full viewport, gradient + grid SVG overlay + bottom fade)
  hero-logo (340px, border-radius 16px)
  hero-division ("Specialty Cleaning" uppercase spaced)
  hero-tagline ("At Your Service" italic orange)
  hero-title-bar (80px x 4px orange)
  h2 title
  hero-stats (flex row of stat cards)
  hero-cta (orange pill button)
cert-strip (light-blue bar with certification logos)
about-section (section-label + section-title + section-bar)
outcomes-grid (auto-fit cards, min 240px)
curriculum-section
  day-cards (vertical flex, 3-col grid: number / info / meta)
instructor-section (dark gradient, blockquote)
features-section (icon + text rows)
final-cta (dual buttons)
course-footer (dark gradient, contact info, cert logos, disclaimer, dev credit)
```

### Day Pages (Content Pages)
```
back-link bar (navy, white back arrow to course_index.html)
servus-header (gradient + grid SVG + bottom fade)
  hero-logo, hero-division, hero-tagline
  accent-bar (80px x 4px orange)
  h2 "Professional Carpet Care Certification"
  module-label (day title, white 85% opacity, text-shadow)
cert-strip (COR logo + IICRC S100 + WorkSafeBC 2026 + COR Certified + CRI Standards)
content (max-width: 960px, padding: 30px 40px)
  h2.section-title (navy, 3px orange bottom border)
  h3.module-title (blue-mid, 4px orange left border)
  .servus-callout (cloud-blue, 5px navy left border, wrench icon)
  tables (navy header, alternating pale-blue rows)
  .video-container (centered embed)
  .cheat-sheet (centered image with shadow)
  .walkthrough-container (interactive step engine)
  .accordion-item (collapsible sections)
glossary-widget (fixed bottom-right, 48px navy circle, expandable panel)
servus-footer (dark gradient, contact info, 4 cert logos, compact disclaimer)
```

## 4. Key Components

### Header
- Gradient: `linear-gradient(135deg, #062d4a 0%, #005a87 100%)`
- SVG grid pattern overlay (opacity 0.05)
- Fade-to-white gradient at bottom (150px)
- Logo: 340px width, 220px on mobile

### Certification Strip
- Background: `var(--servus-light-blue)` (#D3EEF5)
- Items: COR logo + IICRC S100 Compliant + WorkSafeBC 2026 + COR Certified + CRI Standards
- Flex layout with bullet dividers

### Footer (Standardized)
```html
<div class="servus-footer">
    <strong>Servus Group</strong>
    <p>Specialty Cleaning -- [Course Name]</p>
    <p>Contact: 604-435-1135 | info@servusgroup.com</p>
    <p>160-21900 Westminster Hwy, Richmond BC V6V 2K3 | servusgrouplowermainland.com</p>
    <div class="footer-certs">
        COR logo (inverted) | IICRC logo (inverted) | CRI logo (inverted) | Servus logo
    </div>
    <div class="compliance-text" style="font-size:0.7em; max-width:700px; opacity:0.6;">
        [Course-specific disclaimer]
    </div>
</div>
```

### Accordion
```html
<div class="accordion-item">
    <div class="accordion-label">
        <span>Title</span>
        <span class="accordion-toggle">+</span>
    </div>
    <div class="accordion-body">
        <div class="accordion-content">
            [Content]
        </div>
    </div>
</div>
```

### Walkthrough Engine
- Container: `.walkthrough-container` (cloud-blue bg, 2px blue border, 12px radius)
- Header: `.wt-header` (navy gradient, step counter pill)
- Breadcrumbs: `.wt-crumb` (completed=green, current=orange pulsing, locked=gray)
- Step types: inspect (blue), decide (orange), action (green), complete (purple)
- Choice buttons: `.wt-choice-btn.yes` (green) / `.wt-choice-btn.no` (red)
- History tracking with `.wt-history-item`
- Result card: `.wt-result` (green gradient, checkmark)

### Glossary Widget
- Fixed bottom-right, z-index 9999
- Toggle: 48px navy circle with orange border, badge count
- Panel: 340px wide, 480px max-height
- Search + category filter pills
- Terms: name, pronunciation, category badge, definition
- Category badges color-coded per course topic

### Callout Box
```html
<div class="servus-callout">
    <div class="callout-label">Label Text</div>
    <p>Content text</p>
</div>
```
Style: cloud-blue bg, 5px navy left border, wrench icon via ::before

### Tables
- Header: navy bg, white text
- Rows: alternating white/pale-blue
- Hover: light-blue highlight
- Responsive: overflow-x auto on mobile

## 5. Interactive JS Patterns

- **Scroll reveal:** IntersectionObserver on `.reveal` elements
- **Smooth scroll:** `scrollIntoView({ behavior: 'smooth' })`
- **Walkthrough:** Step-based state machine with decision trees
- **Glossary:** Toggle, filter, search functions
- **Accordion:** Max-height transition toggle
- **Scroll restoration:** `history.scrollRestoration = 'manual'`

## 6. Responsive Breakpoints

- **768px:** Reduced header padding, smaller logo (220px), stacked layouts
- **480px:** Further compression, min-height auto

## 7. Print Styles

- Preserve header/footer colors
- Hide glossary widget
- Avoid page breaks inside tables, callouts, accordions
- Max-width 100%, no padding

## 8. Assets (in /assets/ folder)

- `servus-cleaning-logo-colour.jpg` - Color logo
- `servus-cleaning-logo-white.jpg` - White logo for dark backgrounds
- `servus-logo-colour.jpg` - Logo without "Cleaning" descriptor
- `servus-logo-white.jpg` - White version without descriptor
- `iicrc-logo.png` - IICRC certification logo
- `cri-logo.png` - CRI (Carpet & Rug Institute) logo
- COR logo: hosted at `servusgrouplowermainland.com/wp-content/uploads/2014/07/go2HR-CORLogo-K-300x283.png`

## 9. Standardized Contact Info

- **Company:** Servus Group
- **Division:** Specialty Cleaning
- **Phone:** 604-435-1135
- **Email:** info@servusgroup.com
- **Address:** 160-21900 Westminster Hwy, Richmond BC V6V 2K3
- **Website:** servusgrouplowermainland.com

## 10. How to Create a New Course

1. Copy the day page HTML template (use day1/index.html as base)
2. Update the module-label with new course day/title
3. Replace content sections (keep h2/h3/accordion/callout patterns)
4. Create course-specific glossary terms for the widget
5. Build walkthrough scenarios relevant to new topic
6. Create a course_index.html landing page (copy and update)
7. Keep all branding, colors, fonts, and footer identical
8. Add to the same GitHub Pages repo under a new folder

---

*This template was extracted from the Servus Professional Carpet Cleaning Training Course, April 2026. It serves as the master reference for all future Servus Group training courses.*
