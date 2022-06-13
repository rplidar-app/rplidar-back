import numpy as np
from typing import List
from sklearn.cluster import DBSCAN
from models.lidarScanPoint import LidarScanPoint
from models.lidarClusteredScans import LidarClusteredScans


class PointsClusteringService:

    def __init__(self):
        self._eps: float = 400  # The maximum distance between two samples for one to be considered as in the
        # neighborhood of the other. This is not a maximum bound on the distances of points within a cluster. This is
        # the most important DBSCAN parameter to choose appropriately for your data set and distance function.
        self._min_samples: int = 5  # The number of samples (or total weight) in a neighborhood for a point to be
        # considered as a core point. This includes the point itself.

    def get_labels(self, points: List[LidarScanPoint]) -> List[int]:
        return self._fake_clustering(points)
        # formatted_points = np.array([point.coords for point in points])
        # clustering: DBSCAN = DBSCAN(eps=self._eps, min_samples=self._min_samples)
        # clustering.fit(formatted_points)
        # return clustering.labels_.tolist()

    def do(self, points: List[LidarScanPoint]) -> LidarClusteredScans:
        labels: List[int] = self.get_labels(points)
        unclustered: List[LidarScanPoint] = []
        clustered: List[List[LidarScanPoint]] = []
        for index, label in enumerate(labels):
            if label == -1:
                unclustered.append(points[index])
            else:
                while len(clustered) <= label:
                    clustered.append([])
                clustered[label].append(points[index])
        return LidarClusteredScans(clustered=clustered, unclustered=unclustered)

    def _fake_clustering(self, points: List[LidarScanPoint]) -> List[int]:
        return [0 for i in range(len(points))]
