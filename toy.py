
class Toy:
    def __init__(self, player_name: str, nr: int):
        self.player_name = player_name
        self.nr = nr

    def __str__(self) -> str:
        return f'{self.player_name}.{self.nr}'
