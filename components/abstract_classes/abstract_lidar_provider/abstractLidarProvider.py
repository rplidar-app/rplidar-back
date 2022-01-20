from typing import Tuple, Any, Dict, Union, Iterable
from abc import ABC, abstractmethod


class AbstractLidarProvider(ABC):

    def __init__(self, port: str, baud_rate: int = 115200, timeout=1):
        self._port: str = port
        self._baud_rate: int = baud_rate
        self._timeout: int = timeout
        self._motor_status: Union[bool, None] = None
        self._scan_status: Union[bool, None] = None
        self._connection_status: bool = False

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
    def scans(self) -> Union[Iterable[tuple[bool, int, float, float]], None]:
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
