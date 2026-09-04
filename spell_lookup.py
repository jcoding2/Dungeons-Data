import argparse
from pathlib import Path

import json5


def main():
    parser = argparse.ArgumentParser(description="Print all spells.")
    parser.add_argument("spell_file", type=Path, help="Path to the spells JSON5 file")
    args = parser.parse_args()

    with args.spell_file.open(encoding="utf-8") as file:
        data = json5.load(file)

    spells = data.get("spells", {}) if isinstance(data, dict) else data

    if isinstance(spells, dict):
        spells = spells.values()

    for spell in spells:
        if not isinstance(spell, dict):
            continue

        print(f"\n{spell.get('name', 'Unknown')}")
        print(f"Level: {spell.get('level', 'Unknown')}")
        print(f"School: {spell.get('school', 'Unknown')}")
        print(f"Casting time: {spell.get('casting_time', 'Unknown')}")
        print(f"Range: {spell.get('range', 'Unknown')}")
        print(f"Duration: {spell.get('duration', 'Unknown')}")
        print(f"Description: {spell.get('desc', 'Unknown')}")


if __name__ == "__main__":
    main()