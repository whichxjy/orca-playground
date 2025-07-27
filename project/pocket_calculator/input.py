pattern0 = """
6C-E	5D#-E	6F#-E	4F-E	6C-E	4G#-E	x	x	x	x	x	x	x	x	x	x
6F#-E	5G-E	5D#-E	4F-E	6C-E	7E-E	6C-E	4A-E	7F-E	x	x	x	x	x	x	x
"""

pattern1 = """
6C-E	x	6C-E	5D#-E	6F#-E	4F-E	6C-E	4G#-E	x	x	x	x	x	x	x	x
x	x	x	x	x	x	x	x	x	x	x	x	x	x	x	x
"""

pattern2 = """
6F#-E	5G-E	5D#-E	4F-E	6C-E	7E-E	6C-E	4A-E	7F-E	x	x	x	x	x	x	x
x	x	x	x	x	x	x	x	x	x	x	x	x	x	x	x
"""

__patterns__: list[str] = [pattern0, pattern1, pattern2]
__output_path__ = "project/pocket_calculator/patterns"
