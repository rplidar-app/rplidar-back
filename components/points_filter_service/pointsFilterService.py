from typing import List, Union, Iterable, Tuple
from components.work_area_provider.workAreaProvider import WorkAreaProvider
from components.geometry import line_segments_intersection


class PointsFilterService:

    def __init__(self, work_area_provider: WorkAreaProvider):
        self._work_area: WorkAreaProvider = work_area_provider

    def filter(self, points: Iterable[Tuple[float, float, int, float, float]]) ->\
            Tuple[
                List[Tuple[float, float, int, float, float]],
                List[Tuple[float, float, int, float, float]]
            ]:
        inside_points: List[Tuple[float, float, int, float, float]] = []
        outside_points: List[Tuple[float, float, int, float, float]] = []
        for point in points:
            if self.is_point_inside_work_area(point[0], point[1]):
                inside_points.append(point)
            else:
                outside_points.append(point)
        return inside_points, outside_points

    def is_point_inside_work_area(self, x: float, y: float) -> bool:
        intersections_counter: int = 0
        min_x: float = self._work_area.min_x
        for line in self._work_area.none_horizontal_lines:
            if line_segments_intersection(x, y, min_x, y, line[0], line[1], line[2], line[3]):
                intersections_counter += 1
        if intersections_counter%2 == 0:
            return False
        else:
            return True
