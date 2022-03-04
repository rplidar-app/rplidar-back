from typing import List, Tuple, Dict
from models.lidarScanPoint import LidarScanPoint


class LidarScans:
    def __init__(self, inside=None, outside=None):
        if outside is None:
            outside = []
        if inside is None:
            inside = []
        self.inside: List[LidarScanPoint] = inside[:]
        self.outside: List[LidarScanPoint] = outside[:]

    def represent_points_as_tuples(self) -> Dict[str, List[Tuple[float, float, int, float, float]]]:
        return {
            'inside': [scan.as_tuple for scan in self.inside],
            'outside': [scan.as_tuple for scan in self.outside]
        }
