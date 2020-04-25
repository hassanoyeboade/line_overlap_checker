from typing import Tuple


Line = Tuple[float, float]


def line_overlap_checker(line_1: Line, line_2: Line) -> bool:
    """
    Checks if two lines (x1,x2) and (x3,x4) on the x-axis overlap.
    As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
    :param line_1: A 2-tuple of ints representing the points of the first line on the x-axis
    :param line_2: A 2-tuple of ints representing the points of the second line on the x-axis
    :return: boolean indicating if the lines overlap

    Examples::
        line_overlap_checker((1,5), (2,6)) => True
        line_overlap_checker((1,5), (6,8)) => False
    """
    line_1_first_point, line_1_second_point = sorted(line_1)

    line_2_first_point, line_2_second_point = sorted(line_2)

    return line_2_first_point < line_1_second_point < line_2_second_point or \
        line_1_first_point < line_2_first_point < line_1_second_point
