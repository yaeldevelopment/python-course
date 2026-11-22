
import math
from decimal import Decimal
from typing import TypeAlias

Number: TypeAlias = int | float | Decimal
Interval: TypeAlias = list[Number] | tuple[Number, Number]


def merge_intervals(
    intervals: list[Interval] | tuple[Interval, ...],
) -> list[list[Number]]:

    if not isinstance(intervals, (list, tuple)):
        raise TypeError("intervals must be a list or tuple")

    validated = []

    for i, interval in enumerate(intervals):

        if not isinstance(interval, (list, tuple)):
            raise TypeError(f"interval {i} must be a list or tuple")

        if len(interval) != 2:
            raise ValueError(f"interval {i} must contain exactly two values")

        start, end = interval

        for value in (start, end):
            if isinstance(value, bool) or not isinstance(
                value, (int, float, Decimal)
            ):
                raise TypeError("Endpoints must be numeric")

            if isinstance(value, float) and not math.isfinite(value):
                raise ValueError("Float values must be finite")

            if isinstance(value, Decimal) and not value.is_finite():
                raise ValueError("Decimal values must be finite")

        if start > end:
            raise ValueError("Start must be <= end")

        validated.append((start, end))

    if not validated:
        return []

    sorted_intervals = sorted(validated)

    merged = []

    for start, end in sorted_intervals:

        if not merged or start > merged[-1][1]:
            merged.append([start, end])

        elif end > merged[-1][1]:
            merged[-1][1] = end

    return merged


# -------------------------
# TESTS
# -------------------------

print("Test 1:")
print(merge_intervals([[1, 3], [2, 6]]))

print("\nTest 2:")
print(merge_intervals([[1, 2], [2, 3]]))

print("\nTest 3:")
print(merge_intervals([[5, 8], [1, 3], [2, 6]]))

print("\nTest 4:")
print(merge_intervals([[1, 2], [4, 5], [7, 10]]))

print("\nTest 5:")
print(merge_intervals([]))

print("\nAll tests completed!")
