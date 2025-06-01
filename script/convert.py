import re

def convert_notes(input_notes: list[str]) -> list[str]:
    # 白键列表
    white_keys = ["C", "D", "E", "F", "G", "A", "B"]
    # 降号到前一个白键的映射
    flat_map = {
        "Db": "c",
        "Eb": "d",
        "Gb": "f",
        "Ab": "g",
        "Bb": "a"
    }
    # 升号到当前白键的小写
    sharp_map = {
        "C#": "c",
        "D#": "d",
        "F#": "f",
        "G#": "g",
        "A#": "a"
    }

    result = []
    for note in input_notes:
        octave = int(note[0]) - 1
        key = note[1:]

        if key in white_keys:
            new_note = f"{octave}{key}"
        elif key in flat_map:
            new_note = f"{octave}{flat_map[key]}"
        elif key in sharp_map:
            new_note = f"{octave}{sharp_map[key]}"
        else:
            # 其他情况直接小写
            new_note = f"{octave}{key.lower()}"
        result.append(new_note)
    return result


raw = """
2Ab	~	3F	~	3Ab	~	4C	~	3C	~	3Ab	~	4C	~	4Eb	~
3Db	~	3Ab		4Db	~	4Eb		2Bb	~	3F	~	4Db	~	4C	~
"""

notes = [n.strip() for n in re.split(r'[~\s]+', raw) if n.strip()]

converted = convert_notes(notes)
for n in converted:
    print(n)
