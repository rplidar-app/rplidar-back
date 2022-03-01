from typing import Tuple, Any, Dict, Union, Iterable, List
from abc import ABC, abstractmethod
from math import cos, sin, pi
from components.work_area_provider.workAreaProvider import WorkAreaProvider


DEGREES_TO_RADIANS_FACTOR: float = pi/180


class AbstractLidarProvider(ABC):

    def __init__(self, work_area_provider: WorkAreaProvider, port: str, baud_rate: int = 115200, timeout=1, ):
        self._port: str = port
        self._baud_rate: int = baud_rate
        self._timeout: int = timeout
        self._motor_status: Union[bool, None] = None
        self._scan_status: Union[bool, None] = None
        self._connection_status: bool = False
        self._work_area: WorkAreaProvider = work_area_provider

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
    def scans(self) -> Union[Iterable[Tuple[float, float, int, float, float]], None]:
        """
            :return: a list of tuples. Every tuple contains: x, y, quality, angle, distance
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

    @staticmethod
    def _get_coordinates(angle: float, distance: float) -> Tuple[float, float]:
        """
        A method that calculates X and Y coordinates of the point given by angle and distance
        :param angle: an angle of the point in radians
        :param distance: a distance from the centre of the lidar to the point
        :return: a tuple containing X and Y coordinates of the given point
        """
        return -distance*cos(angle*DEGREES_TO_RADIANS_FACTOR), -distance*sin(angle*DEGREES_TO_RADIANS_FACTOR)

    @staticmethod
    def _convert_point_to_output_format(quality: int, angle: float, distance: float) -> Tuple[float, float, int, float,
                                                                                              float]:
        """
        A static method that converts point to the output data format with adding calculated X and Y coordinates of the
        input point
        :param quality:
        :param angle:
        :param distance:
        :return: a tuple containing X and Y coordinates, quality, angle and distance of the given point
        """
        x, y = AbstractLidarProvider._get_coordinates(angle, distance)
        return x, y, quality, angle, distance
