from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from components.lidar_providers.rplidar_provider.rpLidarProvider import FakeRpLidarProvider, RpLidarProvider


# lidar = FakeRpLidarProvider('COM4')  # RpLidarProvider('COM4')
lidar = RpLidarProvider('/dev/ttyUSB0')
print('Lidar connection status:', lidar.connect())
print('Lidar info:', lidar.info)
print('Lidar health:', lidar.health)

origins = [
    '*',
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/lidar/scan')
def read_scan():
    data = lidar.scans
    return lidar.scans


@app.get('/lidar/reset')
def reset_scan():
    lidar.reset()


@app.get('/lidar/info')
def read_info():
    return {'data': lidar.info}


@app.get('/lidar/health')
def read_health():
    return {'data': lidar.health}


@app.get('/lidar/motor/stop')
def stop_motor():
    lidar.stop_motor()


@app.get('/lidar/motor/start')
def start_motor():
    return {'data': lidar.start_motor()}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


if __name__ == '__main__':
    print('Wake up, Neo!')
