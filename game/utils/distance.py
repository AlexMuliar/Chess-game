
from typing import List
from math import sqrt

from position import Position


def euclidian(a: Position, b: Position) -> float:
    return sqrt((a.row - b.row) ** 2 + (a.column - b.column) ** 2)