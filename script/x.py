def is_halfwidth(char):
    # 控制字符 (U+0000 到 U+001F) 和 DEL (U+007F)
    if ord(char) <= 0x1F or ord(char) == 0x7F:
        return True
    # ASCII字符 (U+0020 到 U+007E)
    if 0x20 <= ord(char) <= 0x7E:
        return True
    # 半角片假名 (U+FF61 到 U+FF9F)
    if 0xFF61 <= ord(char) <= 0xFF9F:
        return True
    return False

def parse_music_notation(input_text):
    """解析输入文本为多个乐段的音符和符号序列"""
    for c in input_text:
        if not is_halfwidth(c):
            print(f"非半角字符: '{c}' (Unicode: U+{ord(c):04X})")
            raise ValueError("invalid input")


input = """
5C-8	~	~	~	4F-8	~	~	~	4Ab-8	~	~	~	~	~	4Ab-8	4F-8
~	~	~	~	~	~	4F-8	~	5Eb-8	~	5Db-8	~	5C-8	~	4Ab-8	~

2Ab-8	~	3F-8	~	3Ab-8	~	4C-8	~	3C-8	~	3Ab-8	~	4C-8	~	4Eb-8	~
3Db-8	~	3Ab-8	~	4Db-8	~	4Eb-8	~	2Bb-8	~	3F-8	~	4Db-8	~	4C-8	~
"""

print(parse_music_notation(input))
