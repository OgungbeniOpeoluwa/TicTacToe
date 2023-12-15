from tic_tac_toe.board import Board
from tic_tac_toe.board_element import BoardElement
from tic_tac_toe.games import Games
from tic_tac_toe.invalid_move_exception import InvalidMoveException
from tic_tac_toe.player import Player


class TicTacToe:
    def __init__(self):
        self._board = Board()
        self._player = (Player(BoardElement.X.name), Player(BoardElement.O.name))
        self._move_pair = {}
        self._game = Games.CONTINUE.name

    def get_player(self):
        return self._player

    def pair_number_to_rows_and_column(self):
        row = 0
        column = 0
        for count in range(1, 10):
            self._move_pair[count] = [row, column]
            column += 1
            if column > 2:
                row += 1
                column = 0
        return self._move_pair

    def moves(self, move):
        if move < 1 or move > 9:
            raise InvalidMoveException("moves is between 1 and 9")
        return self.pair_number_to_rows_and_column().get(move)

    def play(self, player_index, move_number):
        players = self._player[player_index]
        result = self.moves(move_number)
        self._board.set_board(players, result)
        self._game = self._board.validate_wins(players)

    def get_game(self):
        return self._game

    def get_board(self):
        return self._board
