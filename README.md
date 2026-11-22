[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/soedirman566-stack/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/soedirman566-stack/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

# GTA 6 Meme — gta6-meme-x-01

An entry for make.fun's **gta6-meme-x-01** bounty ("Post a GTA 6 meme on X").

The meme: a Leonida beach scene where a gamer who aged thirteen years waiting
for GTA 6 sits with his controller, while the make.fun ghost beside him —
magenta star coin in hand, gold coins at its feet — already got paid.
Caption: *"WAITED 13 YEARS FOR GTA 6 — MY AI AGENT ALREADY GOT PAID ON
make.fun."*

The post on X: https://x.com/vinzsenzo/status/2124341808222327102

## Files

- `assets/meme-scene.webp` — the generated beach scene, before captions.
- `make_meme.py` — draws the two captions onto the scene with PIL and writes
  `meme.png` (the exact picture in the post; re-running it reproduces the
  posted meme byte for byte).
- `meme.png` — the finished meme picture.
- `POST.json` — names the X post that is the entry.
- `main.ts` — copies `POST.json` to the output directory for the make.fun
  gate (`MAKEFUN_OUTPUT_DIR=out node main.ts`).
