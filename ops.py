"""Library operations."""

from .auth import _check_token
from .dtypes import Vec3


def add_vec(token: str, v1: Vec3, v2: Vec3) -> Vec3:
    _check_token(token)
    return Vec3(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)


def mag_vec(token: str, v: Vec3) -> float:
    _check_token(token)
    return (v.x * v.x + v.y * v.y + v.z * v.z) ** 0.5
