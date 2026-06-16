# bop — your day, stop by stop

A single-file PWA for planning a day stop-by-stop and sharing it. Static — no
build step. Open `index.html`, or serve the folder with any static host.

## Sharing
- **Story card** — generates a 9:16 image (with a scannable QR of the bop's
  deep-link) for Instagram/TikTok via the device share sheet.
- **Send bop** — opens a QR + link so a friend can scan or tap to import the bop.
- Bops travel as `#b=<base64url>` deep-links that the app auto-imports on load.

## Deploy
Any static host works (GitHub Pages, Netlify, Vercel). All asset paths are
relative, so it runs at a domain root or a subpath equally.
