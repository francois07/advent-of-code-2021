input = [int(x) for x in open("input.txt").read().splitlines()]


def count_decrease(data: list[int]) -> int:
    n = 0

    for i in range(1, len(data)):
        if data[i-1] < data[i]:
            n += 1

    return n


def window_measurements(data: list[int], window_size: int) -> int:
    n = 0

    for i in range(0, len(data) - window_size):
        A = (data[i+k] for k in range(window_size))
        B = (data[i+k+1] for k in range(window_size))

        if sum(A) < sum(B):
            n += 1

    return n


print("Part1:", count_decrease(input))
print("Part2:", window_measurements(input, 3))
