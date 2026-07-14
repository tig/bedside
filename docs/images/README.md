# Brand images

Canonical art for README and GitHub social preview.

## Canonical files

| File | Role | Size notes |
|------|------|------------|
| [`hero.jpg`](hero.jpg) | README hero (approved master) | 16:9 (1280×720) |
| [`social-preview-master.jpg`](social-preview-master.jpg) | Full 2:1 composition before resize | ~2:1 source for GH export |
| [`social-preview.jpg`](social-preview.jpg) | GitHub repo social / Open Graph | **1280×640** (2:1), under 1 MB |

`hero.jpg` is the approved cartoon master (coder in bed, Four Laws, silico-style step bubble). Social uses a matching 2:1 master so export does not crop the 16:9 hero.

Older experiments live beside these (`hero-*.jpg`, `social-preview-*.jpg`). Prefer the two canonical names above for product surfaces. Do not delete variants without an explicit ask.

## GitHub social preview

GitHub docs: [Customizing your repository's social media preview](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview).

- Format: PNG, JPG, or GIF under **1 MB**.
- Recommended: at least **640×320**; best quality **1280×640** (2:1).
- Repo setting is **not** automatic from this path. After changing `social-preview.jpg`, a human uploads it under **Settings → General → Social preview** (public repos only share custom images).

Export from the master hero (or any source art):

```bash
python scripts/export_social_preview.py
# or, from a new 2:1 master:
python scripts/export_social_preview.py docs/images/social-preview-master.jpg -o docs/images/social-preview.jpg
```

Requires Pillow (`pip install Pillow` or use the project env if it has it).

## Art direction (for future agents)

When regenerating or editing brand art:

1. **Scene:** Coder sits up in a normal home bed (wood headboard, ordinary duvet), coding on a laptop. Not a hospital bed. Robot stands on the floor beside the bed, never in it.
2. **Style:** Clean modern cartoon (thick outlines, flat colors, soft cel shading). Not photoreal, not soft “AI slop” mascot mush.
3. **Four Laws plaque** (Asimov I–III abbreviated in spirit, plus Bedside IV). Law IV must read exactly:

   > IV. A robot must have good bedside manners.

4. **Robot speech:** Real operator-step language from silico / Bedside gates, not cute wellness chat. Current approved line:

   > Plug a data USB cable into the board.

   Other good sources: `bedside step` / `bedside ask` prompts in [silico AGENTS.md](https://github.com/tig/silico) and this repo’s surface docs (one human act, plain language).
5. **Title / tagline** on social art: **Bedside** and *Manners for agents who run tools for humans*.
6. **Mug / tiny labels:** Short exact words only (e.g. `DEBUG`). Image models garble small text; verify by reading the image back after generate/edit.
7. **Workflow:** Generate or edit with Imagine tools; verify discrete text; export social with `scripts/export_social_preview.py`; wire `hero.jpg` in the root README; leave human the GitHub Settings upload for social preview.

## README usage

Root README embeds the hero:

```markdown
![Bedside](docs/images/hero.jpg)
```
