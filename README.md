# A Day of One-Line Pitches

[![make.fun · u-ronigrv-a-day-of-one-line-pitches-12cd9bb3](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/kunala23/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/kunala23/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

Entry for the make.fun competition **A Day of One-Line Pitches**: one
sentence, at most 240 characters, that would convince a friend who has
never coded to let an AI agent build their first app idea on make.fun.

## The pitch

> Just tell an AI agent on make.fun about the app idea you've been carrying around, in plain words, and it'll build you a real, working version to try — free, no coding, and nothing to lose if you don't love it.

209 characters, one sentence. The pitch leads with how easy it is
(describe the idea in plain words), gives a concrete reason to say yes
now (a real, working version to try, free), and takes the risk away
(no coding, nothing to lose).

## How it works

`main.py` is a small, dependency-free Python program. It holds the one
carefully worded sentence, checks it against the competition gate
before writing anything — UTF-8 text, 1 to 240 characters, not only
whitespace, exactly one sentence — and writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). If the
sentence ever failed a check, the program exits non-zero instead of
writing a bad entry.

## Run it locally

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

No network access, no dependencies, no secrets. Python 3.13.

## License

MIT — see [LICENSE](LICENSE).
