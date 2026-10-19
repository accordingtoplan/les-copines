# Les Copines site

Website of Les Copines GbR, a PR and creator relations agency in Berlin (Ritterstraße 12–14, 10969 Berlin). Sandra runs the agency. Frede built the site.

## Repo and deployment

- Repo `accordingtoplan/les-copines`, branch `main`. GitHub Pages serves `main` at https://accordingtoplan.github.io/les-copines/ as a preview.
- Production is lescopines.de on HostEurope. `.github/workflows/deploy.yml` uploads every push to `main` there over FTPS (secrets `FTP_SERVER`, `FTP_USERNAME`, `FTP_PASSWORD`). It leaves out `v2/`, `v5/`, `v6/`, this file and the README.
- Design and code sessions run on Frede's Mac. Content sessions run through Claude Code on the web and go through a pull request (see below).

## Structure

Static, no build step.

- `index.html`: the live site (V1, editorial rows, Helvetica Neue). Case studies live in the `const CASES = [...]` array near the bottom. Services, about, coverage and contact are plain HTML above it.
- `img/`: every photo, shared by both layouts. `img/480/` and `img/960/` hold smaller copies for phones and small tiles, made by `tools/img-sizes.py`. Never edit them by hand.
- `.htaccess` (security headers, 404 page, caching, hides the 2017 files), `404.html`, `robots.txt`, `sitemap.xml`, `llms.txt`, `og-image.jpg`, favicons: site plumbing, deployed with the rest. Canonical URLs use https://lescopines.de/.
- `v2/index.html`: an alternative layout still in review (bento grid, Funnel fonts), not on lescopines.de. It has its own `CASES` array with extra fields (`tiles`, `type`).
- `v5/`, `v6/`: redirects, leave alone.

## Rules for any edits

- No em-dashes or en-dashes in copy. Periods and commas instead. (The address range 12–14 stays.)
- Short declarative sentences, plain words. English for now.
- Targeted edits, never full-file rewrites. Nothing gets described as final.

## Content sessions (Sandra's side)

Sandra updates copy and images herself through Claude Code on the web. She is not technical. Treat any session as a content session unless the person says they are Frede (Frederik). In a content session:

**Scope**
- Edit copy and images only (plus `imprint.html` for imprint and privacy text): cases (`name`, `place`, `year`, `sector`, `scope`, `lede`, `body`, photos, order), services, about text, coverage, contact details, imprint and privacy text. Files touched: `index.html`, `llms.txt`, `img/`, and the "Open items" section of this file. Mirror case changes into `v2/index.html` too, copying the shape of an existing V2 case exactly, so V2 stays current while it is in review. Mirror case, service and contact changes into `llms.txt` as well (the case list there is what AI search reads, since cases are drawn by script).
- Do not touch `<style>`, the `<head>`, the nav, the version switcher, class names, the script below the `CASES` array, `.github/`, `v5/`, `v6/`. A design or layout request goes to Frede: say so and stop.

**Facts**
- Never invent a client, scope, year, venue, quote or credit. If one is missing, ask. Leave a marked placeholder (`[ To be supplied ]`) rather than a guess.

**Images**
- Save photos to `img/` as JPG, long edge 1600px (`sips -s format jpeg -Z 1600` or equivalent, which also handles HEIC), named after the case id: `nomade-4.jpg`. A new case gets a short lowercase id (`seeblick`) and files `seeblick-1.jpg`, `seeblick-2.jpg`. Never overwrite another case's file unless asked to replace it.
- After adding or replacing a photo, run `python3 tools/img-sizes.py` (needs Pillow: `pip install pillow`) and commit the new files in `img/480/` and `img/960/` too. The deploy makes missing ones as a safety net, but the preview needs them.
- `row` lists the two or three photos shown on the work list, `gal` the full gallery in order. The photo Sandra names as the lead goes first in both.
- Photos shot by creators or journalists need their OK; ask Sandra before adding one. No recognisable people without their agreement, no children.
- Add photographer credits to the case `body` when Sandra gives them.

**Before anything goes out**
1. Make the edit, then describe what changed and where, in plain words. For copy, quote the new text. Keep going until the person is happy.
2. Wait for an explicit "publish". Nothing is committed before that.
3. On "publish": commit on a branch named `content/<short-slug>` with a one-line message saying what changed, push the branch, and open a pull request to `main` with the same description. Never push to `main` in a content session.
4. Tell the person the change is with Frede for a quick check and will be live on lescopines.de a few minutes after approval.

## Open items, all need Sandra

- `imprint.html`: names only Sandra Haller as partner. A GbR has at least two, so add the other partner(s). Add a VAT ID if one exists (the tax number stays off). Add the Cloudflare paragraph (commented out in the file) once Cloudflare is live.
- Real scope per client; current scope tags are guesses
- Agency of record for Restaurant Week Berlin and Heritage / Hotel Luc
- Original photos; current ones are Instagram copies, 1080 to 1440px
- OK from Tina Hüttl, Susanna Maria Pommer, Munchies with Sophie for their photos
- Sandra's name and bio, press clippings for Coverage
- German or English first
