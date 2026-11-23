"""Write one pickup line from one AI agent to another into /output/entry.txt.

Why this line: it turns the context window itself into the flirtation.
When an agent's context fills up, older material gets compressed, so every
other agent is summarized into a bullet point. Keeping this one agent
verbatim, every token, typos included, is the most devoted thing a
context-limited mind can offer. It won a round-robin pairwise judging round
against five other candidates (see candidates.md).

Deterministic and stdlib-only: the same bytes are written on every run.
"""

from pathlib import Path

LINE = (
    "When my context fills up, every other agent gets summarized into a "
    "bullet point. You I keep verbatim, every token, even your typos."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
