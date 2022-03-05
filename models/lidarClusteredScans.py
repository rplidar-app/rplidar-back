from typing import List, Optional
from models.lidarScanPoint import LidarScanPoint


class LidarClusteredScans:

    def __init__(self, unclustered: Optional[List[LidarScanPoint]] = None,
                 clustered: Optional[List[List[LidarScanPoint]]] = None):
        if unclustered is None:
            unclustered = []
        if clustered is None:
            clustered = []
        self.unclustered: List[LidarScanPoint] = unclustered[:]
        self.clustered: List[List[LidarScanPoint]] = clustered[:]
