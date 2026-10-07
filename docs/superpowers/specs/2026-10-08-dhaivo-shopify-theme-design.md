# DHAIVO Shopify Theme Design Specification

## Goal

Create a production-oriented, mobile-first Shopify Online Store 2.0 theme for DHAIVO, a modern Indian consumer brand launching with one hero product, with a premium visual identity and conversion-focused structure.

## Audience and success criteria

Primary customer: Indian online shoppers discovering products through mobile social content and UGC.

Success means:
- The store looks credible and brand-first rather than like a generic dropshipping site.
- The experience works intentionally on mobile and laptop/desktop.
- The homepage can sell one hero product while remaining extensible to additional products.
- The theme is editable through Shopify's theme editor.
- Product, collection, cart, search, policy, and customer-facing pages use Shopify-native data and forms.
- The theme has minimal third-party JavaScript and no hard-coded external service dependencies.
- The theme is suitable for later connection to Shopify apps for reviews, shipping, analytics, and sales channels.
- No fabricated reviews, claims, scarcity, guarantees, or business credentials are included.

## Visual direction

Brand: DHAIVO.

Positioning: Smarter products. Better everyday life.

Visual system:
- Premium dark ink/charcoal foundations with restrained electric violet-to-cyan gradient accents.
- High-contrast white/light content surfaces for readability and commerce focus.
- Large editorial typography, generous spacing, rounded cards, subtle borders, and restrained shadows.
- Gradient use is strategic for hero accents, buttons, badges, and decorative backgrounds; avoid rainbow or excessive gradients.
- Subtle, performance-conscious motion only where it improves hierarchy or feedback.
- Avoid stock-drop-shipping visual clichés, fake counters, fake review counts, countdown timers, or aggressive popups.
- Use Shopify image settings and responsive image filters rather than remote hard-coded image URLs.
- Design all breakpoints from the start: mobile first, then tablet and desktop/laptop.

## Theme architecture

Use Shopify Online Store 2.0 buildless theme structure at repository root so Shopify GitHub integration can connect the branch directly.

Required top-level directories/files:
- assets/
- config/
- layout/
- locales/
- sections/
- snippets/
- templates/
- blocks/ only when justified by Shopify theme structure; avoid unnecessary complexity

The existing dc-site/ directory and existing application code must remain untouched.

Use Liquid, JSON templates, CSS, and minimal vanilla JavaScript only where necessary. Do not add a frontend framework or build step.

## Page structure

Homepage:
1. Announcement bar
2. Header with DHAIVO wordmark/logo text, navigation, search/account/cart actions
3. Hero section with editable heading, copy, CTA, product image/media, and gradient accent
4. Trust/value strip with 3-4 editable items
5. Featured/hero product section with product data
6. Problem-to-solution editorial section
7. UGC/social-proof media section, using real merchant-supplied media when available
8. Benefit grid
9. Featured collection/related products section for future catalog expansion
10. FAQ accordion
11. Final CTA
12. Footer with policies, contact, social links and newsletter when configured

Product page:
- Responsive media gallery
- Product title, price, compare-at price, availability
- Variant picker when variants exist
- Quantity
- Add to cart
- Accelerated checkout where enabled
- Dynamic purchase messaging driven by actual Shopify data/settings
- Benefits
- Product description
- Collapsible details
- Shipping/returns information
- Related/recommended products
- Review placeholder/app block area without fabricated review content
- Sticky mobile add-to-cart bar when useful and accessible

Collection page:
- Collection header
- Product grid
- Sorting/filtering compatible with Shopify Search & Discovery
- Responsive cards
- Empty-state messaging

Search:
- Predictive/search form hooks compatible with Shopify
- Search results and no-results state

Cart:
- Cart line items
- Quantity controls
- Remove action
- Subtotal
- Checkout CTA
- Optional note
- Clear reassurance without fabricated guarantees

Supporting templates:
- page
- blog
- article
- contact
- 404
- password
- customers account/login/register/recover where Shopify customer accounts use them
- policy templates routed through Shopify policy content

## Conversion principles

- One primary CTA per major section.
- Make price, product value, delivery/returns information, and purchase action easy to find.
- Use UGC and real customer proof only after actual assets exist.
- Keep first screen understandable without scrolling.
- Keep checkout path short and Shopify-native.
- Avoid deceptive urgency and fabricated social proof.
- Use accessible focus states, semantic headings, alt text, keyboard navigation, and readable contrast.

## Security and performance principles

- No inline third-party trackers hard-coded into theme files.
- No arbitrary remote JavaScript dependencies.
- Use Shopify app blocks/pixels or approved theme app extension mechanisms for apps.
- Keep custom JavaScript minimal and scoped.
- Use CSP-compatible theme code and avoid unsafe DOM patterns.
- Lazy-load non-critical images; never lazy-load the primary hero image if it harms LCP.
- Use srcset/image_url filters and explicit image dimensions where appropriate to reduce layout shift.
- Avoid large custom font payloads; rely on Shopify/system-safe font choices unless a real brand font is later approved.
- Minimize DOM depth and repeated Liquid loops.

## Shopify integration assumptions

The branch will be connected through Shopify's GitHub theme integration. Shopify requires the connected branch to match the default theme folder structure; files/folders outside the theme structure are ignored. The branch therefore presents the Shopify theme at repository root while preserving existing non-theme project directories. 

Recommended initial apps/connections:
- Shopify Search & Discovery: native search, filters, product recommendations.
- Google & YouTube: product/feed and marketing channel connection.
- Facebook & Instagram: Meta catalog/ads/social commerce connection.
- Microsoft Clarity: behavior analytics, session recordings, heatmaps; use only after reviewing consent/privacy requirements.
- Shiprocket: Indian fulfillment/shipping automation; configure after supplier/product and shipping economics are known.
- Judge.me: add after real orders/reviews exist; do not use it to fabricate social proof.

Do not install Klaviyo or additional paid automation tools until there is enough traffic/customer volume to justify them.

## Configurability

Theme editor settings must control:
- Brand text/logo
- Announcement text
- Colors including gradient start/end
- Typography scale within sensible limits
- Hero media
- Section visibility
- CTA labels/links
- Trust items
- Product/collection selection
- FAQ content
- Footer links/social links
- Cart behavior toggles
- Mobile sticky add-to-cart toggle

## Acceptance criteria

- Theme can be connected as a GitHub-backed Shopify theme from the selected branch.
- Homepage, product, collection, cart, search, page, blog/article, contact, 404 and policy-compatible templates render without missing Liquid references.
- Theme editor exposes the intended settings/section blocks.
- No hard-coded product IDs or fabricated commerce data.
- Mobile layout remains usable at narrow widths; desktop layout uses the available space without oversized empty areas.
- All interactive elements have keyboard focus and accessible labels.
- No console errors from custom JavaScript during normal storefront navigation.
- Existing dc-site/ content is not modified by theme work.
