---
applyTo: "**"
---

# General Instructions

## No Simple Browser

Never use the Simple Browser or `open_simple_browser` to preview the application. When running the app, just start it and confirm it's running — do not open any browser preview.

## Design Guide

Apple-inspired minimalism. Typography-driven, monochromatic, generous whitespace. No emoji in the UI. Light theme only.

### Color Palette

CSS variables defined in `app/static/css/app.css`:

| Variable                 | Value                    | Usage                         |
| ------------------------ | ------------------------ | ----------------------------- |
| `--color-bg`             | `#FFFFFF`                | Page background               |
| `--color-surface`        | `#F5F5F7`                | Card/section backgrounds      |
| `--color-text`           | `#1D1D1F`                | Primary text                  |
| `--color-text-secondary` | `#86868B`                | Secondary/muted text          |
| `--color-accent`         | `#1D1D1F`                | Buttons, interactive elements |
| `--color-border`         | `rgba(0,0,0,0.08)`       | Subtle separators             |
| `--color-marked`         | `#E8F5E9`                | Marked bingo squares          |
| `--color-marked-check`   | `#34C759`                | Checkmark icon                |
| `--color-winning`        | `#FFF8E1`                | Winning line highlight        |
| `--color-overlay`        | `rgba(255,255,255,0.72)` | Frosted glass overlays        |

### Typography

- Font: Satoshi (loaded from FontShare) with system fallbacks
- Scale: 13px caption / 15px body / 17px subhead / 22px title / 34px large title / 48px display
- Headings: weight 700, letter-spacing `-0.02em`
- Body: weight 400, buttons: weight 500

### Spacing & Shape

- Generous whitespace — let content breathe
- Cards and squares: `border-radius: 12px`
- CTA buttons: pill shape (`border-radius: 980px`), black bg, white text

### Depth

- No visible borders — use inset box-shadows (`0 0 0 1px rgba(0,0,0,0.06)`)
- Frosted glass overlays: `backdrop-filter: blur(20px) saturate(180%)`
- Minimal shadows only where needed

### Motion

- Easing: `cubic-bezier(0.25, 0.1, 0.25, 1)` (Apple curve)
- Page load: staggered `fadeIn` (opacity + translateY) with 100ms delay increments
- Modals: `scaleIn` (scale 0.95→1 + opacity)
- Button press: `transform: scale(0.97)` on `:active`
- No bouncy or playful animations

### Principles

- No emoji in the UI — use typography and whitespace instead
- Monochromatic — black accent, not blue
- Mobile-first with large touch targets
- Light theme only (no dark mode)
