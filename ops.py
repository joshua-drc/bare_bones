"""Library operations."""

from .auth import _check_token
from .dtypes import Vec4


def add_vec(token: str, v1: Vec4, v2: Vec4) -> Vec4:
    _check_token(token)
    return Vec4(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z, v1.w + v2.w)


def mag_vec(token: str, v: Vec4) -> float:
    _check_token(token)
    return (v.x * v.x + v.y * v.y + v.z * v.z + v.w * v.w) ** 0.5
