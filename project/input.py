pattern0 = """
6C-5	~	~	~	~	~	~	~	6C-5	~	~	~	~	~	~	~
6C-5	~	~	~	~	~	~	~	6C-5	~	~	~	~	~	~	~
"""

pattern1 = """
5C-5	~	~	~	4F-5	~	~	~	4Ab-5	~	~	~	~	~	4Ab-5	4F-5
~	~	~	~	~	~	4F-5	~	5Eb-5	~	5Db-5	~	5C-5	~	4Ab-5	~

2Ab-5	~	3F-5	~	3Ab-5	~	4C-5	~	3C-5	~	3Ab-5	~	4C-5	~	4Eb-5	~
3Db-5	~	3Ab-5	~	4Db-5	~	4Eb-5	~	2Bb-5	~	3F-5	~	4Db-5	~	4C-5	~
"""

pattern2 = """
6C-5	~	~	~	5F-5	~	~	~	5Ab-5	~	~	~	~	~	5Ab-5	5F-5
~	~	~	~	~	~	~	~	~	~	~	~	~	~	~	~

5C-5	~	~	~	4F-5	~	~	~	4Ab-5	~	~	~	~	~	4Ab-5	4F-5
~	~	~	~	~	~	~	~	~	~	~	~	~	~	~	~

2Ab-5	~	3F-5	~	3Ab-5	~	4C-5	~	3C-5	~	3Ab-5	~	4C-5	~	4Eb-5	~
3Db-5	~	3Ab-5	~	4Db-5	~	4Eb-5	~	2Bb-5	~	3F-5	~	4Db-5	~	4C-5	~
"""

pattern3 = """
4C-5	~	~	~	~	~	4C-5	4Eb-5	3Bb-5	~	~	~	~	~	4C-5	~
4C-5	~	~	~	~	~	4C-5	4Eb-5	4F-5	~	~	~	~	~	4Eb-5	~

2Ab-5	~	3Ab-5	~	3F-5	~	3Eb-5	~	2Eb-5	~	3Eb-5	~	3F-5	~	3Eb-5	~
2Ab-5	~	3Ab-5	~	3F-5	~	3Eb-5	~	2Db-5	~	3Db-5	~	3Eb-5	~	3Db-5	~
"""

__patterns__: list[str] = [pattern0, pattern1, pattern2, pattern3]
__output_path__ = "project/patterns"
