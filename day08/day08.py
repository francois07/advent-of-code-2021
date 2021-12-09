from enum import Enum


def count_unique(data: str):
    count = 0

    for line in data.splitlines():
        patterns, digits = line.split(" | ")
        digits = digits.split(" ")

        for digit in digits:
            unique = [2, 3, 4, 7]
            if len(digit) in unique:
                count += 1

    return count


def main():
    INPUT_TEXT = open("input.txt").read()

    print("Part1", count_unique(INPUT_TEXT))


if __name__ == "__main__":
    main()
