from typing import List, Tuple, Dict, Optional, Union
from models.lidarScanPoint import LidarScanPoint
from models.lidarClusteredScans import LidarClusteredScans


class LidarScans:
    def __init__(self,
                 inside: Optional[List[LidarScanPoint]] = None,
                 outside: Optional[List[LidarScanPoint]] = None,
                 cluster_labels: Optional[List[int]] = None):
        if outside is None:
            outside = []
        if inside is None:
            inside = []
        if cluster_labels is None:
            cluster_labels = []
        self.outside: List[LidarScanPoint] = outside[:]
        self.inside: List[LidarScanPoint] = inside[:]
        self.cluster_labels: List[int] = cluster_labels[:]

    def represent_points_as_tuples(self) -> Dict[str, Union[List[int], List[Tuple[float, float, int, float, float]]]]:
        return {
            'inside': [scan.as_tuple for scan in self.inside],
            'outside': [scan.as_tuple for scan in self.outside],
            'cluster_labels': self.cluster_labels
        }
