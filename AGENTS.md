# AGENTS.md

Guidance for agents working on the small Python text-to-pixel image generator.

## Structure

- `main.py` accepts dimensions/text and renders the output grid with Pillow.
- `colour generator.py` creates the character-to-color mapping.
- `json/sorted_chars.json` is persistent mapping data; changing it changes established visual output.

## Invariants

- Validate positive dimensions and cap pixel/memory allocation before creating an image.
- Define behavior when text length differs from grid capacity; never index past data or silently allocate enormous canvases.
- Preserve Unicode handling and deterministic mapping for characters already in the JSON file.
- Resolve data paths relative to the script/repository, not the caller's current directory.
- Avoid overwriting an existing output without clear user intent.
- The project is marked unmaintained; keep maintenance changes small.

## Validation

Run `python -m py_compile main.py 'colour generator.py'`. Test empty text, one pixel, exact/short/long input, Unicode, missing/corrupt mapping, invalid/huge dimensions, read-only output paths, and deterministic colors. Inspect generated dimensions and pixel values using Pillow. Do not commit generated `output.png` files or virtual environments.
