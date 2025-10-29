"""Benchmark script to measure performance improvements."""
import time
from project.avril_14th.input import __patterns__
from script.convert import convert_music_notation


def benchmark_conversion(iterations=100):
    """Benchmark the conversion function."""
    patterns = __patterns__
    
    start = time.perf_counter()
    for _ in range(iterations):
        for pattern in patterns:
            result = convert_music_notation(pattern)
    end = time.perf_counter()
    
    total_time = end - start
    total_conversions = iterations * len(patterns)
    avg_time = total_time / total_conversions
    
    print(f"Performance Benchmark Results")
    print(f"=" * 50)
    print(f"Iterations: {iterations}")
    print(f"Patterns per iteration: {len(patterns)}")
    print(f"Total conversions: {total_conversions}")
    print(f"Total time: {total_time:.4f}s")
    print(f"Average time per conversion: {avg_time*1000:.4f}ms")
    print(f"Conversions per second: {total_conversions/total_time:.2f}")
    
    return total_time, avg_time


if __name__ == "__main__":
    benchmark_conversion()
