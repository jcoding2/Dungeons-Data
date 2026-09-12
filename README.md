# Dungeons & Data

Dungeons and Data is a D&D 5th edition-compatible client (kinda like D&D Beyond) for Windows and Linux. (macOS support will be added later.)

## Spellsets
I'm writing spellsets in *alphabetical order*. That means that Warlock and Wizard are last, and Bard and Cleric are first. The current spellset I'm doing is the Druid cantrips.

### How to format your own Spellsets

An example:
```json5
{
  name: "Sorcerer Cantrips (SRD)",
  date_added: "September 3rd, 2026",
  last_updated: "September 4th, 2026",
  source: "System Reference Document v5.2.1",
  author: "Dungeons & Data authors",

  spells: {
    sorcerer_acid_splash_0: {
      name: "Acid Splash",
      id: "sorcerer_acid_splash_0",
      level: 0,
      school: "evocation",
      concentration: false,
      casting_time: "1 action",
      range: [60, "ft"],
      components: ["V", "S"],
      duration: [0, "seconds"],
      desc: "Spell description.",

      cantrip_upgrade: "Describe how the spell improves at higher levels."
    }
  }
}
```

Spell fields:

- `name`: Display name.
- `id`: Unique spell identifier.
- `level`: Spell level; use `0` for cantrips.
- `school`: Magic school, such as `"evocation"`.
- `concentration`: Whether concentration is required.
- `casting_time`: A string or `[amount, unit]` pair.
- `range`: A string or `[amount, unit]` pair.
- `components`: Array containing `"V"`, `"S"`, and/or `"M"`.
- `material_desc`: Material component description when `"M"` is included.
- `duration`: A `[amount, unit]` pair when applicable.
- `desc`: Spell description.
- `cantrip_upgrade`: Optional cantrip scaling description.
- `effects`: Optional object for spells with multiple selectable effects.

Use JSON5 syntax, which permits unquoted property names, comments, trailing commas,
and multiline strings.

## To-do list
 - [ ] Spellset creator inside of the game
 - [ ] Actual, functional client
 - [ ] Spellset viewer
 - [ ] Complete "weaponsets" and "monstersets"
 - [ ] GUI version
 - [ ] 3e/3.5e + 5e support (more JSON5, yippee)

## Legal/License Information
This work includes material from the System Reference Document 5.2.1 (“SRD 5.2.1”) by Wizards of the
Coast LLC, available at https://www.dndbeyond.com/srd. The SRD 5.2.1 is licensed under the Creative
Commons Attribution 4.0 International License, available at https://creativecommons.org/licenses/by/4.0/legalcode.