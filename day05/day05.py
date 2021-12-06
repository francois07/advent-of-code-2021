from typing import Callable
import numpy as np


def get_coordinates(data: str) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    """
    Extracts a list of couples of coordinates from a given input string

    :param str data: The input string
    :return: The list of couples of coordinates
    """
    lines = []

    for line in data.splitlines():
        raw_coordinates = [s.strip().split(",") for s in line.split("->")]
        coordinates = [(int(x), int(y)) for x, y in raw_coordinates]

        lines.append(coordinates)

    return lines


def get_line_points(start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    """
    Bresenham's Line Algorithm

    Computes coordinates between point A and point B

    :param tuple start: Point A's coordinates
    :param tuple end: Point B's coordinates
    :return: The list of coordinates
    """
    x1, y1 = start
    x2, y2 = end

    dx = x2 - x1
    dy = y2 - y1

    is_steep = abs(dy) > abs(dx)
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = x2 - x1
    dy = y2 - y1

    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1

    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)

        if error < 0:
            y += ystep
            error += dx

    return points


def get_overlaps(
    lines: list[tuple[tuple[int, int], tuple[int, int]]],
    condition: Callable[[int, int, int, int],
                        bool] = lambda x1, y1, x2, y2: True
) -> int:
    """
    Places a list of lines on a grid and computes the amount of overlaps

    :param list lines: The list of lines
    :param condition: The condition for the line to be added on the grid (optional)
    :return: The amount of overlapping lines
    """
    coordinates = [couple for coordinates in lines for couple in coordinates]
    flattened_coordinates = [n for couple in coordinates for n in couple]
    size = max(flattened_coordinates) + 1

    grid = np.zeros((size, size))

    for line in lines:
        x1, y1 = line[0]
        x2, y2 = line[1]

        if condition(x1, y1, x2, y2):
            points = get_line_points((x1, y1), (x2, y2))

            for x, y in points:
                grid[y, x] += 1

    return np.count_nonzero(grid >= 2)


def main():
    INPUT_TEXT = open("input.txt").read()
    lines = get_coordinates(INPUT_TEXT)

    overlaps_one_direction = get_overlaps(
        lines, lambda x1, y1, x2, y2: x1 == x2 or y1 == y2)
    overlaps = get_overlaps(lines)

    print("Part1:", overlaps_one_direction)
    print("Part2:", overlaps)


if __name__ == "__main__":
    main()
