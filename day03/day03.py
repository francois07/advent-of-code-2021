from typing import Callable, Type


def get_power_consumption(data: str):
    gamma_rate = ""
    epsilon_rate = ""

    word_list = data.splitlines()
    length = len(word_list[0])

    for index in range(length):
        bit_list = [word[index] for word in word_list]

        gamma_rate += max(set(bit_list), key=bit_list.count)
        epsilon_rate += min(set(bit_list), key=bit_list.count)

    return (gamma_rate, epsilon_rate, int(gamma_rate, 2) * int(epsilon_rate, 2))


def filter_words(word_list: list[str], cmp_func: Type[max] | Type[min], equal_char: str) -> str:
    length = len(word_list[0])
    res = word_list.copy()

    for index in range(length):
        bit_list = [word[index] for word in res]
        filter_char = cmp_func(set(bit_list), key=bit_list.count)

        if bit_list.count(filter_char) == len(bit_list)/2:
            res = [word for word in res if word[index] == equal_char]
        else:
            res = [word for word in res if word[index] == filter_char]
        if len(res) <= 1:
            break

    return res[0]


def get_life_rating(data: str):
    oxygen_rating = filter_words(data.splitlines(), max, "1")
    co2_rating = filter_words(data.splitlines(), min, "0")

    return (oxygen_rating, co2_rating, int(oxygen_rating, 2)*int(co2_rating, 2))


def main():
    INPUT_TEXT = open("input.txt").read()

    gamma_rate, epsilon_rate, power_consumption = get_power_consumption(
        INPUT_TEXT)

    oxygen_rate, co2_rate, life_rating = get_life_rating(INPUT_TEXT)

    print("Part1:", gamma_rate, epsilon_rate, power_consumption)
    print("Part2:", oxygen_rate, co2_rate, life_rating)


if __name__ == "__main__":
    main()
