from script.convert import convert_music_notation
from pathlib import Path
from project.input import __patterns__, __output_path__


total_patterns = len(__patterns__)
num_digits = len(str(total_patterns - 1))

patterns_dir = Path(__output_path__)
patterns_dir.mkdir(parents=True, exist_ok=True)
for i, pattern in enumerate(__patterns__):
    result = convert_music_notation(pattern) + "\n"

    file_path = patterns_dir / f"pattern{i:0{num_digits}d}.orca"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(result)
        print(f"generate pattern: {file_path}")
