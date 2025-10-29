"""Test suite for the convert module."""
import pytest
from script.convert import (
    _number_to_char,
    _char_to_number,
    _is_halfwidth,
    _parse_music_notation,
    _convert_note,
    _convert_segment,
    convert_music_notation,
)


class TestNumberToChar:
    """Tests for _number_to_char function."""

    def test_single_digit(self):
        assert _number_to_char(0) == "0"
        assert _number_to_char(5) == "5"
        assert _number_to_char(9) == "9"

    def test_letters(self):
        assert _number_to_char(10) == "A"
        assert _number_to_char(15) == "F"
        assert _number_to_char(35) == "Z"

    def test_overflow(self):
        assert _number_to_char(36) == "Z"
        assert _number_to_char(100) == "Z"


class TestCharToNumber:
    """Tests for _char_to_number function."""

    def test_digits(self):
        assert _char_to_number("0") == 0
        assert _char_to_number("5") == 5
        assert _char_to_number("9") == 9

    def test_letters(self):
        assert _char_to_number("A") == 10
        assert _char_to_number("F") == 15
        assert _char_to_number("Z") == 35

    def test_invalid_char(self):
        with pytest.raises(ValueError):
            _char_to_number("a")
        with pytest.raises(ValueError):
            _char_to_number("@")


class TestIsHalfwidth:
    """Tests for _is_halfwidth function."""

    def test_control_chars(self):
        assert _is_halfwidth("\n")
        assert _is_halfwidth("\t")
        assert _is_halfwidth("\x00")

    def test_ascii_chars(self):
        assert _is_halfwidth("A")
        assert _is_halfwidth("z")
        assert _is_halfwidth("0")
        assert _is_halfwidth(" ")
        assert _is_halfwidth("~")

    def test_halfwidth_katakana(self):
        assert _is_halfwidth("\uff61")  # Halfwidth katakana
        assert _is_halfwidth("\uff9f")  # Halfwidth katakana

    def test_fullwidth_chars(self):
        assert not _is_halfwidth("あ")
        assert not _is_halfwidth("漢")
        assert not _is_halfwidth("Ａ")  # Fullwidth A


class TestParseMusicNotation:
    """Tests for _parse_music_notation function."""

    def test_empty_input(self):
        assert _parse_music_notation("") == []

    def test_single_segment(self):
        input_text = """
        5C-8 ~ ~ ~ 4F-8 ~ ~ ~ 4Ab-8 ~ ~ ~ ~ ~ 4Ab-8 4F-8
        ~ ~ ~ ~ ~ ~ 4F-8 ~ 5Eb-8 ~ 5Db-8 ~ 5C-8 ~ 4Ab-8 ~
        """
        result = _parse_music_notation(input_text)
        assert len(result) == 1
        assert len(result[0]) == 32

    def test_multiple_segments(self):
        input_text = """
        5C-8 ~ ~ ~ 4F-8 ~ ~ ~ 4Ab-8 ~ ~ ~ ~ ~ 4Ab-8 4F-8
        ~ ~ ~ ~ ~ ~ 4F-8 ~ 5Eb-8 ~ 5Db-8 ~ 5C-8 ~ 4Ab-8 ~

        2Ab-8 ~ 3F-8 ~ 3Ab-8 ~ 4C-8 ~ 3C-8 ~ 3Ab-8 ~ 4C-8 ~ 4Eb-8 ~
        3Db-8 ~ 3Ab-8 ~ 4Db-8 ~ 4Eb-8 ~ 2Bb-8 ~ 3F-8 ~ 4Db-8 ~ 4C-8 ~
        """
        result = _parse_music_notation(input_text)
        assert len(result) == 2
        assert all(len(segment) == 32 for segment in result)

    def test_invalid_segment_length(self):
        input_text = "5C-8 ~ ~ ~"  # Only 4 notes, not 32
        with pytest.raises(ValueError, match="must be 32 notes"):
            _parse_music_notation(input_text)

    def test_fullwidth_char(self):
        input_text = "あ"
        with pytest.raises(ValueError, match="invalid input"):
            _parse_music_notation(input_text)


class TestConvertNote:
    """Tests for _convert_note function."""

    def test_rest(self):
        assert _convert_note("x") is None

    def test_white_key(self):
        note = _convert_note("5C-8")
        assert note.octave == "4"
        assert note.note == "C"
        assert note.velocity == "8"
        assert note.explicit_duration is None

    def test_flat_note(self):
        note = _convert_note("4Ab-5")
        assert note.octave == "3"
        assert note.note == "g"
        assert note.velocity == "5"

    def test_sharp_note(self):
        note = _convert_note("5C#-A")
        assert note.octave == "4"
        assert note.note == "c"
        assert note.velocity == "A"

    def test_explicit_duration(self):
        note = _convert_note("5C-8-5")
        assert note.octave == "4"
        assert note.note == "C"
        assert note.velocity == "8"
        assert note.explicit_duration == "5"

    def test_invalid_note(self):
        with pytest.raises(ValueError, match="invalid note"):
            _convert_note("invalid")


class TestConvertSegment:
    """Tests for _convert_segment function."""

    def test_empty_positions(self):
        positions = ["x"] * 32
        result = _convert_segment(positions)
        assert "#................................#" in result

    def test_single_note(self):
        positions = ["5C-8"] + ["x"] * 31
        result = _convert_segment(positions)
        lines = result.split("\n")
        assert lines[1].startswith("#4")
        assert lines[2].startswith("#C")
        assert lines[3].startswith("#8")
        assert lines[4].startswith("#1")

    def test_note_with_tie(self):
        positions = ["5C-8", "~", "~"] + ["x"] * 29
        result = _convert_segment(positions)
        lines = result.split("\n")
        # First position should have duration 3
        assert lines[4][1] == "3"


class TestConvertMusicNotation:
    """Tests for convert_music_notation function."""

    def test_basic_conversion(self):
        input_text = """
        5C-8 ~ ~ ~ 4F-8 ~ ~ ~ 4Ab-8 ~ ~ ~ ~ ~ 4Ab-8 4F-8
        ~ ~ ~ ~ ~ ~ 4F-8 ~ 5Eb-8 ~ 5Db-8 ~ 5C-8 ~ 4Ab-8 ~
        """
        result = convert_music_notation(input_text)
        assert isinstance(result, str)
        assert "#1e=a2e=a3e=a4e=a1e=a2e=a3e=a4e=a#" in result

    def test_multiple_segments(self):
        input_text = """
        5C-8 ~ ~ ~ 4F-8 ~ ~ ~ 4Ab-8 ~ ~ ~ ~ ~ 4Ab-8 4F-8
        ~ ~ ~ ~ ~ ~ 4F-8 ~ 5Eb-8 ~ 5Db-8 ~ 5C-8 ~ 4Ab-8 ~

        2Ab-8 ~ 3F-8 ~ 3Ab-8 ~ 4C-8 ~ 3C-8 ~ 3Ab-8 ~ 4C-8 ~ 4Eb-8 ~
        3Db-8 ~ 3Ab-8 ~ 4Db-8 ~ 4Eb-8 ~ 2Bb-8 ~ 3F-8 ~ 4Db-8 ~ 4C-8 ~
        """
        result = convert_music_notation(input_text)
        # Should have at least 2 segments worth of content
        segment_count = result.count("#1e=a2e=a3e=a4e=a1e=a2e=a3e=a4e=a#")
        assert segment_count >= 2

    def test_padding_with_defaults(self):
        # Test with only 1 segment (should pad to OUTPUT_NUMBER)
        input_text = """
        5C-8 ~ ~ ~ 4F-8 ~ ~ ~ 4Ab-8 ~ ~ ~ ~ ~ 4Ab-8 4F-8
        ~ ~ ~ ~ ~ ~ 4F-8 ~ 5Eb-8 ~ 5Db-8 ~ 5C-8 ~ 4Ab-8 ~
        """
        result = convert_music_notation(input_text)
        # Should have OUTPUT_NUMBER (4) segments
        segment_count = result.count("#1e=a2e=a3e=a4e=a1e=a2e=a3e=a4e=a#")
        assert segment_count == 4


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
