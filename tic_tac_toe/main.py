from tic_tac_toe.games import Games
from tic_tac_toe.tic_tactoe_game import TicTacToe

tic_tac_toes = TicTacToe()


def play():
    count = 0
    while tic_tac_toes.get_game() == Games.CONTINUE.name:
        loop_board()
        print()
        inputs = int(input(f'{tic_tac_toes.get_player()[count].get_name()} enter your move number: '))
        loop_board()
        print()
        tic_tac_toes.play(count, inputs)
        if tic_tac_toes.get_game() == Games.WIN.name:
            loop_board()
            print(f'{tic_tac_toes.get_player()[count].get_name()} won')
            break
        elif tic_tac_toes.get_game() == Games.DRAW.name:
            loop_board()
            print("It is Draw")
            break

        count += 1
        if count >= 2:
            count = 0


def loop_board():
    for count in range(3):
        for counts in range(3):
            print(tic_tac_toes.get_board().get_board()[count][counts], end="\t")
        print()


print(f"""Welcome to TIC_TAC_TOE Game!!!,
        This Game is available for Two players
        Kindly setup your names!!!""")
player_1 = input("player_one Enter your name: ")
player_2 = input("player_two Enter your name: ")
tic_tac_toes.get_player()[0].set_name(player_1)
tic_tac_toes.get_player()[1].set_name(player_2)
play()
