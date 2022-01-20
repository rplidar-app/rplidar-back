from typing import Optional

from fastapi import FastAPI

from components.lidar_providers.rplidar_provider.rpLidarProvider import RpLidarProvider


lidar = RpLidarProvider('COM4')
print('Lidar connection status:', lidar.connect())
print('Lidar info:', lidar.info)
print('Lidar health:', lidar.health)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/lidar/scan')
def read_scan():
    return {'data': lidar.scans}


@app.get('/lidar/reset')
def reset_scan():
    lidar.reset()


@app.get('/lidar/info')
def read_info():
    return {'data': lidar.info}


@app.get('/lidar/health')
def read_scan():
    return {'data': lidar.health}


@app.get('/lidar/motor/stop')
def read_scan():
    lidar.stop_motor()


@app.get('/lidar/motor/start')
def read_scan():
    return {'data': lidar.start_motor()}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


if __name__ == '__main__':
    print('Wake up, Neo!')
