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
        (x + 1, y) if x < x_max - 1 else None,
        (x - 1, y - 1) if (x > x_min and y > y_min) else None,
        (x + 1, y + 1) if (x < x_max - 1 and y < y_max - 1) else None,
        (x - 1, y + 1) if (x > x_min and y < y_max - 1) else None,
        (x + 1, y - 1) if (x < x_max - 1 and y > y_min) else None
    ]

    return [pos for pos in adjacent_pos if pos is not None]


def flash_point(points: list[list[int]], pos: tuple[int, int], flashed=[]) -> None:
    """
    Flashes a point in the input list according to problem description

    :param list points: The input list
    :param tuple pos: The X and Y coordinates of the point to flash
    :param list flashed: The list of already flashed points
    :return: The flashed points
    """
    x, y = pos
    adjacent_points = get_adjacent(pos, (0, 0), (len(points[0]), len(points)))

    if points[y][x] > 9 and (x, y) not in flashed:
        flashed.append((x, y))

        for i, j in adjacent_points:
            points[j][i] += 1 if (i, j) not in flashed else 0
            flash_point(points, (i, j), flashed)

        points[y][x] = 0

    return flashed


def simulate_flashes(data: str, steps: int) -> int:
    """
    Computes the total number of flashes up until a certain step according to problem description

    :param str data: The input data
    :param int steps: The step to compute
    :return: The total number of flashes
    """
    flash_counter = 0
    points = [[int(x) for x in line] for line in data.splitlines()]

    for _ in range(steps):
        points = [[x+1 for x in line] for line in points]
        flashed = []

        for y in range(len(points)):
            for x in range(len(points[0])):
                flashed = flash_point(points, (x, y), flashed)

        flash_counter += len(flashed)

    return flash_counter


def get_sync_step(data: str) -> int:
    """
    Computes at which step points start flashing in sync

    :param str data: The input data
    :return: The computed step
    """
    points = [[int(x) for x in line] for line in data.splitlines()]
    i = 0

    while True:
        points = [[x+1 for x in line] for line in points]
        flashed = []

        for y in range(len(points)):
            for x in range(len(points[0])):
                flashed = flash_point(points, (x, y), flashed)

        if len(flashed) == len(points) * len(points[0]):
            return i + 1

        i += 1


def main():
    INPUT_TEXT = open("input.txt").read()
    total_100 = simulate_flashes(INPUT_TEXT, 100)
    sync_step = get_sync_step(INPUT_TEXT)

    print("Part1:", total_100)
    print("Part2:", sync_step)


if __name__ == "__main__":
    main()
