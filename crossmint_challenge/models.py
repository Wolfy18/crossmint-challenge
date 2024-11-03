from dataclasses import dataclass
from typing import Literal


@dataclass
class POLYanets:
    row: int
    column: int


@dataclass
class SOLoons:
    row: int
    column: int
    color: Literal["blue", "red", "purple", "white"]


@dataclass
class comETHs:
    row: int
    column: int
    direction: Literal["up", "down", "right", "left"]