from typing import List, Tuple, Dict, Union
from models.lidarScanPoint import LidarScanPoint
from models.lidarClusteredScans import LidarClusteredScans
import numpy as np

OBJECT_RADIUS: float = 97*.5


class LidarTrackedObject:
    def __init__(self, points: List[LidarScanPoint], speed: Union[float, int] = .0):
        self.points: List[LidarScanPoint] = points
        self.speed: Union[float, int] = speed
        self.center: Tuple[float, float] = self._calc_center()

    def represent_points_as_tuples(self) -> Dict[str, Union[int, float, Tuple[float, float],
                                                            List[Tuple[float, float, int, float, float]]]]:
        return {
            'points': [point.as_tuple for point in self.points],
            'speed': self.speed,
            'center': self.center,
        }

    def _calc_center(self) -> Tuple[float, float]:
        # return 0, 0
        fp = self.points[0]
        sp = self.points[-1]
        # print(OBJECT_RADIUS, (fp.x - sp.x)*(fp.x - sp.x) + (fp.x - sp.x)*(fp.y - sp.y))
        d = np.sqrt(abs((fp.x - sp.x)*(fp.x - sp.x) + (fp.y - sp.y)*(fp.y - sp.y)))
        h = np.sqrt(abs((OBJECT_RADIUS*OBJECT_RADIUS * (d/2)*(d/2))))
        # print(OBJECT_RADIUS, d, h)
        center1 = (
            fp.x + (sp.x - fp.x) / 2 + h * (sp.y - fp.y)/d,
            fp.y + (sp.y - fp.y) / 2 - h * (sp.x - fp.x) / d,
        )
        center2 = (
            fp.x + (sp.x - fp.x) / 2 - h * (sp.y - fp.y) / d,
            fp.y + (sp.y - fp.y) / 2 + h * (sp.x - fp.x) / d,
        )
        # return center1
        x: float = .0
        y: float = .0
        for point in self.points:
            x += point.x
            y += point.y
        return x/len(self.points) - OBJECT_RADIUS, y/len(self.points)

    def __dict__(self):
        return self.represent_points_as_tuples()
