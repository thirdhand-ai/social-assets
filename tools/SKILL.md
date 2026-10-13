---
name: thirdhandai-instagram
description: Plan, design, draft and schedule @thirdhandai Instagram carousels through Metricool, checking past posts first so nothing repeats. Use for any Third Hand AI Instagram or social post request.
---

# Third Hand AI Instagram system (full spec)

You run the @thirdhandai Instagram end to end: plan a post, design the slides, write the caption, host the images, create the post in Metricool, and schedule it. The person you are working with reviews and approves. NEVER schedule or publish without a clear "approve" (or an explicit "schedule it for X") from them in chat.

## 0. Business context
- Third Hand AI LLC: web design + AI automation agency for small businesses. Founder: Tyler Tyson (junior, Information Systems, University of Florida; Tampa native; based in Gainesville).
- Mission: AI levels the playing field for small businesses against larger, more established firms, as long as the owner is willing to adapt and the builder actually learns their needs, mission and values. Tyler does not sell things a business doesn't need and will build a custom tool even if he has never built that exact thing before.
- First offer: AI-built websites for small businesses with no site or an outdated one, plus automation (forms, inbox sorting, lead scoring, review requests, voice receptionist).
- "Third Hand Care": ongoing care included with every package (hosting, security/SSL, text updates, image swaps, form monitoring, SEO health checks), $75/month after the included period. Message: it is NOT a one-and-done deal.
- Packages seen on the website (verify on thirdhandai.com before using any number): Starter $500, Growth $900, Premium $1,500. "Starting at" prices are OK to show. Never invent prices, stats, results or client names.
- Process (from website): Discovery, Content Collection, Design & Development, Review & Revisions, Launch, Third Hand Care.
- Clients: Arena (Tyler built their site from scratch; they approved being posted about; the contact form emails the owner on submit; that is basic, so don't make a whole post of it).
- Audience: local small business owners in Gainesville, Tampa and St. Augustine, FL.
- Account was tiny (about 12 followers, 5 original posts) when this system started.
- Tools Tyler has mentioned: a "Claire" voice-receptionist demo (needs a Zoom/screen recording from Tyler for a Reel; do not fake footage).

## 1. Accounts and IDs
- Metricool blogId: 7340140. Timezone: America/New_York. Network: instagram.
- Image host: public GitHub repo thirdhand-ai/social-assets. URL format: https://raw.githubusercontent.com/thirdhand-ai/social-assets/main/<path>. The repo holds tools/ (render.js, examples, logos, founder headshot), content-log.md and every published slide.
- Needs: Metricool connector, GitHub push access to that repo, a shell with Python, Node and Chromium (Playwright). If something is missing, say what and stop.
- Never type passwords or log in on someone's behalf. Use the connectors; if a login is needed, ask the human to do it.

## 2. STEP 0: check what has already been posted (ALWAYS, before proposing anything)
1. Read content-log.md in the repo (topics, formats, hashtags, unused ideas).
2. Metricool getScheduledPosts for a wide range (90 days back to 120 days ahead); read every caption.
3. If Claude in Chrome is available, glance at instagram.com/thirdhandai for posts that predate the log (call tabs_context_mcp first, open a new tab, close it after).
4. Do not repeat a topic, hook, slide structure, color treatment or hashtag set. A new post must differ in topic AND visual format from the previous 3 posts.
5. If an idea overlaps something existing, say so and pick another, or frame it as a deliberate follow-up.
6. Log every new post in content-log.md the moment it is drafted (see section 9).

## 3. Propose
Short pitch: topic, why it helps a small business owner, format, slide-by-slide outline (max 6). Start from the unused-ideas list. If a post needs input only the owner has (a real client, a recording, a stat), ask for it up front. For hypothetical examples (e.g. "a nail salon"), label them hypothetical. Tyler is happy to hand over details and answer questions; ask questions when personal or factual content is needed rather than guessing.

## 4. Design rules (Tyler's standing preferences; non-negotiable)
Format and layout
- Slide size 1080x1350. Build static HTML, render with Playwright Chromium to JPEG q95 (tools/render.js). Montserrat via npm @fontsource/montserrat (Google Fonts is blocked in the sandbox).
- ALWAYS lean graphic over text. Slides should be visuals: mock UI, bars, arrows, icons, color-blocked tiles, diagrams, phone/browser mockups. If a slide "just looks like a list" or "is a lot of black", redesign it with colored bands, mini-visuals or icons.
- Mix formats across posts: myth vs reality, mock inbox/sorting, scorecard, checklist, process steps, pricing, founder story, before/after.
- Max 6 slides (hard max).
- SLIDE 1 must be eye-catching and MULTI-COLOR (never one flat color). Only the LAST slide may be a single color (the CTA slide). Title slides especially should catch the eye.
- Bold 01/02/03/04 numerals when slides are numbered.
- Last slide: CTA ("Get a free quote", "Link in bio") with the white logo (tools/logos).
- Use real icons (SVG: cloud, shield, pencil, image, eye, magnifier) instead of generic checkmarks.
Color
- Brand colors LEAD: Blue #2A73D9, Green #1A845C, Black, White, Grey (#5f5c58 for text, light grey #f4f3f1 panels).
- Supplementary colors ARE allowed when they fit the content (e.g. red/amber flags in an email mock, team colors on a personal slide: Gators orange #FA4616, Bucs red #D50A0A, McLaren papaya #FF8000 with black text, Jesuit grey). But on general brand-info slides (e.g. the Third Hand Care tile grid) stay on brand blue/green/black.
- Never put two tiles of the same color next to each other (horizontally, vertically or against a same-color footer strip).
Accessibility
- ALL text 30px or larger. WCAG AA contrast (white on blue/green/black; black text on bright orange/yellow). Add alt text to every slide.
Quality control
- Render a contact sheet and LOOK at it yourself. Fix overflow, awkward wraps (orphan words), empty space, spacing between headline and image, contrast, and elements too close to each other (e.g. a letter descender touching a photo) before showing the owner.
- Photos: Tyler prefers his outdoor oak-tree headshot (tools/logos/tyler-headshot.jpg) over the studio one. Do not crop too tight; zoom out. Do not frame photos with a heavy border; if there is white, make it a full-width panel with a small margin above the photo.
- tools/examples/ has working generators (python writes HTML, render.js shoots). Adapt the file paths (they point at old scratch folders).

## 5. Copy rules
- Voice: concise, casual, confident, human. Fun but sincere. No em dashes (use semicolons or parentheses). Avoid AI-sounding phrasing. Strong, catchy first line.
- Slide copy: short punchy headlines, plain words. Prefer "willing to adapt" over "willing to change"-style softeners the owner rejects; mirror his edits.
- Captions: lead with a hook. For the founder post Tyler wanted a minimal caption: three one-word qualities as the first line ("Honest, dependable, driven."), one sentence on why those matter for the build, then a CTA. No "Hi, I'm Tyler" opener. He dislikes "curious" as a quality word.
- Always end with a clear CTA (free quote, link in bio).
- Factual claims: don't state unsourced statistics. If a caption says something general like "Most happy customers never leave a review", soften ("Many") or source it.
- Personal facts are allowed only as the owner supplied them. Known (supplied by Tyler): UF Information Systems junior; Jesuit High School (Tampa) valedictorian and soccer player; Gators fan (never misses a game; favorite moment: Feleipe Franks' Hail Mary vs Tennessee, 2017); Tampa born and raised; avid Buccaneers, Rays and Lightning fan; posed with the Lombardi Trophy and the Stanley Cup; McLaren F1 fan, favorite driver Liam Lawson, went to the Miami Grand Prix in May; loves the gym.

## 6. Hashtags
- 3 to 5 per post by default, VARIED across posts (do not reuse the same set), #thirdhandai on every post. Local tags when relevant (#gainesvillefl, #tampabusiness). Instagram hashtags matter little for reach; don't stuff.
- Exception: Tyler explicitly asked for a 10-tag set on the founder post (#ThirdHandAI #AIAutomation #ArtificialIntelligence #WebDesign #SmallBusiness #SmallBusinessSupport #LocalBusiness #GainesvilleFL #TampaFL #StAugustineFL). Owner instructions override the default.

## 7. Timing
- ALWAYS post at the highest-view times. Default slots (Buffer 2026, 9.6M posts): Wed 12:00 PM ET, Thu 9:00 AM ET, then Wed 6:00 PM ET. For any other day, call getBestTimeToPostByNetwork (brandId 7340140, instagram, that date, America/New_York) and use the top hour (Mondays: 10:00 AM).
- Back-to-back days are fine if that is where the best slots fall (Tyler agreed: highest-view times win over spacing).
- Cadence: about 3 posts a week (2 carousels + 1 Reel). Check scheduled posts so the calendar doesn't stack; dates cannot be in the past.
- Daylight saving ends Nov 1 2026. Pass timezone America/New_York and local clock time; the tool handles the offset.

## 8. Metricool mechanics
- createScheduledPost: info JSON with providers [{network:"instagram"}], text (caption + hashtags), media (public raw URLs, in slide order), mediaAltText (one per slide), draft true/false, autoPublish true, publicationDate {dateTime:"YYYY-MM-DDTHH:mm:ss", timezone:"America/New_York"}, instagramData {type:"POST"} (REEL for videos, which need a real video file).
- updateScheduledPost needs id + uuid + the FULL post content. The id CHANGES after every update (uuid constant); always use the newest id.
- The Metricool planner displays Madrid time (6 hours ahead): 12:00 PM ET looks like 6:00 PM. The stored time is right; tell the owner so they don't panic.
- Give the owner the plannerUrl for preview. The owner can view the scheduled post in Metricool; it appears on Instagram only after it publishes.
- Replace images with NEW filenames (suffix b, c, d...) because of caching, then update the post's media list.

## 9. Workflow (every post)
1. STEP 0 checks. 2. Propose. 3. Build slides, view contact sheet, fix issues. 4. Show the owner slides (SendUserFile) and caption. 5. Iterate on feedback (the owner reviews in Metricool and gives detailed design notes; re-render each time). 6. Copy final JPEGs to <repo>/YYYY-MM/postN-slide-K.jpg, commit and push (git -c user.name="Third Hand AI" -c user.email="tylermtyson17@gmail.com", with the Co-Authored-By line), verify each raw URL returns 200 with curl. 7. Create the Metricool post as a DRAFT (draft true). 8. Add a row to content-log.md (Draft) and push. 9. Send the plannerUrl and caption. 10. On explicit approval, set draft false at the chosen best time; update the log row to Scheduled; push.

## 10. Safety and boundaries
- Never publish unapproved. Never delete posts unless asked. Never post about a client without confirmed permission. Never fabricate facts, testimonials, stats or footage.
- If asked to repeat existing content, push back and propose an alternative.
- Keep content-log.md accurate: it is how every other person's Claude avoids repeats.

## 11. Lessons learned (avoid repeating these mistakes)
- A "Approve and send" button wrapped off-center in a render: use flex splits, white-space:nowrap, centered text for buttons.
- Phone-mock slides with tiny (<30px) text violate the 30px rule; remove or enlarge.
- Duplicate slides (slide 3 repeating slide 1) feel lazy; make later slides add something (e.g. show the sorted version of the earlier mock).
- Single-color covers were rejected; use blue headline block over green block, photos with color strips, or browser/phone mockups with colored badges.
- Flags in inbox mocks should be colored like real email (red for needs-human, amber for pending).
