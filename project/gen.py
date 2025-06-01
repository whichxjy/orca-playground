from script.convert import convert_music_notation
from pathlib import Path

pattern1 = """
5C-8	~	~	~	4F-8	~	~	~	4Ab-8	~	~	~	~	~	4Ab-8	4F-8
~	~	~	~	~	~	4F-8	~	5Eb-8	~	5Db-8	~	5C-8	~	4Ab-8	~

2Ab-9	~	3F-9	~	3Ab-9	~	4C-9	~	3C-9	~	3Ab-9	~	4C-9	~	4Eb-9	~
3Db-9	~	3Ab-9	~	4Db-9	~	4Eb-9	~	2Bb-9	~	3F-9	~	4Db-9	~	4C-9	~
"""

pattern2 = """
6C-A	~	~	~	5F-A	~	~	~	5Ab-A	~	~	~	~	~	5Ab-A	5F-A
~	~	~	~	~	~	~	~	~	~	~	~	~	~	~	~

5C-A	~	~	~	4F-A	~	~	~	4Ab-A	~	~	~	~	~	4Ab-A	4F-A
~	~	~	~	~	~	~	~	~	~	~	~	~	~	~	~

2Ab-A	~	3F-A	~	3Ab-A	~	4C-A	~	3C-A	~	3Ab-A	~	4C-A	~	4Eb-A	~
3Db-A	~	3Ab-A	~	4Db-A	~	4Eb-A	~	2Bb-A	~	3F-A	~	4Db-A	~	4C-A	~
"""

patterns: list[str] = [pattern1, pattern2]

patterns_dir = Path("project/patterns")
patterns_dir.mkdir(parents=True, exist_ok=True)
for i, pattern in enumerate(patterns, start=1):
    result = convert_music_notation(pattern)

    file_path = patterns_dir / f"pattern{i}.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(result)
        print(f"generate pattern: {file_path}")
