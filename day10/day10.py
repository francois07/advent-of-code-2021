def is_corrupt(line: str, chunk_chars: dict[str, str]):
    """
    Computes wether a line is corrupt or not according to problem description

    :param str line: The line
    :param dict chunk_chars: The chunks opening characters associated with their closing counterparts
    :return: The computed boolean and the first corrupt character (or None if not corrupt)
    """
    chunks = []

    for char in line:
        if char in chunk_chars.values():
            chunks.append(char)
        elif char in chunk_chars:
            if chunks[-1] == chunk_chars.get(char):
                chunks.pop()
            else:
                return True, char

    return False, None


def get_syntax_score(data: str, chunks_chars: dict[str, str], char_points: dict[str, int]):
    """
    Computes the lines syntax score according to problem description

    :param str data: The lines
    :param dict chunk_chars: The chunks opening characters associated with their closing counterparts
    :param dict char_points: The characters' points according to problem descriptipn
    :return: The syntax score
    """
    score = 0

    for line in data.splitlines():
        corrupt, char = is_corrupt(line, chunks_chars)
        score += char_points[char] if corrupt else 0

    return score


def complete_line(line: str, chunk_chars: dict[str, str]):
    """
    Computes an incomplete line's completion string according to problem description

    :param str line: The line
    :param dict chunk_chars: The chunks opening characters associated with their closing counterparts
    :return: The completion string
    """
    chunks = []
    inv_chunk_chars = {v: k for k, v in chunk_chars.items()}

    for char in line:
        if char in chunk_chars.values():
            chunks.append(char)
        elif char in chunk_chars:
            chunks.pop()

    return "".join([inv_chunk_chars[char] for char in reversed(chunks)])


def get_completion_score(data: str, chunk_chars: dict[str, str], char_points: dict[str, int]):
    """
    Computes the lines completion score according to problem description

    :param str data: The lines
    :param dict chunk_chars: The chunks opening characters associated with their closing counterparts
    :param dict char_points: The characters' points according to problem descriptipn
    :return: The completion score
    """
    scores = []

    for line in data.splitlines():
        corrupt, _ = is_corrupt(line, chunk_chars)

        if corrupt:
            continue

        score = 0
        completion = complete_line(line, chunk_chars)

        for c in completion:
            score = (score * 5) + char_points[c]

        scores.append(score)

    return sorted(scores)[len(scores)//2]


def main():
    INPUT_TEXT = open("input.txt").read()
    CHUNK_CHARS = {
        "}": "{",
        "]": "[",
        ")": "(",
        ">": "<"
    }
    CHAR_SYNTAX_POINTS = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    CHAR_COMPLETION_POINTS = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }

    print("Part1:", get_syntax_score(INPUT_TEXT, CHUNK_CHARS, CHAR_SYNTAX_POINTS))
    print("Part2:", get_completion_score(
        INPUT_TEXT, CHUNK_CHARS, CHAR_COMPLETION_POINTS))


if __name__ == "__main__":
    main()
