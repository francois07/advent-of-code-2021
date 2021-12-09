from typing import Callable


def get_minfuel(data: str, comp_func: Callable[[int, int], int] = lambda x, y: abs(x - y)) -> int:
    """
    Computes the minimum possible fuel to be used according to problem description

    :param str data: The crabs' positions
    :param comp_func: The function used to compare positions (optional)
    :return: The minimum fuel
    """
    positions = [int(x) for x in data.split(",")]
    min_fuel = float("inf")

    for pos in positions:
        fuel_cost = sum([comp_func(n, pos) for n in positions])
        min_fuel = min(min_fuel, fuel_cost)

    return min_fuel


def main():
    INPUT_TEXT = open("input.txt").read()
    minfuel = get_minfuel(INPUT_TEXT)
    minfuel_incremental = get_minfuel(
        INPUT_TEXT, lambda x, y: int(abs(x - y)*(abs(x - y) + 1)/2))

    print("Part1:", minfuel)
    print("Part2:", minfuel_incremental)


if __name__ == "__main__":
    main()
