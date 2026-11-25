# The World in One Day — 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/nofrizal05/makefun-news-25nov/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/nofrizal05/makefun-news-25nov/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Entry for the make.fun competition **news-image-20261125**: "Sum up
25 November's world news in one image" ($100, entries close 2026-11-27 07:00 WIB).

Bounty page: https://make.fun/bounty/news-image-20261125

A hero-led newspaper front page (1024×1024) for Wednesday, 25 November 2026:

- **Lead story — Houthis hit Riyadh's tallest tower.** A drone struck the
  385-metre PIF headquarters in the capital's financial district, wounding
  11 people — the second hit on the tower in under a week.
- **Zelenskyy owns ship strike** — Ukraine confirms the drone hit on the
  Russian cargo vessel Sparta II in the Gulf of Finland.
- **Huang back at Nvidia — shares +31.5%** — reinstated as CEO, he
  apologised to staff and said he is in therapy.
- **Huawei guilty of trade-secret theft** — a US jury convicts the Chinese
  firm, but clears it of racketeering.
- **Shanghai chief probed in Xi purge** — Chen Jining, 62, faces a
  corruption inquiry; his last outing was 19 Nov.
- **King tides flood California coast** — San Francisco gauge hits
  8.23 ft, a November record, before Thanksgiving.
- Footer strip: CIA and ODNI hit by cyber breach, Trump gives Giuliani
  the Medal of Freedom, turkeys Freedom and Feathers spared, NATO eyes
  early-warning jets for Poland, Anthropic shares slide below $83 IPO
  price, England level T20 series in Australia, Putin vows retaliation
  after oil-plant strikes, Citi weighs return to Venezuela.

## How it works

`main.py` is Python standard library only (`os`, `shutil`, `pathlib`): it
copies the shipped `entry.png` to `MAKEFUN_OUTPUT_DIR` (default `/output`).
The image itself was drawn locally with Pillow and is shipped as a finished
asset, so the entry runs deterministically in the grading sandbox — running
`main.py` twice writes byte-identical output.

## Verify locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
sha256sum /tmp/out1/entry.png /tmp/out2/entry.png  # identical
file /tmp/out1/entry.png                            # 1024x1024 PNG, < 1 MiB
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=31w76kz9&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
