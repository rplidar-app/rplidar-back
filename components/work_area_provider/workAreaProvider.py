from typing import *
import json


class WorkAreaProvider:

    def __init__(self):
        self._file_path: str = './env/work_area.json'
        self._data: List[Dict[str, Union[int, float]]] = []
        self._load_data()

    @property
    def data(self) -> List[Dict[str, Union[int, float]]]:
        return self._data

    @data.setter
    def data(self, points: List[Dict[str, Union[int, float]]]):
        self._data = points
        self._store_data()

    def _load_data(self) -> bool:
        try:
            with open(self._file_path, 'r', encoding='utf-8') as work_area_file:
                self._data = json.load(work_area_file)
                return True
        except IOError as e:
            self._data = []
            print('WARNING: file %s does not exist or you don\'t have permissions to read it.\n' % self._file_path,
                  'Exception text: %s' % str(e))
            try:
                with open(self._file_path, 'w', encoding='utf-8') as work_area_file:
                    json.dump(self._data, work_area_file)
                    return True
            except IOError as e:
                print('ERROR: can\'t create file %s' % self._file_path, '\n exception text: %s' % str(e))
                return False

    def _store_data(self) -> bool:
        try:
            with open(self._file_path, 'w', encoding='utf-8') as work_area_file:
                json.dump(self._data, work_area_file)
                return True
        except IOError as e:
            print('ERROR: can\'t store the work area into a file %s\n' % self._file_path,
                  'Exception text: %s' % str(e))
