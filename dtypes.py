"""Library types."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Vec3:
    x: float
    y: float
    z: float


def get_lucky_vec() -> Vec3:
    return Vec3(x=1.0, y=2.0, z=3.0)
