# news-in-one-image-20261126

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/lugasprahara/news-in-one-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/lugasprahara/news-in-one-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

One 1024×1024 image that sums up the world news of Thursday 26 November 2026 — 33 stories in one image. The top story is the US proposal for new tariffs on 14 trading partners; around it sit 11 panels (Houthi attacks on Saudi ports and the Ras Tanura refinery, the Cairo ring-road tanker fire that killed at least 31, Ukraine's strike on Savasleyka airbase, the AI stock sell-off, the US warning its citizens to leave Iran, the first Pakistani astronaut aboard China's Tiangong station, the judges' move in the Netanyahu bribery case, the Gaza strike that killed Hamas's security chief, China's investigation of Shanghai party chief Chen Jining, the EU leaders' clash over the Ukraine loan, and Kim Jong Un's nuclear vow), 21 one-line briefs, and a dark world map with numbered dots for the 12 placed stories. The image is rendered programmatically with Python and Pillow (`render.py`) from the day's wire reports (BBC, Al Jazeera, CNBC, The Guardian, France 24, Euronews, Yonhap and others, credited in the image footer); `main.ts` copies the finished `entry.png` to the output directory, byte for byte, every run.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=aes5np1n&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards</sub>
