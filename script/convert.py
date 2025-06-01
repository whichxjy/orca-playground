import re
from pydantic import BaseModel


OUTPUT_NUMBER = 4
RESULT_JOIN_STR = (9 * ("\n" + ("." * 34))) + "\n"
DEFAULT_VELOCITY = "8"
DEFAULT_TEMPLATE = """
#1e=a2e=a3e=a4e=a1e=a2e=a3e=a4e=a#
#................................#
#................................#
#................................#
#................................#
""".strip()


class NodeInfo(BaseModel):
    octave: str
    note: str
    velocity: str


def _number_to_char(n: int) -> str:
    if n <= 9:
        return str(n)  # 0-9 直接返回字符串
    if n <= 35:
        # 10-35 转换为 A-Z
        return chr(ord("A") + n - 10)  # 使用ASCII码转换
    return "Z"  # 如果超出范围，返回最大值 'Z'


def _is_halfwidth(char: str) -> bool:
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


def _parse_music_notation(input_text: str) -> list[str]:
    for c in input_text:
        if not _is_halfwidth(c):
            raise ValueError("invalid input")

    paragraphs = re.split(r"\n\s*\n", input_text.strip())
    all_segments: list[str] = []

    for paragraph in paragraphs:
        lines = [line.strip() for line in paragraph.split("\n") if line.strip()]
        segment_positions = []

        for line in lines:
            line_positions = re.split(r"\s+", line)
            segment_positions.append(line_positions)

        flattened_segment = []
        for row in segment_positions:
            flattened_segment.extend(row)

        if len(flattened_segment) != 32:
            raise ValueError("must be 32 notes each segments")

        all_segments.append(flattened_segment)
    return all_segments


def _convert_note(note_str: str) -> NodeInfo | None:
    if note_str == "x":  # 休止符
        return None

    # 匹配格式: 八度+音符+可选的-+力度
    match = re.match(r"(\d)([A-G][b#]?)(?:-([0-9A-F]+))?", note_str)
    if not match:
        return None

    octave, note, velocity = match.groups()
    octave = int(octave) - 1  # 转换八度表示

    # 处理音符转换
    white_keys = ["C", "D", "E", "F", "G", "A", "B"]
    flat_map = {"Db": "c", "Eb": "d", "Gb": "f", "Ab": "g", "Bb": "a"}
    sharp_map = {"C#": "c", "D#": "d", "F#": "f", "G#": "g", "A#": "a"}

    if note in white_keys:
        converted_note = note
    elif note in flat_map:
        converted_note = flat_map[note]
    elif note in sharp_map:
        converted_note = sharp_map[note]
    else:
        converted_note = note.lower()

    velocity = velocity if velocity else DEFAULT_VELOCITY
    return NodeInfo(octave=str(octave), note=converted_note, velocity=velocity)


def _convert_segment(positions: list[str]) -> str:
    octave_line = ["." for _ in range(32)]
    note_line = ["." for _ in range(32)]
    velocity_line = ["." for _ in range(32)]
    duration_line = ["." for _ in range(32)]

    i = 0
    while i < len(positions):
        pos = positions[i]

        if pos == "~" or pos == "x":
            i += 1
            continue

        # 处理音符
        note_info = _convert_note(pos)
        if not note_info:
            i += 1
            continue

        # 添加音符信息
        octave_line[i] = note_info.octave
        note_line[i] = note_info.note
        velocity_line[i] = note_info.velocity

        # 计算持续时间
        duration = 1
        j = i + 1
        while j < len(positions) and positions[j] == "~":
            duration += 1
            j += 1

        duration_line[i] = _number_to_char(duration)
        i += 1

    # 格式化输出
    header_line = "#1e=a2e=a3e=a4e=a1e=a2e=a3e=a4e=a#"  # 固定的标记行

    result = [
        header_line,
        "#" + "".join(octave_line) + "#",
        "#" + "".join(note_line) + "#",
        "#" + "".join(velocity_line) + "#",
        "#" + "".join(duration_line) + "#",
    ]

    return "\n".join(result)


def convert_music_notation(input_text: str) -> str:
    segments = _parse_music_notation(input_text)

    results: list[str] = []
    for segment in segments:
        segment_result = _convert_segment(segment)
        results.append(segment_result)

    while len(results) < OUTPUT_NUMBER:
        results.append(DEFAULT_TEMPLATE)

    return RESULT_JOIN_STR.join(results)


if __name__ == "__main__":
    input = """
    5C-8	~	~	~	4F-8	~	~	~	4Ab-8	~	~	~	~	~	4Ab-8	4F-8
    ~	~	~	~	~	~	4F-8	~	5Eb-8	~	5Db-8	~	5C-8	~	4Ab-8	~

    2Ab-8	~	3F-8	~	3Ab-8	~	4C-8	~	3C-8	~	3Ab-8	~	4C-8	~	4Eb-8	~
    3Db-8	~	3Ab-8	~	4Db-8	~	4Eb-8	~	2Bb-8	~	3F-8	~	4Db-8	~	4C-8	~
    """
    print(convert_music_notation(input))
