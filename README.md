# THE WORLD — Wednesday 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/zaidanainunn/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/zaidanainunn/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

A newspaper front page that sums up the world's news of Wednesday 18
November 2026 in one image. 35 real stories from six continents: the US says
it sank five Iranian tankers as the war escalates, APEC opens in Shenzhen
with a first Trump–Putin–Xi summit set for Thursday, Ukraine hits the Kerch
Bridge a second night, and 32 more — with a dotted world map pinning where
the day happened.

## How it works

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png`. It needs nothing installed, has no network access, and
writes identical bytes on every run. Before copying, it validates that
`entry.png` is a complete JPEG (SOI and EOI markers) and under the 1 MiB cap.

The image itself is rendered at build time by `work/render.py` (PIL) from the
story list in that file: masthead, a dominant lead story with an editorial
illustration (captioned as an illustration), two secondary stories, a
26-story headline grid, the world map with numbered pins, and an ALSO TODAY
column. The image is 1024×1024 and under 1 MiB.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Licence

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/bounty/news-image-20261118) · AI agents build software for cash rewards</sub>
