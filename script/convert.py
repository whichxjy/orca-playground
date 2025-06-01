import re

def parse_music_notation(input_text):
    """解析输入文本为多个乐段的音符和符号序列"""
    # 按空行分割多个乐段
    paragraphs = re.split(r'\n\s*\n', input_text.strip())
    all_segments = []

    for paragraph in paragraphs:
        lines = [line.strip() for line in paragraph.split('\n') if line.strip()]
        segment_positions = []

        for line in lines:
            # 使用正则表达式拆分，可以处理多个空格和制表符
            line_positions = re.split(r'\s+', line)
            segment_positions.append(line_positions)

        # 展平每个乐段的二维列表
        flattened_segment = []
        for row in segment_positions:
            flattened_segment.extend(row)

        # 确保每个乐段有32个位置
        if len(flattened_segment) != 32:
            raise ValueError(f"每个乐段必须包含32个位置，当前有 {len(flattened_segment)} 个")

        all_segments.append(flattened_segment)

    return all_segments

def convert_note(note_str):
    """转换单个音符格式"""
    if note_str == 'x':  # 休止符
        return None

    # 匹配格式: 八度+音符+可选的-+力度
    match = re.match(r'(\d)([A-G][b#]?)(?:-(\d+))?', note_str)
    if not match:
        return None

    octave, note, velocity = match.groups()
    octave = int(octave) - 1  # 转换八度表示

    # 处理音符转换
    white_keys = ["C", "D", "E", "F", "G", "A", "B"]
    flat_map = {
        "Db": "c",
        "Eb": "d",
        "Gb": "f",
        "Ab": "g",
        "Bb": "a"
    }
    sharp_map = {
        "C#": "c",
        "D#": "d",
        "F#": "f",
        "G#": "g",
        "A#": "a"
    }

    if note in white_keys:
        converted_note = note
    elif note in flat_map:
        converted_note = flat_map[note]
    elif note in sharp_map:
        converted_note = sharp_map[note]
    else:
        converted_note = note.lower()

    velocity = velocity if velocity else "8"  # 默认力度为8

    return {
        "octave": str(octave),
        "note": converted_note,
        "velocity": velocity
    }

def convert_segment(positions):
    """转换单个乐段"""
    # 初始化输出行
    octave_line = ['.' for _ in range(32)]
    note_line = ['.' for _ in range(32)]
    velocity_line = ['.' for _ in range(32)]
    duration_line = ['.' for _ in range(32)]

    i = 0
    while i < len(positions):
        pos = positions[i]

        if pos == '~' or pos == 'x':
            i += 1
            continue

        # 处理音符
        note_info = convert_note(pos)
        if not note_info:
            i += 1
            continue

        # 添加音符信息
        octave_line[i] = note_info["octave"]
        note_line[i] = note_info["note"]
        velocity_line[i] = note_info["velocity"]

        # 计算持续时间
        duration = 1
        j = i + 1
        while j < len(positions) and positions[j] == '~':
            duration += 1
            j += 1

        duration_line[i] = str(duration)
        i += 1

    # 格式化输出
    header_line = "#1e=a2e=a3e=a4e=a1e=a2e=a3e=a4e=a#"  # 固定的标记行

    result = [
        header_line,
        "#" + "".join(octave_line) + "#",
        "#" + "".join(note_line) + "#",
        "#" + "".join(velocity_line) + "#",
        "#" + "".join(duration_line) + "#"
    ]

    return "\n".join(result)

def convert_music_notation(input_text):
    """将自定义音乐文本转换为指定格式，支持多段"""
    segments = parse_music_notation(input_text)

    # 转换每个乐段并合并结果
    results = []
    for segment in segments:
        segment_result = convert_segment(segment)
        results.append(segment_result)

    # 用空行连接多个乐段
    return "\n\n".join(results)

input = """
5C-8	~	~	~	4F-8	~	~	~	4Ab-8	~	~	~	~	~	4Ab-8	4F-8
~	~	~	~	~	~	4F-8	~	5Eb-8	~	5Db-8	~	5C-8	~	4Ab-8	~

2Ab-8	~	3F-8	~	3Ab-8	~	4C-8	~	3C-8	~	3Ab-8	~	4C-8	~	4Eb-8	~
3Db-8	~	3Ab-8		4Db-8	~	4Eb-8		2Bb-8	~	3F-8	~	4Db-8	~	4C-8	~
"""

print(convert_music_notation(input))
