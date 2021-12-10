def get_adjacent(pos: tuple[int], min_pos: tuple[int], max_pos: tuple[int]) -> list[tuple]:
    """
    Computes a point's adjacent positions

    :param tuple pos: The point's X and Y coordinates
    :param tuple min_pos: The minimum X and Y coordinates
    :param tuple max_pos: The maximum X and Y coordinates
    :return: The point's adjacent positions
    """
    x, y = pos
    x_min, y_min = min_pos
    x_max, y_max = max_pos

    adjacent_pos = [
        (x, y - 1) if y > y_min else None,
        (x, y + 1) if y < y_max - 1 else None,
        (x - 1, y) if x > x_min else None,
        (x + 1, y) if x < x_max - 1 else None
    ]

    return [pos for pos in adjacent_pos if pos is not None]


def get_low_points(points: list[list[int]]) -> list[tuple[int, int]]:
    """
    Extracts low points from the input according to problem description

    :param points: The list of points
    :return: The low points
    """
    low_points = []

    for y in range(len(points)):
        line = points[y]

        for x in range(len(line)):
            adjacent_locations = get_adjacent(
                (x, y), (0, 0), (len(line), len(points)))
            adjacent_points = [points[y][x] for x, y in adjacent_locations]

            if points[y][x] < min(adjacent_points):
                low_points.append((x, y))

    return [(x, y) for x, y in low_points]


def get_basin(points: list[list[int]], current_point: tuple[int, int], basin: list[tuple[int, int]] = []) -> list[tuple[int, int]]:
    """
    Computes a low point's basin according to problem description using recursion

    :param points: The list of points
    :param current_points: The current point
    :param basin: The basin
    :return: The low point's basin
    """
    x, y = current_point
    value = points[y][x]
    adjacent_points = get_adjacent(
        (x, y), (0, 0), (len(points[0]), len(points)))

    basin.append((x, y))

    for point in adjacent_points:
        i, j = point
        point_value = points[j][i]

        if point not in basin and 9 > point_value:
            get_basin(points, point, basin)

    return basin


def main():
    INPUT_TEXT = open("input.txt").read()

    points = [[int(x) for x in list(line)] for line in INPUT_TEXT.splitlines()]

    low_points = get_low_points(points)
    risk_levels = [points[y][x] + 1 for x, y in low_points]

    basins = [get_basin(points, low_point, []) for low_point in low_points]
    basins_sizes = sorted([len(basin) for basin in basins], reverse=True)
    largest_basins = basins_sizes[:3]

    print("Part1:", sum(risk_levels))
    print("Part2:", largest_basins[0] * largest_basins[1] * largest_basins[2])


if __name__ == "__main__":
    main()
