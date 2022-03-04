from typing import Union, Optional, List, Tuple, Dict
from math import cos, sin, pi


DEGREES_TO_RADIANS_FACTOR: float = pi / 180


class LidarScanPoint:

    def __init__(self, quality: int, angle: float, distance: float, x: Optional[float] = None,
                 y: Optional[float] = None):
        self.quality: int = quality
        self.angle: float = angle
        self.distance: float = distance
        self.x: float = x
        self.y: float = y
        if self.x is None or self.y is None:
            self._calc_coordinates()

    def _calc_coordinates(self) -> None:
        self.x = -self.distance * cos(self.angle*DEGREES_TO_RADIANS_FACTOR)
        self.y = -self.distance * sin(self.angle*DEGREES_TO_RADIANS_FACTOR)

    @property
    def coords(self) -> Tuple[float, float]:
        return self.x, self.y

    @property
    def as_dict(self) -> Dict[str, Union[float, int]]:
        return {
            'x': self.x,
            'y': self.y,
            'quality': self.quality,
            'angle': self.angle,
            'distance': self.distance,
        }

    @property
    def as_tuple(self) -> Tuple[float, float, int, float, float]:
        return self.x, self.y, self.quality, self.angle, self.distance
