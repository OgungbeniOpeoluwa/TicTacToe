from tic_tac_toe.board_element import BoardElement
from tic_tac_toe.board_fill_exception import BoardFilledException
from tic_tac_toe.games import Games


class Board:
    def __init__(self):
        self._list = [[], [], []]
        for count in range(3):
            for counts in range(3):
                self._list[count].append(BoardElement.EMPTY.name)

    def __str__(self):
        return self._list.__str__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def set_board(self, player_index, player_move):
        self.validate_board(player_move)
        self._list[player_move[0]][player_move[1]] = player_index.get_identity()

    def validate_board(self, player_move):
        if self._list[player_move[0]][player_move[1]] != BoardElement.EMPTY.name:
            raise BoardFilledException("space is not  available")

    def validate_wins(self, player_id):
        if self.row(player_id):
            return Games.WIN.name
        elif self.column(player_id):
            return Games.WIN.name
        elif self.right_diagonal(player_id):
            return Games.WIN.name
        elif self.left_diagonal(player_id):
            return Games.WIN.name
        elif self.is_full():
            return Games.DRAW.name
        else:
            return Games.CONTINUE.name

    def row(self, player_id):
        counter = 0
        for count in range(3):
            for counts in range(3):
                if self._list[count][counts] == player_id.get_identity():
                    counter += 1
            if counter == 3:
                return True
            else:
                counter = 0

    def column(self, player_id):
        counter = 0
        for count in range(3):
            for counts in range(3):
                if self._list[counts][count] == player_id.get_identity():
                    counter += 1
            if counter == 3:
                return True
            counter = 0

    def right_diagonal(self, player_id) -> bool:
        for count in range(3):
            if self._list[count][count] != player_id.get_identity():
                return False
        return True

    def left_diagonal(self, player_id) -> bool:
        column = 2
        for row in range(3):
            if self._list[row][column] != player_id.get_identity():
                return False
            else:
                column -= 1
        return True

    def is_full(self):
        for count in range(3):
            for counts in range(3):
                if self._list[count][counts] == BoardElement.EMPTY.name:
                    return False
        return True

    def get_board(self):
        return self._list
