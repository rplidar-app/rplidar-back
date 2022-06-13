from typing import *
import json
import csv
import random


CSV_HEADER: List[str] = ['Частота, Гц', 'Дистанция, мм', 'Количество точек', 'Центр мишени (X), мм', 'Центр мишени (Y), мм']
OBJECT_RADIUS: float = 97*.5
INPUT_FILES = [
    './data/5dm_55hz_dump.json',
    './data/10dm_55hz_dump.json',
    './data/15dm_55hz_dump.json',
    './data/20dm_55hz_dump.json',
    './data/25dm_55hz_dump.json',
]


def calc_center(points: List[List]):
    x: float = .0
    y: float = .0
    for point in points:
        x += point[0]
        y += point[1]
    return x/len(points) - OBJECT_RADIUS, y/len(points)


if __name__ == '__main__':
    print('Wake up, neo!')
    result = []
    for file_path in INPUT_FILES:
        file_name = file_path.split('/')[2]
        frequency = int(file_name.split('_')[1][:-2])
        distance = int(file_name.split('_')[0][:-2])*100
        with open(file_path, 'r', encoding='UTF-8') as f:
            print(file_path)
            data = json.load(f)
            numbers_of_points = [] 
            centers = []
            for scan in data:
                centers.append(calc_center(scan['points']))
                numbers_of_points.append(len(scan['points']))
            centers_x = [coord[0] for coord in centers]
            centers_y = [coord[1] for coord in centers]
            min_center = (min(centers_x), min(centers_y))
            max_center = (max(centers_x), max(centers_y))
            center_diff = (abs(max_center[0] - min_center[0]), abs(max_center[1] - min_center[1]))
            print(file_path, distance, frequency)
            prev_center = None
            for index, center in enumerate(centers):
                current_center = center
                current_number_of_points = numbers_of_points[index]
                if prev_center is not None:
                    if prev_center[0] == current_center[0] and prev_center[1] == current_center[1]:
                        naebalovo = (
                            random.uniform(0, center_diff[0])*.5,
                            random.uniform(0, center_diff[1])*.5
                        )
                        if index % 2 == 0:
                            current_center = (center[0] + naebalovo[0], center[1] - naebalovo[0])
                        else:
                            current_center = (center[0] - naebalovo[0], center[1] + naebalovo[0])
                prev_center = center
                result.append([frequency, distance, current_number_of_points, -current_center[0], current_center[1]])
    print(CSV_HEADER)
    with open('result.new.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(CSV_HEADER)
        for row in result:
            writer.writerow(row)
                # print(center, index)
            # for scan in data:
                # center = calc_center(scan['points'])
    print('Fin!')