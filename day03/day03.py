from typing import Callable


def find_most_common(data: list[str], index: int) -> str:
    bit_list = [x[index] for x in data]
    res = bit_list[0]
    counter = bit_list.count(res)

    for i in bit_list:
        freq = bit_list.count(i)
        if freq > counter:
            counter = freq
            res = i

    return counter, res


def find_least_common(data: list[str], index: int) -> str:
    bit_list = [x[index] for x in data]
    res = bit_list[0]
    counter = bit_list.count(res)

    for i in bit_list:
        freq = bit_list.count(i)
        if freq < counter:
            counter = freq
            res = i

    return counter, res


def get_power_consumption(data: str, build_func: Callable[[list[str], int], tuple[int, str]]):
    res = ""
    tab = data.splitlines()
    length = len(tab[0])

    for i in range(length):
        res += build_func(tab, i)[1]

    return res, int(res, 2)


def oxygen_filter(word: str, index: int, most_common: tuple[int, str], least_common: tuple[int, str]):
    most_common_count, most_common_bit = most_common
    least_common_count, least_common_bit = least_common

    if most_common_count == least_common_count:
        return word[index] == "1"
    return word[index] == most_common_bit


def co2_filter(word: str, index: int, most_common: tuple[int, str], least_common: tuple[int, str]):
    most_common_count, most_common_bit = most_common
    least_common_count, least_common_bit = least_common

    if most_common_count == least_common_count:
        return word[index] == "0"
    return word[index] == least_common_bit


def get_life_rating(data: str, filter_func: Callable[[str, int, tuple[int, str], tuple[int, str]], bool]):
    word_list = data.splitlines()
    n = len(word_list[0])

    for index in range(n):
        most_common = find_most_common(word_list, index)
        least_common = find_least_common(word_list, index)

        word_list = [word for word in word_list if filter_func(
            word, index, most_common, least_common)]

        if len(word_list) <= 1:
            break

    return word_list[0], int(word_list[0], 2)


def main():
    INPUT_TEXT = open("input.txt").read()

    gamma_rate_bin, gamma_rate = get_power_consumption(
        INPUT_TEXT, find_most_common)
    epsilon_rate_bin, epsilon_rate = get_power_consumption(
        INPUT_TEXT, find_least_common)

    oxygen_rate_bin, oxygen_rate = get_life_rating(INPUT_TEXT, oxygen_filter)
    co2_rate_bin, co2_rate = get_life_rating(INPUT_TEXT, oxygen_filter)

    print("Part1:", gamma_rate_bin, epsilon_rate_bin, gamma_rate * epsilon_rate)
    print("Part2:", oxygen_rate_bin, co2_rate_bin, oxygen_rate * co2_rate)


if __name__ == "__main__":
    main()
