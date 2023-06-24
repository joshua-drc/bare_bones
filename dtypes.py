"""Library types."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Vec4:
    x: float
    y: float
    z: float
    w: float


def get_lucky_vec() -> Vec4:
    return Vec4(x=1.0, y=2.0, z=3.0, w=4.0)
