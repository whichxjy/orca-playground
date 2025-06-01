import re

def parse_music_notation(input_text):
    """解析输入文本为音符和符号序列"""
    lines = [line.strip() for line in input_text.strip().split('\n') if line.strip()]
    all_positions = []

    for line in lines:
        line_positions = re.split(r'\s+', line)
        all_positions.append(line_positions)

    # 展平二维列表
    flattened_positions = []
    for row in all_positions:
        flattened_positions.extend(row)

    # 检查总位置是否为32个
    if len(flattened_positions) != 32:
        raise ValueError(f"输入必须包含32个位置，当前有 {len(flattened_positions)} 个")

    return flattened_positions

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

def convert_music_notation(input_text):
    """将自定义音乐文本转换为指定格式"""
    positions = parse_music_notation(input_text)

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



input_text = """
5C-8	~	~	~	4F-8	~	~	~	4Ab-8	~	~	~	~	~	4Ab-8	4F-8
~	~	~	~	~	~	4F-8	~	5Eb-8	~	5Db-8	~	5C-8	~	4Ab-8	~
"""

print(convert_music_notation(input_text))
