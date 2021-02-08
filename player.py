from toy import Toy
from color import Color


class Player:
    def __init__(self, name: str, color: Color, number_of_toys: int):
        self.name = name
        self.color = color
        self.toys = [Toy(self.name, i) for i in range(number_of_toys)]

    def __str__(self) -> str:
        return self.color.ink(self.name)
