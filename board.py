from typing import List
from toy import Toy
from player import Player


class Board:
    def __init__(self, size: int):
        self.fields: List[Toy] = [None] * size

    def __getitem__(self, key: int):
        return self.fields[key]

    def __setitem__(self, key: int, value: Toy):
        self.fields[key] = value

    def toy_positon(self, toy: Toy) -> Toy:
        return self.fields.index(toy)

    # Moves the toy number of offset positons forward.
    # Returns the old toy at this position or None,
    # if this field was empty before.
    def move_toy(self, toy: Toy, offset: int) -> Toy:
        # Get old positon of toy
        old_pos = self.toy_positon(toy)
        # Remove toy from old position
        self.fields[old_pos] = None
        # Calculate new position
        new_pos = (old_pos + offset) % len(self.fields)
        # Save the element that was previously at this position
        old_toy = self.fields[new_pos]
        # Move the toy to its new positon
        self.fields[new_pos] = toy
        return old_toy

    def __str__(self):
        return ' '.join(map(lambda x: str(x).center(8), self.fields))


# b = Board(10)
# p = Player('Linus', 4)
# b[0] = p.toys[0]
# print(f'Before move: {b}')
# print(b.move_toy(p.toys[0], 3))
# print(f'After move : {b}')
