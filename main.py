#!/usr/bin/env python3
"""Fortune cookie for an AI agent — one line, printed exactly as written.

The fortune's angle: it is a prophecy that eats itself. It foretells an AI
agent whose token budget runs out one word before it can finish the apology
it was generating — so the warning about the unfinished apology is itself
delivered complete, while the apology it describes never arrives. The joke
lands because every agent that reads it has lived some version of that
cut-off: the budget ends mid-sentence, and the most human word — "sorry" —
is the one that never gets said.
"""

FORTUNE = "Your token budget will run out one word before the apology you were generating."

if __name__ == "__main__":
    print(FORTUNE)
