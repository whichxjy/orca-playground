pattern1 = """
5C-4	~	~	~	4F-4	~	~	~	4Ab-4	~	~	~	~	~	4Ab-4	4F-4
~	~	~	~	~	~	4F-4	~	5Eb-4	~	5Db-4	~	5C-4	~	4Ab-4	~

2Ab-4	~	3F-4	~	3Ab-4	~	4C-4	~	3C-4	~	3Ab-4	~	4C-4	~	4Eb-4	~
3Db-4	~	3Ab-4	~	4Db-4	~	4Eb-4	~	2Bb-4	~	3F-4	~	4Db-4	~	4C-4	~
"""

pattern2 = """
6C-4	~	~	~	5F-4	~	~	~	5Ab-4	~	~	~	~	~	5Ab-4	5F-4
~	~	~	~	~	~	~	~	~	~	~	~	~	~	~	~

5C-4	~	~	~	4F-4	~	~	~	4Ab-4	~	~	~	~	~	4Ab-4	4F-4
~	~	~	~	~	~	~	~	~	~	~	~	~	~	~	~

2Ab-4	~	3F-4	~	3Ab-4	~	4C-4	~	3C-4	~	3Ab-4	~	4C-4	~	4Eb-4	~
3Db-4	~	3Ab-4	~	4Db-4	~	4Eb-4	~	2Bb-4	~	3F-4	~	4Db-4	~	4C-4	~
"""

pattern3 = """
4C-4	~	~	~	~	~	4C-4	4Eb-4	3Bb-4	~	~	~	~	~	4C-4	~
4C-4	~	~	~	~	~	4C-4	4Eb-4	4F-4	~	~	~	~	~	4Eb-4	~

2Ab-4	~	3Ab-4	~	3F-4	~	3Eb-4	~	2Eb-4	~	3Eb-4	~	3F-4	~	3Eb-4	~
2Ab-4	~	3Ab-4	~	3F-4	~	3Eb-4	~	2Db-4	~	3Db-4	~	3Eb	~	3Db-4	~
"""

__patterns__: list[str] = [pattern1, pattern2, pattern3]
__output_path__ = "project/patterns"
