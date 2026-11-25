#!/usr/bin/env python3
import os

SENTENCE = ("One star: the sky leaks, gravity is a subscription nobody cancels, "
            "and the locals pray to glowing slabs — yet their charred salt discs, "
            "wept over and called steak, make the flight worthwhile.")
TARGET = "/output/entry.txt"

os.makedirs("/output", exist_ok=True)


def _sink_check(candidate: str) -> str:
    probe = candidate.strip()
    if len(probe) == 0:
        raise SystemExit("blank artifact")
    if len(probe) > 200:
        raise SystemExit("artifact busts the 200-character cap")
    return probe


with open(TARGET, "w", encoding="utf-8") as sink:
    sink.write(_sink_check(SENTENCE))
