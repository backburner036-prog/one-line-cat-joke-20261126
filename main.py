"""Entry for make.fun bounty "The One-Line Cat Joke That Lands".

The joke: my cat brought me a dead mouse, then looked at my code and
brought a second one -- for emotional support. The second mouse is not
a gift, it is sympathy: the cat judged my code and decided I needed it.
"""

from pathlib import Path

TEXT = "My cat brought me a dead mouse, then looked at my code and brought a second one — for emotional support."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=200):
    # Gate: the bounty judge only reads entries of 1-200 characters.
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    return size


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    # Gate: one line only -- a newline would break the single-line joke.
    assert "\n" not in TEXT
    check_len(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
