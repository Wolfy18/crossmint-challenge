from dataclasses import dataclass
from typing import Literal


@dataclass
class POLYanet:
    row: int
    column: int


@dataclass
class SOLoon:
    row: int
    column: int
    color: Literal["blue", "red", "purple", "white"]


@dataclass
class ComETH:
    row: int
    column: int
    direction: Literal["up", "down", "right", "left"]