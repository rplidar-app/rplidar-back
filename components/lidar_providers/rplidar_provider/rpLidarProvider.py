from typing import Tuple, Any, Dict, Union, Iterable, List
import threading
from rplidar import RPLidar, RPLidarException
from components.abstract_classes.abstract_lidar_provider.abstractLidarProvider import AbstractLidarProvider


class RpLidarProvider(AbstractLidarProvider):

    def __init__(self, port: str, baud_rate: int = 115200, timeout=1):
        super().__init__(port, baud_rate, timeout)
        self._info: Union[Dict[str, Any], None] = None
        self._health: Union[str, None] = None
        self._lidar_instance: Union[RPLidar, None] = None
        self._lidar_polling_thread: Union[threading.Thread, None] = None
        self._data_buffer = []
        self._data_buffer_lock = threading.Lock()
        self._scan_status_lock = threading.Lock()
        self._lidar_instance_lock = threading.Lock()

    def _poll_lidar_scans(self):
        try:
            with self._lidar_instance_lock:
                for scan in self._lidar_instance.iter_scans():
                    local_data = []
                    for point in scan:
                        with self._scan_status_lock:
                            if self._scan_status is False:
                                self._lidar_instance.stop()
                                break
                        local_data.append(point)
                    with self._data_buffer_lock:
                        self._data_buffer = local_data
        except RPLidarException as e:
            print('RpLidarProvider._poll_lidar_scans:', e)
            with self._scan_status_lock:
                self._scan_status = False

    @property
    def info(self) -> Union[Dict[str, Any], None]:
        return self._info

    @property
    def health(self) -> Union[str, None]:
        return self._health

    @property
    def scans(self) -> Union[Iterable[tuple[int, float, float]], None]:
        if not self._connection_status:
            return None
        data = []
        with self._data_buffer_lock:
            data = self._data_buffer
        return data

    def connect(self) -> bool:
        if self._connection_status:
            return True
        try:
            self._lidar_instance = RPLidar(self._port, self._baud_rate, self._timeout)
        except RPLidarException as e:
            self._connection_status = False
            self._scan_status = None
            self._motor_status = None
            self._lidar_instance = None
            return False
        else:
            self._connection_status = True
            self._lidar_instance.start_motor()
            self._motor_status = True
            self._scan_status = False
            self._info = self._lidar_instance.get_info()
            self._health = self._lidar_instance.get_health()
            self._lidar_polling_thread = threading.Thread(target=self._poll_lidar_scans, args=())
            self.start_scan()
            return True

    def disconnect(self) -> None:
        if self._lidar_instance is None:
            return
        self._lidar_instance.disconnect()
        self._lidar_instance = None
        self._connection_status = False
        self._scan_status = None
        self._motor_status = None

    def start_scan(self) -> bool:
        if self._connection_status:
            if self._scan_status:
                return True
            else:
                self._scan_status = True
                self._lidar_polling_thread.start()
                return True
        return False

    def stop_scan(self) -> None:
        if self._connection_status:
            with self._scan_status_lock:
                self._scan_status = False

    def start_motor(self) -> bool:
        if not self._connection_status:
            return False
        try:
            self._lidar_instance.start_motor()
        except RPLidarException as e:
            print(e)
            self.disconnect()
            return False

    def stop_motor(self) -> None:
        if not self._connection_status:
            return
        try:
            self._lidar_instance.stop_motor()
        except RPLidarException as e:
            self.disconnect()
            raise e

    def reset(self) -> None:
        if not self._connection_status:
            return
        try:
            self._lidar_instance.reset()
        except RPLidarException as e:
            self.disconnect()
            raise e


class FakeRpLidarProvider(AbstractLidarProvider):

    def __init__(self, port: str, baud_rate: int = 115200, timeout=1):
        super().__init__(port, baud_rate, timeout)
        self.grabbed_data: List[List[Tuple[int, float, float]]] = []
        self.counter = 0
        self._load_grabbed_data_from_json()


    def _load_grabbed_data_from_json(self):
        import json
        with open('./components/lidar_providers/rplidar_provider/data.json') as f:
            self.grabbed_data = json.load(f)

    @property
    def info(self) -> Union[Dict[str, Any], None]:
        return None

    @property
    def health(self) -> Union[str, None]:
        return 'Fake lidar health is fucking amazing!'

    @property
    def scans(self) -> Union[Iterable[Tuple[int, float, float]], None]:
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
    lidar = RpLidarProvider(LIDAR_PORT)
    print(lidar.info)
    print(lidar.health)
    print(lidar.scans)
