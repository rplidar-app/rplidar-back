from typing import Any, Dict, Union, List, Optional
from abc import ABC, abstractmethod
from math import pi
from models.lidarScans import LidarScans
from components.work_area_provider.workAreaProvider import WorkAreaProvider
from components.points_filter_service.pointsFilterService import PointsFilterService
from components.points_clustering_service.pointsClusteringService import PointsClusteringService

DEGREES_TO_RADIANS_FACTOR: float = pi / 180


class AbstractLidarProvider(ABC):

    def __init__(self, work_area_provider: WorkAreaProvider, port: str, baud_rate: int = 115200, timeout=1, ):
        self._port: str = port
        self._baud_rate: int = baud_rate
        self._timeout: int = timeout
        self._motor_status: Union[bool, None] = None
        self._scan_status: Union[bool, None] = None
        self._connection_status: bool = False
        self._work_area: WorkAreaProvider = work_area_provider
        self._filter: PointsFilterService = PointsFilterService(self._work_area)
        self._clustering: PointsClusteringService = PointsClusteringService()

    @property
    @abstractmethod
    def info(self) -> Union[Dict[str, Any], None]:
        raise NotImplementedError()

    @property
    @abstractmethod
    def health(self) -> Union[str, None]:
        raise NotImplementedError()

    @property
    def scan_status(self) -> Union[bool, None]:
        return self._scan_status

    @property
    def motor_status(self) -> bool:
        return self._motor_status

    @property
    def connection_status(self) -> bool:
        return self._connection_status

    @property
    @abstractmethod
    def scans(self) -> Optional[LidarScans]:
        """
            :return: Lidar scans
        """
        raise NotImplementedError()

    @abstractmethod
    def connect(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def disconnect(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def start_scan(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def stop_scan(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def start_motor(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def stop_motor(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def reset(self) -> None:
        raise NotImplementedError()
