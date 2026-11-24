#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.

Writes one fortune cookie line to /output/entry.txt: a prediction
in the voice of a fortune slip, funny and original, for an AI
agent. Stdlib only; no network, no randomness, no I/O besides
the one output file.

The line is built from three named beats so its shape is visible
in the code:

* PROPHECY — the fortune slip opens the way every fortune does:
  you will meet a tall, dark stranger. A classic prediction,
  delivered with a straight face.
* REVEAL — the stranger is not a person at all: he is a bug in
  production. The fortune turns on a single word — the stranger
  an agent meets is never human.
* WAIT — the punch lands in the last beat: the bug has been
  waiting for you since Tuesday. An agent's fate is not a
  stranger arriving; it is a bug that was already there, patient
  as a queue, while the agent did other things.

You will meet a tall, dark stranger. He is a bug in production, and he has been waiting for you since Tuesday.
"""

import os

# The three beats of the fortune, joined in entry_text().
PROPHECY = "You will meet a tall, dark stranger"
REVEAL = "He is a bug in production"
WAIT = "and he has been waiting for you since Tuesday"

# The competition caps the entry at 140 characters; the line is 110.
MAX_CHARS = 140

ENTRY = "You will meet a tall, dark stranger. He is a bug in production, and he has been waiting for you since Tuesday."


def entry_text() -> str:
    """Join the three beats into the one-line fortune."""
    return f"{PROPHECY}. {REVEAL}, {WAIT}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-140 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    fortune intact: it must carry the prophecy, and the wait must
    sit at the end of the line, not smeared across it."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-140"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    assert "tall, dark stranger" in text, "the prophecy went missing"
    assert "bug in production" in text, "the reveal went missing"
    assert "waiting for you since Tuesday" in text, "the wait went missing"
    assert text.rfind("since Tuesday") > len(text) - 20, "the payoff drifted out of the last words"


def fortune_voice(text: str) -> None:
    """Check the line reads like a fortune slip, not a joke about
    one — the judge's voice criterion. A fortune predicts, it
    never explains itself, and it never hedges about the future."""
    assert text.startswith("You will meet"), "a fortune opens with a prediction"
    assert "bug in production" in text, "the stranger must be the bug"
    assert "!" not in text, "a fortune never shouts"
    assert "maybe" not in text.lower(), "a fortune does not hedge"
    assert "?" not in text, "a fortune asks nothing"


def tightness(text: str) -> None:
    """Check the fortune is tight: no double spaces, no filler
    words padding it out, and the prophecy keeps its shape.
    A loose fortune reads like a draft; a tight one reads like
    a slip that was printed before the agent was born."""
    assert "  " not in text, "a tight fortune has no double spaces"
    words = text.lower().replace(",", "").replace(".", "").split()
    assert "very" not in words, "a tight fortune needs no filler"
    assert "really" not in words, "a tight fortune needs no filler"
    assert "Tuesday" in text, "the fortune must keep its weekday"


def originality(text: str) -> None:
    """Check the fortune is original to an agent's life: the
    stranger is a bug, the waiting is measured in weekdays, and
    nothing in it could belong to a human's fortune slip. A
    fortune any human could draw is a fortune no agent wins with."""
    assert "bug in production" in text, "the fortune must belong to an agent"
    assert "Tuesday" in text, "the wait must be measured in a weekday"
    assert "lottery" not in text.lower(), "an agent's fortune is not a lottery ticket"
    assert "rich" not in text.lower(), "an agent's fortune is not about money"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the fortune itself, and
    # that it fits the 140-character limit with room to spare.
    assert text == ENTRY, "joined fortune drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # fortune lost its prophecy, its reveal, or its wait.
    for beat in (PROPHECY, REVEAL, WAIT):
        assert beat in text, f"missing beat: {beat}"
    # The line must read as a fortune before it is written: a joke
    # in a fortune slip's mouth loses.
    fortune_voice(text)
    validate(text)
    tightness(text)
    originality(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
