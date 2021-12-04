
class Board:

    """
    Representation of a bingo board

    :param id: The board id
    :param str input: The raw board data
    """

    def __init__(self, id, input: str) -> None:
        self.id = id
        self.input = input
        self.lines = self.get_lines()
        self.columns = [self.get_column(i) for i in range(len(self.lines[0]))]

    def __getitem__(self, key: int) -> list[int]:
        return self.lines[key]

    def get_lines(self) -> list[list[int]]:
        """
        Extracts lines from the raw board data and converts values to integers

        :return: The board lines
        """
        lines = []
        for line in self.input.split("\n"):
            tab = []
            for i in range(0, len(line), 3):
                tab.append(int(line[i:i+3]))
            lines.append(tab)
        return lines

    def get_column(self, index: int) -> list[list[int]]:
        """
        Extracts columns from the board lines

        :return: The board columns
        """
        return [line[index] for line in self.lines]

    def is_winner(self, numbers: list[int], turn: int) -> bool:
        """
        Computes wether or not the board is a winner at a specific turn according to problem description

        :return: True if the board is a winner
        """
        res = False
        numbers_at_turn = numbers[:turn]

        for line in self.lines:
            in_numbers = [n in numbers_at_turn for n in line]
            if all(in_numbers):
                res = True
        for column in self.columns:
            in_numbers = [n in numbers_at_turn for n in column]
            if all(in_numbers):
                res = True

        return res

    def get_score(self, numbers: list[int], turn: int) -> int:
        """
        Computes the board score at a specific turn

        :return: The board score
        """
        sum_unmarked = 0
        numbers_at_turn = numbers[:turn]

        for line in self.lines:
            sum_unmarked += sum([n for n in line if n not in numbers_at_turn])

        return sum_unmarked * numbers[turn - 1]


class Bingo:
    """
    Representation of a bingo game

    :param str input: The bingo game data, including boards and drawn numbers in order
    """

    def __init__(self, input: str) -> None:
        self.input = input
        self.numbers = self.get_numbers()
        self.boards = self.get_boards()

    def __getitem__(self, key: int) -> Board:
        return self.boards[key]

    def get_numbers(self) -> list[int]:
        """
        Extracts drawn numbers from the game data

        :return: The drawn numbers in order
        """
        return [int(x) for x in self.input.split("\n\n")[0].split(",")]

    def get_boards(self) -> list[Board]:
        """
        Extracts bingo boards from the game data

        :return: The bingo boards
        """
        boards = self.input.split("\n\n")[1:]
        return [Board(i, board) for i, board in enumerate(boards)]

    def get_winners(self) -> list[tuple[int, int, int]]:
        """
        Simulates the bingo game and computes the winners in order

        :return: The winners in order, along with the turn which they won at and their final score
        """
        turns = len(self.numbers)
        winners = []

        for turn in range(1, turns):
            nums = self.numbers[:turn]
            boards = [board for board in self.boards if board.id not in [
                w[1] for w in winners]]

            for board in boards:
                if board.is_winner(self.numbers, turn):
                    winner = (self.numbers[turn-1], board.id,
                              board.get_score(self.numbers, turn))
                    winners.append(winner)

        return winners


def main():
    INPUT_TEXT = open("input.txt").read()
    bingo_subsystem = Bingo(INPUT_TEXT)
    winners = bingo_subsystem.get_winners()

    print("Part1:", winners[0])
    print("Part2:", winners[-1])


if __name__ == "__main__":
    main()
