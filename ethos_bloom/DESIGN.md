# Design System Specification: The Empathic Curatorial

## 1. Overview & Creative North Star
**Creative North Star: The Empathic Curatorial**

This design system is built to move social impact out of the realm of "charity aesthetics" and into the world of high-end editorial prestige. The vision is "The Empathic Curatorial"—an interface that feels like a modern art gallery dedicated to human progress. We achieve this through a "Digital First, Human Always" approach: utilizing generous whitespace (the "breathing room" of luxury), intentional asymmetry to break the rigid bootstrap-grid feel, and sophisticated tonal layering. 

The experience should feel like a series of curated physical layers—vellum, frosted glass, and heavy-stock paper—stacked to create depth without the clutter of traditional UI borders.

---

## 2. Colors & Texture
Our palette balances the urgency of social change with the sophistication of a premium brand.

### The Color Logic
- **Primary (`#b5106a`) & Primary Container (`#d63384`):** Our energetic pulse. Use these for momentum-driven elements and CTAs.
- **Secondary (`#714ca0`):** The intellectual anchor. Use for secondary actions or to cool down high-energy sections.
- **Tertiary (`#785900`):** The "Human Glow." Use sparingly for highlights, testimonials, or "Impact Moments."

### The "No-Line" Rule
Standard 1px borders are strictly prohibited for sectioning. Structural boundaries must be defined solely through background color shifts. To separate a section, transition from `surface` to `surface-container-low`. This creates a seamless, "liquid" flow between content blocks that feels infinitely more premium than a hard-lined grid.

### Surface Hierarchy & Nesting
Treat the UI as a physical stack. 
1. **Base Layer:** `surface` (#fbf8ff)
2. **Structural Sections:** `surface-container-low` (#f4f2ff)
3. **Interactive Cards:** `surface-container-lowest` (#ffffff)
4. **Floating Overlays:** `surface-bright` with Glassmorphism.

### The Glass & Gradient Rule
To avoid a "flat" SaaS appearance, all primary CTAs and Hero backgrounds should utilize a **Signature Texture**: a subtle radial gradient transitioning from `primary` (#b5106a) to `primary-container` (#d63384). For floating navigation or modal headers, use Glassmorphism: `surface-variant` at 70% opacity with a `20px` backdrop-blur.

---

## 3. Typography
The typography strategy is built on a high-contrast scale to create an editorial, magazine-like hierarchy.

- **The Display & Headline Voice (Plus Jakarta Sans):** Chosen for its modern, geometric clarity with a slight "human" curve. Use `display-lg` for impact statements, utilizing `tracking-tighter` (-0.02em) to give it a tight, professional polish.
- **The Functional Voice (Inter):** Chosen for its unparalleled legibility. Used for all body, labels, and titles.
- **Editorial Intent:** Use `headline-lg` in `on_surface` paired immediately with `body-lg` in `on_surface_variant`. This contrast in weight and color creates a sophisticated, curated feel.

---

## 4. Elevation & Depth
Depth is achieved through **Tonal Layering** rather than artificial shadows.

### The Layering Principle
Hierarchy is defined by "The Lift." A card should not just sit on a page; it should emerge from it. Place a `surface-container-lowest` card on a `surface-container-low` background. The subtle shift from a soft lilac-white to a pure white provides all the affordance a user needs without visual noise.

### Ambient Shadows
When an element must float (e.g., a Modal or a hovered Primary Card), use an **Ambient Shadow**:
- **Color:** `#151935` (On Surface) at 6% opacity.
- **Blur/Spread:** `40px` blur, `0px` spread, `12px` Y-offset.
This mimics natural light reflecting off a matte surface, avoiding the "dirty" look of grey shadows.

### The "Ghost Border" Fallback
If accessibility requirements demand a container boundary, use a **Ghost Border**: The `outline-variant` token at **15% opacity**. It should be felt, not seen. Explicitly forbid 100% opaque borders.

---

## 5. Components

### Buttons: The "Momentum" Variant
- **Primary:** Gradient fill (`primary` to `primary-container`), `full` rounded corners, `title-sm` typography (Inter Bold).
- **Secondary:** No fill. Ghost Border (15% `outline-variant`). On hover, transition to `surface-container-high`.
- **Micro-interaction:** On hover, a subtle `0.98` scale-down to mimic the tactile feel of a physical button.

### Cards: The "Impact Container"
- **Style:** No borders. `xl` (1.5rem) rounded corners. 
- **Layout:** Use generous internal padding (`p-8` or `p-10`). 
- **Asymmetry:** For social impact stories, use an asymmetrical image-to-text ratio (e.g., 60% image, 40% text) to break the standard 50/50 "box" feel.

### Input Fields: The "Quiet Entry"
- **Background:** `surface-container-high`.
- **Border:** None (until focus).
- **Focus State:** A 2px "Ghost Border" becomes 40% opaque `primary`.
- **Label:** `label-md` positioned strictly above the field, never as a placeholder.

### Impact Chips
- **Selection:** Use `secondary-container` with `on_secondary_container` text.
- **Shape:** `full` (pill-shaped).
- **Usage:** Use these for tagging "SDG Goals" or "Project Categories" to add a splash of color to data-heavy views.

---

## 6. Do’s and Don’ts

### Do:
- **Do** use whitespace as a functional element. If a section feels crowded, double the padding.
- **Do** use "surface-stacking" to define hierarchy before reaching for a shadow.
- **Do** use `display-lg` typography for mission-critical statements to evoke emotion.
- **Do** ensure all interactive elements have a minimum `44px` hit state, regardless of their visual size.

### Don’t:
- **Don’t** use a `#000000` shadow or border. It kills the "high-end" editorial feel.
- **Don’t** use divider lines between list items. Use `16px` of vertical whitespace or a subtle background shift on hover.
- **Don’t** use "default" blue for links. All links must be `primary` or `secondary` with a 1px underline offset by 4px.
- **Don’t** crowd the corners. Always maintain at least `1.5rem` (xl) of breathing room from the edge of a container to the content inside.