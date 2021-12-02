def window_measurements(data: str, window_size: int = 1) -> int:
    """
    Counts how many times the given window sum decreases

    :param str data: The data to compute
    :param int window_size: The window size
    """
    parsed_data = [int(x) for x in data.splitlines()]
    n = 0

    for i in range(0, len(parsed_data) - window_size):
        A = (parsed_data[i+k] for k in range(window_size))
        B = (parsed_data[i+k+1] for k in range(window_size))

        if sum(A) < sum(B):
            n += 1

    return n


def main():
    INPUT_TEXT = open("input.txt")

    decrease_count = window_measurements(INPUT_TEXT)
    window_decrease_count = window_measurements(INPUT_TEXT, 3)

    print("Part1:", decrease_count)
    print("Part2:", window_decrease_count)


if __name__ == "__main__":
    main()
