from typing import List, Tuple, Dict, Union
from models.lidarScanPoint import LidarScanPoint
from models.lidarClusteredScans import LidarClusteredScans


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
        x: float = .0
        y: float = .0
        for point in self.points:
            x += point.x
            y += point.y
        return x/len(self.points), y/len(self.points)

    def __dict__(self):
        return self.represent_points_as_tuples()
