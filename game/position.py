from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Position:
    row: int
    column: int