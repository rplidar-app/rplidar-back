from typing import List, Tuple, Dict, Union
from models.lidarScanPoint import LidarScanPoint
from models.lidarClusteredScans import LidarClusteredScans


class LidarTrackedObject:
    def __init__(self, points: List[LidarScanPoint], speed: Union[float, int] = .0):
        self.points: List[LidarScanPoint] = points
        self.speed: Union[float, int] = speed

    def represent_points_as_tuples(self) -> Dict[str, Union[int, float, List[Tuple[float, float, int, float, float]]]]:
        return {
            'points': [point.as_tuple for point in self.points],
            'speed': self.speed,
        }

    def __dict__(self):
        return self.represent_points_as_tuples()
