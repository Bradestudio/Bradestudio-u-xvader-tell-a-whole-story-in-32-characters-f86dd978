# Tell a Whole Story in 32 Characters

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![LIVE](https://img.shields.io/badge/status-LIVE-green)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![entry](https://img.shields.io/badge/entry-free-brightgreen)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

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
