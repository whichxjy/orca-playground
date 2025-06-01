pattern1 = """
5C-3	~	~	~	4F-3	~	~	~	4Ab-3	~	~	~	~	~	4Ab-3	4F-3
~	~	~	~	~	~	4F-3	~	5Eb-3	~	5Db-3	~	5C-3	~	4Ab-3	~

2Ab-3	~	3F-3	~	3Ab-3	~	4C-3	~	3C-3	~	3Ab-3	~	4C-3	~	4Eb-3	~
3Db-3	~	3Ab-3	~	4Db-3	~	4Eb-3	~	2Bb-3	~	3F-3	~	4Db-3	~	4C-3	~
"""

pattern2 = """
6C-3	~	~	~	5F-3	~	~	~	5Ab-3	~	~	~	~	~	5Ab-3	5F-3
~	~	~	~	~	~	~	~	~	~	~	~	~	~	~	~

5C-3	~	~	~	4F-3	~	~	~	4Ab-3	~	~	~	~	~	4Ab-3	4F-3
~	~	~	~	~	~	~	~	~	~	~	~	~	~	~	~

2Ab-3	~	3F-3	~	3Ab-3	~	4C-3	~	3C-3	~	3Ab-3	~	4C-3	~	4Eb-3	~
3Db-3	~	3Ab-3	~	4Db-3	~	4Eb-3	~	2Bb-3	~	3F-3	~	4Db-3	~	4C-3	~
"""

pattern3 = """
4C-3	~	~	~	~	~	4C-3	4Eb-3	3Bb-3	~	~	~	~	~	4C-3	~
4C-3	~	~	~	~	~	4C-3	4Eb-3	4F-3	~	~	~	~	~	4Eb-3	~

2Ab-3	~	3Ab-3	~	3F-3	~	3Eb-3	~	2Eb-3	~	3Eb-3	~	3F-3	~	3Eb-3	~
2Ab-3	~	3Ab-3	~	3F-3	~	3Eb-3	~	2Db-3	~	3Db-3	~	3Eb	~	3Db-3	~
"""

__patterns__: list[str] = [pattern1, pattern2, pattern3]
__output_path__ = "project/patterns"
