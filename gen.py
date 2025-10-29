"""Generate Orca pattern files from music notation.

This script processes music notation patterns and converts them to Orca format.
It supports processing multiple projects efficiently.
"""
from pathlib import Path
import sys

from project.avril_14th.input import __output_path__, __patterns__
from script.convert import convert_music_notation


def generate_patterns(patterns: list[str], output_path: str) -> None:
    """Generate pattern files from music notation.
    
    Args:
        patterns: List of music notation patterns to convert
        output_path: Directory path where pattern files will be saved
    """
    total_patterns = len(patterns)
    num_digits = len(str(total_patterns - 1))

    patterns_dir = Path(output_path)
    patterns_dir.mkdir(parents=True, exist_ok=True)
    
    for i, pattern in enumerate(patterns):
        result = convert_music_notation(pattern) + "\n"

        file_path = patterns_dir / f"pattern{i:0{num_digits}d}.orca"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"generate pattern: {file_path}")


def main():
    """Main entry point for the pattern generator."""
    # Currently processes avril_14th project
    # Can be extended to process multiple projects
    generate_patterns(__patterns__, __output_path__)


if __name__ == "__main__":
    main()

