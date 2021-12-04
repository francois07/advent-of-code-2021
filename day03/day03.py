from typing import Type


def get_power_consumption(data: str) -> tuple[str, str, int]:
    """
    Computes the power consumption

    :param str data: The diagnostic report to process
    :return: The power consumption
    """
    gamma_rate = ""
    epsilon_rate = ""

    word_list = data.splitlines()
    length = len(word_list[0])

    for index in range(length):
        bit_list = [word[index] for word in word_list]

        gamma_rate += max(set(bit_list), key=bit_list.count)
        epsilon_rate += min(set(bit_list), key=bit_list.count)

    return (gamma_rate, epsilon_rate, int(gamma_rate, 2) * int(epsilon_rate, 2))


def filter_words(data: str, cmp_func: Type[max] | Type[min], equal_char: str) -> str:
    """
    Filters the diagnostic report according to the problem description

    :param str data: The diagnostic report
    :param Type[max] | Type[min] cmp_func: The function used to get the char that will filter the data, either min or max
    :param str equal_char: The char to use as a filter in case of counting equality
    :return: The final word
    """
    word_list = data.splitlines()
    length = len(word_list[0])

    for index in range(length):
        bit_list = [word[index] for word in word_list]
        filter_char = cmp_func(set(bit_list), key=bit_list.count)

        if bit_list.count(filter_char) == len(bit_list)/2:
            word_list = [
                word for word in word_list if word[index] == equal_char]
        else:
            word_list = [
                word for word in word_list if word[index] == filter_char]
        if len(word_list) <= 1:
            break

    return word_list[0]


def get_life_support_rating(data: str) -> tuple[str, str, int]:
    """
    Computes the life support rating

    :param str data: The diagnostic report
    :return: The life support rating
    """
    oxygen_rating = filter_words(data, max, "1")
    co2_rating = filter_words(data, min, "0")

    return (oxygen_rating, co2_rating, int(oxygen_rating, 2)*int(co2_rating, 2))


def main():
    INPUT_TEXT = open("input.txt").read()

    gamma_rate, epsilon_rate, power_consumption = get_power_consumption(
        INPUT_TEXT)

    oxygen_rate, co2_rate, life_rating = get_life_support_rating(INPUT_TEXT)

    print("Part1:", gamma_rate, epsilon_rate, power_consumption)
    print("Part2:", oxygen_rate, co2_rate, life_rating)


if __name__ == "__main__":
    main()
