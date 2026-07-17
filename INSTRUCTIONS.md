# Your Website — How Everything Works

This is a plain guide, written for someone who has never coded. Nothing here
requires installing a code editor or using a command line — you can do all
of it through your web browser. Come back to this file anytime.

---

## 1. What's in this folder

```
website/
├── index.html          ← Home page
├── about.html           ← About page
├── publications.html    ← Publications page
├── editorial.html       ← Editorial page
├── cv.html               ← CV page
├── contact.html         ← Contact page
├── css/style.css        ← All colors, fonts, spacing — one file controls the whole site's look
├── js/script.js         ← The interactive bits (help tab, mobile menu, publication circle)
└── images/               ← All photos, organized in folders per page
    ├── home/
    ├── about/
    ├── publications/
    ├── editorial/
    ├── cv/
    └── contact/
```

Every page right now uses **placeholder images** (light tan boxes with
labels like "Your Headshot") so you can see the layout before your real
photos are in. Nothing is broken — that's expected.

---

## 2. Preview the site on your own computer (before publishing)

You don't need to publish to see it. Just find the `website` folder on your
computer and **double-click `index.html`**. It will open in your browser
(Chrome, Safari, etc.) and behave exactly like the live site — click the red
help tab, resize the window to see the mobile menu, etc.

Every time you make a change and save the file, just refresh the browser
tab to see the update.

---

## 3. Editing text

Every page is an `.html` file, which you can open with any plain text
editor — on a Mac, **TextEdit** works if you use "Format → Make Plain
Text" first; on Windows, **Notepad** works fine. (If you want a nicer
editor later, a free one called **VS Code** is worth installing, but it's
not required.)

To change text: open the file, use your editor's "Find" (Cmd/Ctrl+F) to
locate the sentence you want to change (search for a few words you can see
on the live page), edit the words between the `<` `>` tags, and save.

**Rule of thumb:** only change text that sits *between* tags, like:
```html
<h1>Your Name</h1>
```
becomes
```html
<h1>Jane Smith</h1>
```
Don't delete the `<h1>` or `</h1>` parts themselves — those tell the
browser how to style the text.

---

## 4. Swapping in your real photos

Each placeholder image is referenced by a line like this in the HTML:
```html
<img src="images/home/headshot.svg" alt="Portrait of Your Name">
```

To replace it:
1. Save your real photo into the matching folder (e.g. `images/home/`).
   JPG or PNG both work fine. Keep file sizes reasonable — under 1–2MB per
   photo keeps the site fast (most phone photos will need resizing/export
   at a smaller size; any free tool like Preview on Mac or the Windows
   Photos app can "export/resize" an image).
2. Rename your photo to match, e.g. `headshot.jpg`, OR keep your own
   filename and just update the `src=` in the HTML to match it exactly
   (including the folder path).
3. Save the HTML file and refresh your browser to check it looks right.

Where each placeholder lives (✔ = your real photo is already in; still a
placeholder = swap it whenever you're ready, same steps as above):

| Section | File(s) to replace | Status |
|---|---|---|
| Home — main photo (the only photo on the page now) | `images/home/main-photo.jpg` | ✔ |
| About — photo next to the bio | `images/about/telegram-photo.jpg` | ✔ |
| About — Watch video | `images/about/columbia-video.mp4` (+ `columbia-video-poster.jpg` for the preview frame) | ✔ |
| Publications — 6 logos | `images/publications/logo-1.svg` through `logo-6.svg` (add more by copying a line in `publications.html`) | still placeholders |
| Editorial — hero image | `images/editorial/hero.jpg` | ✔ |
| Contact — photo booth photo | `images/contact/photobooth.jpg` | ✔ |

The CV page is built from real text (typed in the HTML), not images, so
there's nothing to swap there — just edit the words directly (see section
3 above).

To swap the Watch video for a different clip later: export/save the new
video, name it `columbia-video.mp4` (MP4 format, H.264 — most phone and
editing apps export this by default), and replace the file in
`images/about/`. Keep it under roughly 50MB so the page loads quickly.

---

## 5. Changing colors and fonts

Open `css/style.css` and look at the very top — the `:root { ... }` block.
Every color and font on the whole site is controlled from these few lines:

```css
--color-bg: #FFFFFF;         /* page background — pure white, matches your photos' white backgrounds so they blend in */
--color-charcoal: #83807A;   /* light gray accent — buttons, links, nav */
--color-rose: #F5DEDA;       /* light light pink accent — eyebrows, help tab, dividers */
--font-display: 'Archivo', ...;    /* nav name, section subheads, body text, and page titles (h1) */
--font-nav: 'Lora', ...;           /* the Home/About/Publications/... nav links */
--font-accent: 'Newsreader', ...;  /* italic — one emphasized line per page */
--font-hand: 'Caveat', ...;        /* handwritten photo captions, doodle labels */
--font-mono: 'Courier Prime', ...; /* footer, CV dates, telegram text */
```

The palette is light gray + light pink + pure white, pulled from your
color photo but lightened: gray carries the "functional" parts of the site
(buttons, links, the current-page underline in the nav), and pink carries
the "soft" decorative touches (the small uppercase eyebrow labels, the
help tab, the thin lines under CV section headings). To retune either
color everywhere at once, just change `--color-charcoal` or `--color-rose`
(and their `-dark` partners, used for hover states).

Fonts: **Archivo** for the structural stuff (nav name, subheadings, body
text, and the big page titles/h1s), **Lora** for the Home/About/
Publications/etc. links in the top nav, **Caveat** for smaller handwritten
touches (photo captions, the "creative" label in the Publications circle),
**Newsreader** italic for one flowing accent line per page (the
`class="lede"` paragraphs, the help tab message, the "Email:" line), and
**Courier Prime** for document-style text (footer, CV dates, the About
page telegram).

To change a color, replace the hex code (like `#D8A79B`) with a new one.
A free color picker like [coolors.co](https://coolors.co) or
[htmlcolorcodes.com](https://htmlcolorcodes.com) will give you hex codes
you can paste in directly.

To change any font:
1. Go to [Google Fonts](https://fonts.google.com), pick a font, click it,
   and copy the `<link>` code it gives you.
2. Paste that `<link>` into the `<head>` section of **every** HTML file,
   replacing the existing Google Fonts `<link>` line (or add your new
   font's `family=...` segment onto the existing link's URL alongside the
   others, separated by `&family=`).
3. Update the matching `--font-*` variable in `style.css` to the new
   font's name.

To keep the Home page's "no visible edge" look when you swap in a new
main photo, export or crop it on a plain pure-white background — that's
what makes it blend into the page instead of looking like a framed
photo.

---

## 6. Editing links

- **Publications:** in `publications.html`, each logo is wrapped in
  `<a href="#" ...>` — replace `#` with the real URL of the published piece.
  There are three separate spots using the same logos (the circle, the
  mobile grid, and the text list) — update all three so they match.
- **Socials / Substack:** in `about.html` and `contact.html`, find the
  `.socials` section and replace each `href="#"`.
- **LinkedIn:** in `cv.html`, replace the `href="#"` on the "View on
  LinkedIn" button.
- **Watch video:** this one plays directly from a video file rather than
  YouTube/Vimeo — see section 4's table above for how to swap it for a
  different clip.

---

## 7. Making the "Download PDF" button on the CV page work

The button already points to a file called `cv.pdf` sitting in the same
top-level folder as `index.html` — it just doesn't exist yet. To make it
work:
1. Export your CV as a PDF from wherever you wrote it (Word: File → Save
   As → PDF; Google Docs: File → Download → PDF; Canva: Share → Download →
   PDF — any of these work).
2. Name the exported file exactly `cv.pdf` (lowercase).
3. Add it to the site folder at the top level, right next to `index.html`
   (not inside `images/`). Once it's uploaded to GitHub in the same spot,
   the button will download it automatically — no code changes needed.

---

## 8. Making the contact form actually send emails

GitHub Pages only hosts static files — it can't run the code needed to
send an email from a form, so the Contact page form is wired to
[Formspree](https://formspree.io) (a free service that emails you
whenever someone submits it) at your endpoint
`https://formspree.io/f/mpqvqqla`. This is already set up in
`contact.html` — no action needed. The **mailto link** on the Contact
page (`abigailrebordao@gmail.com`) also works immediately as a backup, in
case anyone prefers to just email you directly instead of using the form.

If you ever need to point the form at a different Formspree form (e.g.
you create a new one), replace the URL in the form's `action="..."`
attribute in `contact.html` with the new one Formspree gives you.

---

## 9. Publishing to GitHub Pages (no coding required)

1. **Create a GitHub account** at [github.com](https://github.com) if you
   don't have one (free).
2. **Create a new repository:** click the "+" in the top right → "New
   repository." Name it something like `your-name-website`. Leave it
   Public. Click "Create repository."
3. **Upload your files:** on the new repo's page, click "uploading an
   existing file." Drag your entire `website` folder's *contents* (not the
   folder itself — the `index.html`, `css`, `js`, `images` etc. should sit
   at the top level of the repo) into the upload area. Scroll down, click
   "Commit changes."
4. **Turn on GitHub Pages:** go to the repo's "Settings" tab → "Pages" in
   the left sidebar. Under "Branch," choose `main` and folder `/ (root)`,
   then click "Save."
5. Wait about a minute, then refresh that Pages settings screen — it will
   show your live URL, something like:
   `https://yourusername.github.io/your-name-website/`
6. That's it — your site is live and shareable.

**Making future updates:** for a small text edit, click into that one file
(e.g. `about.html`) in your repo, click the pencil ("Edit") icon, make the
change, and click "Commit changes." For a big batch of changes like this
round — several files at once — the easiest path is: go to your repo's
main page, select all the files and folders (checkbox at the top, or click
one file and shift-click the last), delete them, commit that deletion,
then use "Add file → Upload files" and drag in everything from your
updated `website` folder again. You don't need to delete the *repository*
itself — just its contents — and you don't need to touch the Pages
settings again, since those stay put. GitHub Pages republishes
automatically within a minute or two either way.

---

## 10. Getting help later

Come back to this conversation anytime — I can help you write bio copy,
pick colors from your vision board, resize photos, add more publications,
troubleshoot a GitHub Pages hiccup, or add entirely new sections.
