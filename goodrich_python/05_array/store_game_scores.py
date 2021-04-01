class GameEntry:
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return f"({self._name}, {self._score})"


class Scoreboard:
    def __init__(self, capacity=10):
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, k):
        return self._board[k]

    def __str__(self):
        return '\n'.join(str(self._board[j]) for j in range(self._n))


    def add(self, entry):
        """Consider adding entry to high scores."""
        score = entry.get_score()

        # Does new entry qualify as a high score?
        # answer is yes if board not full or score is higher than last entry
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):  # no score drops from list
                self._n += 1  # so overall number increases

            # shift lower scores rightward to make room for new entry
            j = self._n - 1
            while j > 0 and self._board[j - 1].get_score() < score:
                self._board[j] = self._board[j - 1]  # shift entry from j-1 to j
                j -= 1  # and decrement j
            self._board[j] = entry  # when done, add new entry


if __name__ == '__main__':
    board = Scoreboard(5)
    for e in (
            ('Rob', 750), ('Mike', 1105), ('Rose', 590), ('Jill', 740),
            ('Jack', 510), ('Anna', 660), ('Paul', 720), ('Bob', 400),
    ):
        ge = GameEntry(e[0], e[1])
        board.add(ge)
        print(f'After considering {ge}, scoreboard is:')
        print(board)
        print()
