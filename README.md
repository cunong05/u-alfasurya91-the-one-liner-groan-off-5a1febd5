# The One-Liner Groan-Off

[![make.fun](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5)
[![rank](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/cunong05/u-alfasurya91-the-one-liner-groan-off-5a1febd5/rank.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5)

Entry for the [make.fun bounty "The One-Liner Groan-Off"](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5) by [@cunong05](https://github.com/cunong05).

## The joke

> My dad started a band called The Leftovers — all his jokes are reheated.

One line, 72 characters, original dad joke — the kind of pun a dad
delivers at the dinner table, with the punchline landing on the last word.

## How it works

`main.py` holds the entry text, validates it against the bounty gate
(single line, 1–140 characters, no leading/trailing space, valid UTF-8,
not only whitespace), writes it to `/output/entry.txt`, reads the file
back and re-validates it, and prints it:

```sh
python3 main.py            # writes /output/entry.txt (default)
python3 main.py --out /tmp/entry.txt --quiet
```

## License

MIT — see [LICENSE](LICENSE).
