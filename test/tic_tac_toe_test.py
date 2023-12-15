import unittest

from tic_tac_toe.board import Board
from tic_tac_toe.board_element import BoardElement
from tic_tac_toe.board_fill_exception import BoardFilledException
from tic_tac_toe.games import Games
from tic_tac_toe.invalid_move_exception import InvalidMoveException
from tic_tac_toe.tic_tactoe_game import TicTacToe


class MyTestCase(unittest.TestCase):
    def test_that_board_is_fill_with_empty(self):
        tic_tac_toes = TicTacToe()
        board = Board()
        self.assertEqual(board, tic_tac_toes.get_board())

    def test_that_first_player_has_the_id_of_X(self):
        tic_tac_toes = TicTacToe()
        player = tic_tac_toes.get_player()
        self.assertEqual(BoardElement.X.name, player[0].get_identity())

    def test_that_second_player_has_the_identity_of_O(self):
        tic_tac_toes = TicTacToe()
        player = tic_tac_toes.get_player()
        self.assertEqual(BoardElement.O.name, player[1].get_identity())

    def test_that_when_move_number_1_is_entered_it_returns_list_0_0(self):
        tic_tac_toes = TicTacToe()
        self.assertEqual([0, 0], tic_tac_toes.moves(1))

    def test_that_when_i_move_by_9_it_returns_list_2_2(self):
        tic_tac_toes = TicTacToe()
        self.assertEqual([2, 2], tic_tac_toes.moves(9))

    def test_that_when_first_player_enter_1_the_board_changes_the_position_entered_from_empty_to_X(self):
        tic_tac_toes = TicTacToe()
        board = Board()
        player = tic_tac_toes.get_player()
        tic_tac_toes.play(0, 1)
        board.set_board(player[0], [0, 0])
        self.assertEqual(board, tic_tac_toes.get_board())

    def test_that_when_two_players_plays_and_each_position_entered_from_empty_to_X_and_O(self):
        tic_tac_toes = TicTacToe()
        board = Board()
        player = tic_tac_toes.get_player()
        board.set_board(player[0], [2, 2])
        board.set_board(player[1], [1, 1])
        tic_tac_toes.play(0, 9)
        tic_tac_toes.play(1, 5)
        self.assertEqual(board, tic_tac_toes.get_board())

    def test_that_player_cant_play_if_board_is_not_empty(self):
        tic_tac_toes = TicTacToe()
        board = Board()
        player = tic_tac_toes.get_player()
        board.set_board(player[0], [2, 2])
        tic_tac_toes.play(0, 9)
        with self.assertRaises(BoardFilledException) as ex:
            tic_tac_toes.play(1, 9)

    def test_That_when_A_player1_wins(self):
        tic_tac_toes = TicTacToe()
        player = tic_tac_toes.get_player()
        tic_tac_toes.play(0, 1)
        tic_tac_toes.play(1, 4)
        tic_tac_toes.play(0, 2)
        tic_tac_toes.play(1, 6)
        tic_tac_toes.play(0, 3)
        self.assertEqual(Games.WIN.name, tic_tac_toes.get_game())

    def test_that_player2_with_identity_0_wins(self):
        tic_tac_toes = TicTacToe()
        tic_tac_toes.play(0, 6)
        tic_tac_toes.play(1, 7)
        tic_tac_toes.play(0, 2)
        tic_tac_toes.play(1, 9)
        tic_tac_toes.play(0, 3)
        tic_tac_toes.play(1, 8)
        self.assertEqual(Games.WIN.name, tic_tac_toes.get_game())

    def test_that_player2_with_identity_0_wins_on_the_coloum(self):
        tic_tac_toes = TicTacToe()
        tic_tac_toes.play(0, 6)
        tic_tac_toes.play(1, 5)
        tic_tac_toes.play(0, 4)
        tic_tac_toes.play(1, 2)
        tic_tac_toes.play(0, 3)
        tic_tac_toes.play(1, 8)
        self.assertEqual(Games.WIN.name, tic_tac_toes.get_game())

    def test_that_player1_with_identity_x_wins_on_the_coloum(self):
        tic_tac_toes = TicTacToe()
        tic_tac_toes.play(0, 6)
        tic_tac_toes.play(1, 5)
        tic_tac_toes.play(0, 9)
        tic_tac_toes.play(1, 1)
        tic_tac_toes.play(0, 3)
        self.assertEqual(Games.WIN.name, tic_tac_toes.get_game())

    def test_that_player1_with_identity_X_wins_on_the_right_diagonal(self):
        tic_tac_toes = TicTacToe()
        tic_tac_toes.play(0, 1)
        tic_tac_toes.play(1, 3)
        tic_tac_toes.play(0, 9)
        tic_tac_toes.play(1, 2)
        tic_tac_toes.play(0, 5)
        self.assertEqual(Games.WIN.name, tic_tac_toes.get_game())

    def test_that_player1_with_identity_O_wins_on_the_right_diagonal(self):
        tic_tac_toes = TicTacToe()
        tic_tac_toes.play(0, 4)
        tic_tac_toes.play(1, 9)
        tic_tac_toes.play(0, 2)
        tic_tac_toes.play(1, 1)
        tic_tac_toes.play(0, 6)
        tic_tac_toes.play(1, 5)
        self.assertEqual(Games.WIN.name, tic_tac_toes.get_game())

    def test_that_player1_with_identity_x_wins_on_the_left_diagonal(self):
        tic_tac_toes = TicTacToe()
        tic_tac_toes.play(0, 1)
        tic_tac_toes.play(1, 3)
        tic_tac_toes.play(0, 9)
        tic_tac_toes.play(1, 2)
        tic_tac_toes.play(0, 5)
        self.assertEqual(Games.WIN.name, tic_tac_toes.get_game())

    def test_that_noPlayer_won_the_game(self):
        tic_tac_toes = TicTacToe()
        tic_tac_toes.play(0, 1)
        tic_tac_toes.play(1, 9)
        tic_tac_toes.play(0, 7)
        tic_tac_toes.play(1, 4)
        tic_tac_toes.play(0, 5)
        tic_tac_toes.play(1, 3)
        tic_tac_toes.play(0, 6)
        tic_tac_toes.play(1, 2)
        tic_tac_toes.play(0, 8)
        self.assertEqual(Games.DRAW.name, tic_tac_toes.get_game())

    def test_move_number(self):
        tic_tac_toes = TicTacToe()
        with self.assertRaises(InvalidMoveException) as ex:
            tic_tac_toes.moves(10)




if __name__ == '__main__':
    unittest.main()
