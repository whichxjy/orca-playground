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

pattern4 = """
4C-5	~	~	~	~	~	4C-5	4Eb-5	3Bb-6	~	~	~	~	~	4C-7	~
4C-7	~	~	~	~	~	4C-8	4Eb-8	4F-9	~	~	~	~	~	4Eb-A	~

2Ab-5	~	3Ab-5	~	3F-5	~	3Eb-5	~	2Eb-6	~	3Eb-6	~	3F-7	~	3Eb-7	~
2Ab-7	~	3Ab-7	~	3F-8	~	3Eb-8	~	2Db-9	~	3Db-9	~	3Eb-A	~	3Db-A	~
"""

pattern5 = """
4Db-A	~	5F-A	~	5G-A	~	5Ab-A	~	6C-A	~	5G-A	~	~	~	~	~
~	~	5F-A	~	5G-A	~	5Ab-A	~	6C-A	~	5G-A	~	5F-A-6	~	~	~

x	x	4F-A	~	4G-A	~	4Ab-A	~	5C-A	~	4G-A	~	~	~	~	~
~	~	4F-A	~	4G-A	~	4Ab-A	~	5C-A	~	4G-A	~	4F-A-6	~	~	~
"""

pattern6 = """
x	x	5F-A	~	5G-A	~	5Ab-A	~	6C-A	~	5G-A	~	~	~	~	~
~	~	5F-A	~	5G-A	~	5Ab-9	~	6C-8	~	~	5G-7	~	5F-6	~	~

x	x	4F-A	~	4G-A	~	4Ab-A	~	5C-A	~	4G-A	~	~	~	~	~
~	~	4F-A	~	4G-A	~	4Ab-9	~	5C-8	~	~	4G-7	~	4F-6	~	~
"""

__patterns__: list[str] = [
    pattern0,
    pattern1,
    pattern2,
    pattern3,
    pattern4,
    pattern5,
    pattern6,
]
__output_path__ = "project/patterns"
