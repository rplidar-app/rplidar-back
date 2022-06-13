from typing import List, Tuple, Dict, Union, Optional
from models.lidarScanPoint import LidarScanPoint
from models.lidarTrackedObject import LidarTrackedObject


class LidarScan:
    def __init__(self,
                 points_inside_work_area: List[LidarScanPoint] = [],
                 points_outside_work_area: List[LidarScanPoint] = [],
                 cluster_labels: List[int] = []):
        self.untracked_points: List[LidarScanPoint] = points_outside_work_area[:]
        self.ungrouped_points: List[LidarScanPoint] = []
        self.objects: List[LidarTrackedObject] = []
        self._group_points(points_inside_work_area, cluster_labels)

    def _group_points(self, points: List[LidarScanPoint], labels: List[int]):
        groups: List[List[LidarScanPoint]] = []
        for i in range(len(labels)):
            if labels[i] == -1:
                self.ungrouped_points.append(points[i])
            else:
                while labels[i] >= len(groups):
                    groups.append([])
                groups[labels[i]].append(points[i])
        for group in groups:
            self.objects.append(LidarTrackedObject(points=group, speed=.0))

    def represent_points_as_tuples(self) -> Dict[str, Union[List[int], List[Tuple[float, float, int, float, float]]]]:
        return {
            'untracked_points': [point.as_tuple for point in self.untracked_points],
            'ungrouped_points': [point.as_tuple for point in self.ungrouped_points],
            'objects': [obj.represent_points_as_tuples() for obj in self.objects]
        }
