from script.convert import convert_music_notation
from pathlib import Path

pattern1 = """
5C-8	~	~	~	4F-8	~	~	~	4Ab-8	~	~	~	~	~	4Ab-8	4F-8
~	~	~	~	~	~	4F-8	~	5Eb-8	~	5Db-8	~	5C-8	~	4Ab-8	~

2Ab-8	~	3F-8	~	3Ab-8	~	4C-8	~	3C-8	~	3Ab-8	~	4C-8	~	4Eb-8	~
3Db-8	~	3Ab-8	~	4Db-8	~	4Eb-8	~	2Bb-8	~	3F-8	~	4Db-8	~	4C-8	~
"""

pattern2 = """
6C-A	x	x	x	5F-A	~	~	~	5Ab-A	~	~	~	~	~	5Ab-A	5F-A
~	~	~	~	~	~	~	~	~	~	~	~	~	~	~	~

5C-A	x	x	x	4F-A	~	~	~	4Ab-A	~	~	~	~	~	4Ab-A	4F-A
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
