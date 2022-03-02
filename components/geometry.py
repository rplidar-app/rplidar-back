from typing import Union, Tuple


def line_segments_intersection(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float)\
        -> Union[Tuple[float, float], None]:
    """
    A function to calculate coordinates of the intersection point between two lines
    :param x1: X coordinate of the first point of the first line
    :param y1: Y coordinate of the first point of the first line
    :param x2: X coordinate of the second point of the first line
    :param y2: Y coordinate of the second point of the first line
    :param x3: X coordinate of the first point of the second line
    :param y3: Y coordinate of the first point of the second line
    :param x4: X coordinate of the second point of the second line
    :param y4: Y coordinate of the second point of the second line
    :return: a tuple with x and y intersection coordinates, or None if there is no intersection between lines
    """
    a_dx = x2 - x1
    a_dy = y2 - y1
    b_dx = x4 - x3
    b_dy = y4 - y3
    s = (-a_dy * (x1 - x3) + a_dx * (y1 - y3)) / (-b_dx * a_dy + a_dx * b_dy)
    t = (+b_dx * (y1 - y3) - b_dy * (x1 - x3)) / (-b_dx * a_dy + a_dx * b_dy)
    # if s >= 0 and s <= 1 and t >= 0 and t <= 1:
    if 0 <= s <= 1 and 0 <= t <= 1:
        return x1 + t * a_dx, y1 + t * a_dy
    else:
        return None
