class Color:
    def __init__(self, value):
        self.value = value

    def ink(self, obj) -> str:
        return f'\033[{self.value}{str(obj)}\033[0m'


RED = Color('41')
GREEN = Color('42')
YELLOW = Color('43')
BLUE = Color('44')
MAGENTA = Color('45')
CYAN = Color('46')
WHITE = Color('47')
