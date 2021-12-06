def count_latern_fishes(data: str, day: int):
    """
    Computes the number of lanternfishes after X days, according to the problem description

    :param str data: The initial disposition of the fishes
    :param int day: The number of days to compute
    :return: The number of fishes
    """
    fishes = [int(x) for x in data.split(",")]
    population = {key: 0 for key in range(9)}

    for fish in set(fishes):
        population[fish] = fishes.count(fish)

    for _ in range(day):
        new_pop = population.copy()

        for key in population:
            if key == 0:
                new_pop[8] = population[0]
            else:
                new_pop[key-1] = population[key]

        new_pop[6] += new_pop[8]
        population = new_pop

    return sum(population.values())


def main():
    INPUT_TEXT = open("input.txt").read()
    fishes_80_days = count_latern_fishes(INPUT_TEXT, 80)
    fishes_256_days = count_latern_fishes(INPUT_TEXT, 256)

    print("Part1:", fishes_80_days)
    print("Part2:", fishes_256_days)


if __name__ == "__main__":
    main()
