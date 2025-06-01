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

pattern3 = """
4C-A	~	~	~	~	~	4C-A	4Eb-A	3Bb-A	~	~	~	~	~	4C-A	~
4C-A	~	~	~	~	~	4C-A	4Eb-A	4F-A	~	~	~	~	~	4Eb-A	~

2Ab-A	~	3Ab-A	~	3F-A	~	3Eb-A	~	2Eb-A	~	3Eb-A	~	3F-A	~	3Eb-A	~
2Ab-A	~	3Ab-A	~	3F-A	~	3Eb-A	~	2Db-A	~	3Db-A	~	3Eb	~	3Db-A	~
"""

__patterns__: list[str] = [pattern1, pattern2, pattern3]
__output_path__ = "project/patterns"
