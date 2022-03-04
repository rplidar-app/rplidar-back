from typing import List, Union, Dict, Optional
from components.work_area_provider.workAreaProvider import WorkAreaProvider
from components.geometry import line_segments_intersection
from models.lidarScanPoint import LidarScanPoint
from models.lidarScans import LidarScans


class PointsFilterService:

    def __init__(self, work_area_provider: WorkAreaProvider):
        self._work_area: WorkAreaProvider = work_area_provider

    def filter(self, points: List[LidarScanPoint]) -> Optional[LidarScans]:
        inside_points: List[LidarScanPoint] = []
        outside_points: List[LidarScanPoint] = []
        for point in points:
            if self.is_point_inside_work_area(point.x, point.y):
                inside_points.append(point)
            else:
                outside_points.append(point)
        return LidarScans(inside=inside_points, outside=outside_points)

    def is_point_inside_work_area(self, x: float, y: float) -> bool:
        intersections_counter: int = 0
        min_x: float = self._work_area.min_x
        for line in self._work_area.none_horizontal_lines:
            if line_segments_intersection(x, y, min_x, y, line[0], line[1], line[2], line[3]):
                intersections_counter += 1
        if intersections_counter % 2 == 0:
            return False
        else:
            return True
