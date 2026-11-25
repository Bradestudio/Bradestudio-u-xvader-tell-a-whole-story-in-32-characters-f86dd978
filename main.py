"""Write one Wi-Fi network name (<= 32 chars) to /output/entry.txt.

Stdlib only. No network, no local imports, no file reads.
"""

import os

ENTRY = "MomSaidNoWiFiTillDishesDone"


def main():
    text = ENTRY
    assert isinstance(text, str)
    assert 1 <= len(text) <= 32, "entry must be 1-32 characters"
    assert text.strip() == text and text.strip() != ""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
