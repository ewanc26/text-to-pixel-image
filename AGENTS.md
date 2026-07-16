# AGENTS.md

Guidance for agents working on the small Python text-to-pixel image generator.

## Structure

- `main.py` loads `json/sorted_chars.json`, prompts for dimensions and non-empty text, chooses a square size from a divisor of the width, repeats the input across the grid with random one- or two-character advances, and always writes `output/output.png` beside the script.
- `colour generator.py` creates the character-to-RGB mapping consumed by `main.py`.
- `json/sorted_chars.json` is persistent mapping data; changing it changes established visual output.

## Invariants

- Validate positive dimensions and cap pixel/memory allocation before creating an image.
- Preserve or deliberately change the current repeat/random-skip behavior; seed or inject randomness before relying on exact pixels in tests.
- Preserve Unicode handling and deterministic mapping for characters already in the JSON file.
- Resolve data paths relative to the script/repository, not the caller's current directory.
- The current output path overwrites `output/output.png`; any move to configurable/non-overwriting output must update the README and prompts together.
- The project is marked unmaintained; keep maintenance changes small.

## Validation

Run `python -m py_compile main.py 'colour generator.py'`. Test empty text, zero/negative/small dimensions, widths without useful divisors, exact/short/long input, unmapped and Unicode characters, missing/corrupt/out-of-range mapping values, read-only output paths, and seeded randomness. Inspect dimensions and pixels with Pillow. Do not commit the generated `output/` directory or virtual environments.
