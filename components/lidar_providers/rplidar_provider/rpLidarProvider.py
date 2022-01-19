from typing import Tuple, Any, Dict, Union

from rplidar import RPLidar, RPLidarException

from components.abstract_classes.abstract_lidar_provider.abstractLidarProvider import AbstractLidarProvider


class RpLidarProvider(AbstractLidarProvider):

    def __init__(self, port: str, baud_rate: int = 115200, timeout=1):
        super().__init__(port, baud_rate, timeout)
        self._lidar_instance: Union[RPLidar, None] = None

    @property
    def info(self) -> Union[Dict[str, Any], None]:
        if not self._connection_status:
            return None
        return self._lidar_instance.get_info()

    @property
    def health(self) -> Union[str, None]:
        if not self._connection_status:
            return None
        return self._lidar_instance.get_health()

    @property
    def scans(self) -> Union[Tuple[int, float, float], None]:
        raise NotImplementedError()

    def connect(self) -> bool:
        if self._connection_status:
            return True
        try:
            self._lidar_instance = RPLidar(self._port, self._baud_rate, self._timeout)
        except RPLidarException:
            self._connection_status = False
            self._scan_status = None
            self._motor_status = None
            self._lidar_instance = None
            return False
        else:
            self._connection_status = True
            self._lidar_instance.start_motor()
            self._motor_status = True
            self._scan_status = True
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
                try:
                    self._lidar_instance.reset()
                except RPLidarException as e:
                    print(e)
                    self.disconnect()
                else:
                    self._scan_status = True
                    return True
        return False

    def stop_scan(self) -> None:
        if self._connection_status:
            try:
                self._lidar_instance.stop()
            except RPLidarException as e:
                self.disconnect()
                raise e
            else:
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
            self._lidar_instance.start_motor()
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


if __name__ == '__main__'"":
    LIDAR_PORT: str = 'COM4'  # '/dev/ttyUSB0'
    lidar = RpLidarProvider(LIDAR_PORT)
    # lidar = RPLidar(LIDAR_PORT)
    #
    # info = lidar.get_info()
    # print(info)
    #
    # health = lidar.get_health()
    # print(health)
    #
    # for i, scan in enumerate(lidar.iter_scans()):
    #     print('%d: Got %d measurements' % (i, len(scan)), scan[0])
    #     # if i > 10:
    #     #     break
    #
    # lidar.stop()
    # lidar.stop_motor()
    # lidar.disconnect()
