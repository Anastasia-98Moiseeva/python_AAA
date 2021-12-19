from abc import abstractmethod


class ComputerColor:

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __mul__(self, value: float):
        pass

    @abstractmethod
    def __rmul__(self, value: float):
        pass


class Color(ComputerColor):
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self) -> str:
        return f'{self.START};{self.r};{self.g};{self.b}{self.MOD}●{self.END}{self.MOD}'

    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b

    def __add__(self, other):
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)

    def __hash__(self):
        return hash((self.r, self.g, self.b))

    @staticmethod
    def new_color(current, contrast):
        cl = -256 * (1 - contrast)
        F = (259 * (cl + 255)) / (255 * (259 - cl))
        return int(F * (current - 128) + 128)

    def __mul__(self, contrast: float):
        if contrast >= 1 or contrast <= 0:
            raise ValueError(f'Contrast is equals to {contrast}, but should be between 0 and 1')

        return Color(Color.new_color(self.r, contrast), Color.new_color(self.g, contrast), Color.new_color(self.b, contrast))

    __rmul__ = __mul__

    __repr__ = __str__


def print_a(color):
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
        [bg_color] * 19,
    ]
    for row in a_matrix:
        print(''.join(str(ptr) for ptr in row))


if __name__ == '__main__':
    orange = Color(255, 165, 0)
    orange1 = Color(255, 165, 0)
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    print(f'orange: {orange}')
    print(f'red: {red}')
    print(f'green: {green}')

    assert orange == orange1
    assert orange != red

    print(f'green+red: {green + red}')

    color_list = [orange1, red, green, orange]
    color_set = set(color_list)
    assert len(color_set) == 3

    contrast_red_color = 0.5 * red
    print(f'red color with 0.5 contrast: {contrast_red_color}')

    print_a(green)
