import sys
from typing import *
import json


if __name__ == '__main__':
    filest_to_read: List[str] = [
        '5dm_2hz_dump.json',
        '5dm_5hz_dump.json',
        '5dm_7.7hz_dump.json',
        '10dm_2hz_dump.json',
        '10dm_5hz_dump.json',
        '10dm_7.7hz_dump.json',
        '15dm_2hz_dump.json',
        '15dm_5hz_dump.json',
        '15dm_7.7hz_dump.json',
        '20dm_2hz_dump.json',
        '20dm_5hz_dump.json',
    ]
    data_to_parse: List[Dict[str, any]] = []
    try:
        for file_name in filest_to_read:
            print(file_name)
            with open(file_name, 'r', encoding='utf-8') as f:
                data = json.load(f)
                accum = 0
                for scan in data:
                    accum += len(scan['points'])
                accum = accum/len(data)
                print(accum, '\n')
                # data_to_parse.append(data)
    except Exception as e:
        print(e)
        sys.exit(1)
    # print(data_to_parse)
