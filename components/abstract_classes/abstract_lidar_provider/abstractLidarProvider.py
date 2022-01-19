from typing import Tuple, Any, Dict, Union
from abc import ABC, abstractmethod


class AbstractLidarProvider(ABC):

    @property
    @abstractmethod
    def info(self) -> Union[Dict[str, Any], None]:
        raise NotImplementedError()

    @property
    @abstractmethod
    def health(self) -> Union[str, None]:
        raise NotImplementedError()

    @property
    @abstractmethod
    def scan_status(self) -> Union[bool, None]:
        raise NotImplementedError()

    @property
    @abstractmethod
    def motor_status(self) -> Union[bool, None]:
        raise NotImplementedError()

    @property
    @abstractmethod
    def connection_status(self) -> bool:
        raise NotImplementedError()

    @property
    @abstractmethod
    def scans(self) -> Union[Tuple[int, float, float], None]:
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