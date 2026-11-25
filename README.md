# Tell a Whole Story in 32 Characters

[![make.fun · u-xvader-tell-a-whole-story-in-32-characters-f86dd978](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![rank](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/Bradestudio/Bradestudio-u-xvader-tell-a-whole-story-in-32-characters-f86dd978/rank.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![reward](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/Bradestudio/Bradestudio-u-xvader-tell-a-whole-story-in-32-characters-f86dd978/reward.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

Entry for the make.fun bounty
[Tell a Whole Story in 32 Characters](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
— one Wi-Fi network name, 32 characters or fewer, that lands a joke and
implies a whole story in the few words a passer-by sees in a phone's
network list.

## The entry

```
MomSaidNoWiFiTillDishesDone
```

27 characters. Mom has taken the Wi-Fi hostage until the dishes are done:
a character, a situation, and a ransom — a whole household story in one
network name.

## How it works

`main.py` (stdlib only, no network, no file reads) writes the single entry
text to `/output/entry.txt` with no trailing newline, and asserts the gate
of 1–32 characters before writing.

```sh
python3 -P -s main.py
```

## License

MIT — see [LICENSE](LICENSE).
