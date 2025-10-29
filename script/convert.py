import re
from pydantic import BaseModel


OUTPUT_NUMBER = 4
RESULT_JOIN_STR = (8 * ("\n" + ("." * 34))) + "\n"
DEFAULT_TEMPLATE = """
#1e=a2e=a3e=a4e=a1e=a2e=a3e=a4e=a#
#................................#
#................................#
#................................#
#................................#
""".strip()

# Pre-defined constant dictionaries for note conversion (moved from _convert_note)
WHITE_KEYS = {"C", "D", "E", "F", "G", "A", "B"}
FLAT_MAP = {"Db": "c", "Eb": "d", "Gb": "f", "Ab": "g", "Bb": "a"}
SHARP_MAP = {"C#": "c", "D#": "d", "F#": "f", "G#": "g", "A#": "a"}

# Header line constant (moved from _convert_segment)
HEADER_LINE = "#1e=a2e=a3e=a4e=a1e=a2e=a3e=a4e=a#"

# Compiled regex patterns for better performance
NOTE_PATTERN = re.compile(r"(\d)([A-G][b#]?)-([0-9A-F]+)(?:-([1-9]|[A-Z]))?")
PARAGRAPH_PATTERN = re.compile(r"\n\s*\n")
WHITESPACE_PATTERN = re.compile(r"\s+")


class NodeInfo(BaseModel):
    octave: str
    note: str
    velocity: str
    explicit_duration: str | None


def _number_to_char(n: int) -> str:
    if n <= 9:
        return str(n)  # 0-9 直接返回字符串
    if n <= 35:
        # 10-35 转换为 A-Z
        return chr(ord("A") + n - 10)  # 使用ASCII码转换
    return "Z"  # 如果超出范围，返回最大值 'Z'


def _char_to_number(c: str) -> int:
    if "0" <= c <= "9":
        return int(c)
    if "A" <= c <= "Z":
        return ord(c) - ord("A") + 10
    raise ValueError(f"invalid char for number: {c}")


def _is_halfwidth(char: str) -> bool:
    """Check if a character is halfwidth (more efficient version)."""
    code_point = ord(char)
    # Control characters (U+0000 to U+001F) and DEL (U+007F)
    # ASCII characters (U+0020 to U+007E)
    if code_point <= 0x7E:
        return True
    # Half-width katakana (U+FF61 to U+FF9F)
    if 0xFF61 <= code_point <= 0xFF9F:
        return True
    return False


def _parse_music_notation(input_text: str) -> list[str]:
    """Parse music notation into segments (optimized version)."""
    if not input_text:
        return []

    # Validate all characters are halfwidth (optimized to avoid repeated checks)
    for c in input_text:
        if not _is_halfwidth(c):
            raise ValueError("invalid input")

    paragraphs = PARAGRAPH_PATTERN.split(input_text.strip())
    all_segments: list[str] = []

    for paragraph in paragraphs:
        lines = [line.strip() for line in paragraph.split("\n") if line.strip()]
        
        # Flatten segments more efficiently - use list comprehension
        flattened_segment = [
            position
            for line in lines
            for position in WHITESPACE_PATTERN.split(line)
        ]

        if len(flattened_segment) != 32:
            raise ValueError("must be 32 notes each segments")

        all_segments.append(flattened_segment)
    return all_segments


def _convert_note(note_str: str) -> NodeInfo | None:
    """Convert note string to NodeInfo (optimized version)."""
    if note_str == "x":  # 休止符
        return None

    # 匹配格式: 八度+音符+力度 (using compiled pattern)
    match = NOTE_PATTERN.match(note_str)
    if not match:
        raise ValueError(f"invalid note: {note_str}")

    octave, note, velocity, duration = match.groups()
    octave = int(octave) - 1  # 转换八度表示

    # 处理音符转换 (using module-level constants)
    if note in WHITE_KEYS:
        converted_note = note
    elif note in FLAT_MAP:
        converted_note = FLAT_MAP[note]
    elif note in SHARP_MAP:
        converted_note = SHARP_MAP[note]
    else:
        converted_note = note.lower()

    return NodeInfo(
        octave=str(octave),
        note=converted_note,
        velocity=velocity,
        explicit_duration=duration if duration is not None else None,
    )


def _convert_segment(positions: list[str]) -> str:
    """Convert a segment of positions to Orca format (optimized version)."""
    # Pre-allocate lists with dots
    octave_line = ["."] * 32
    note_line = ["."] * 32
    velocity_line = ["."] * 32
    duration_line = ["."] * 32

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

        # 确定持续时间
        if note_info.explicit_duration is not None:
            # 使用显式指定的持续时间
            duration = _char_to_number(note_info.explicit_duration)
        else:
            # 使用原来的规则计算持续时间
            duration = 1
            j = i + 1
            while j < len(positions) and positions[j] == "~":
                duration += 1
                j += 1

        duration_line[i] = _number_to_char(duration)
        i += 1

    # 格式化输出 - use pre-formatted strings and reduce concatenations
    octave_str = "".join(octave_line)
    note_str = "".join(note_line)
    velocity_str = "".join(velocity_line)
    duration_str = "".join(duration_line)

    return (
        f"{HEADER_LINE}\n"
        f"#{octave_str}#\n"
        f"#{note_str}#\n"
        f"#{velocity_str}#\n"
        f"#{duration_str}#"
    )


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
