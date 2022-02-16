from typing import Tuple, Any, Dict, Union, Iterable, List
from components.abstract_classes.abstract_lidar_provider.abstractLidarProvider import AbstractLidarProvider


class FakeRpLidarProvider(AbstractLidarProvider):

    def __init__(self, port: str, baud_rate: int = 115200, timeout=1):
        super().__init__(port, baud_rate, timeout)
        self.grabbed_data: List[List[Tuple[float, float, int, float, float]]] = []
        self.counter = 0
        self._load_grabbed_data_from_json()

    def _load_grabbed_data_from_json(self):
        import json
        with open('./components/lidar_providers/fake_rplidar_provider/data.json') as f:
            self.grabbed_data = json.load(f)

    @property
    def info(self) -> Union[Dict[str, Any], None]:
        return None

    @property
    def health(self) -> Union[str, None]:
        return 'Fake lidar health is fucking amazing!'

    @property
    def scans(self) -> Union[Iterable[Tuple[float, float, int, float, float]], None]:
        scan = self.grabbed_data[self.counter]
        self.counter += 1
        if self.counter >= len(self.grabbed_data):
            self.counter = 0
        return scan

    def connect(self) -> bool:
        return True

    def disconnect(self) -> None:
        return

    def start_scan(self) -> bool:
        return True

    def stop_scan(self) -> None:
        return

    def start_motor(self) -> bool:
        return True

    def stop_motor(self) -> None:
        return

    def reset(self) -> None:
        return


if __name__ == '__main__'"":
    LIDAR_PORT: str = 'COM4'  # '/dev/ttyUSB0'
    lidar = FakeRpLidarProvider(LIDAR_PORT)
    print(lidar.info)
    print(lidar.health)
    print(lidar.scans)
