import re
from enum import Enum
from typing import Callable


class Directions(str, Enum):
    FORWARD = "forward"
    UP = "up"
    DOWN = "down"


def get_commands(data: str) -> list[tuple[str, int]]:
    """
    Extracts commands from a given input string

    :param str data: Data to process
    :return: Commands extracted from the data
    """
    commands = []

    for command in data.splitlines():
        match = re.match(r"(forward|up|down) (\d+)", command)
        instruction, step = match.groups()

        commands.append((instruction, int(step)))

    return commands


def get_final_position(
    commands: list[tuple[str, int]],
    instruction_set: dict[str, Callable[[int, int, int, int], tuple[int, int, int]]],
    initial_pos=(0, 0), initial_aim=0
) -> tuple[int, int]:
    """
    Computes the final position based on a list of commands and a dictionnary describing what they do

    :param commands:        The list of commands to compute
    :param instruction_set: The functions corresponding to the commands' instructions
    :param initial_post:    The initial (X, Y) position
    :param initial_aim:     The initial aim
    """
    x, y = initial_pos
    aim = initial_aim

    for (instruction, step) in commands:
        x, y, aim = instruction_set[instruction](x, y, aim, step)

    return x, y


def main():
    INPUT_TEXT = open("input.txt").read()
    commands = get_commands(INPUT_TEXT)

    part1_instructions = {
        Directions.FORWARD: lambda x, y, aim, step: (x+step, y, aim),
        Directions.UP: lambda x, y, aim, step: (x, y-step, aim),
        Directions.DOWN: lambda x, y, aim, step: (x, y+step, aim)
    }
    part2_instructions = {
        Directions.FORWARD: lambda x, y, aim, step: (x+step, y+aim*step, aim),
        Directions.UP: lambda x, y, aim, step: (x, y, aim-step),
        Directions.DOWN: lambda x, y, aim, step: (x, y, aim+step)
    }

    x1, y1 = get_final_position(commands, part1_instructions)
    x2, y2 = get_final_position(commands, part2_instructions)

    print("Part1:", (x1, y1), x1*y1)
    print("Part2:", (x2, y2), x1*y2)


if __name__ == "__main__":
    main()
