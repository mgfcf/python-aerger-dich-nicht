from typing import List
from player import Player
from board import Board


class Game:
    def __init__(self, players: List[Player], number_of_toys: int, board_size: int):
        self.players = players
        self.board = Board(board_size)

    def __str__(self) -> str:
        output = ''
        player_names = map(lambda p: str(p), self.players)
        output += f'Players: {", ".join(player_names)}\n'
        output += f'Board: {self.board}'
        return output


if __name__ == '__main__':
    # Read game config data
    number_of_toys = 4
    number_of_players = int(input('Number of players: '))
    players = []
    for i in range(number_of_players):
        print(f'-- Player {i} --')
        name = input('Name: ')
        color = input('Color: ')
        players.append(Player(name, color, 4))

    g = Game(players, number_of_toys, 10)
    print(g)
