class Pixel:
    """
    _x - x coordinate
    _y - y coordinate
    _red - a value between 0 and 255
    _green - a value between 0 and 255
    _blue - a value between 0 and 255
    """

    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_cords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg = (self._red + self._blue + self._green)//3
        self._red = avg
        self._green = avg
        self._blue = avg

    def print_pixel_info(self):
        print("X: {}, Y: {}".format(self._x, self._y), end="")
        if self._red == 0 and self._green == 0 and self._blue > 50:
            print(", Color: ({}, {}, {}) Blue".format(self._red, self._green, self._blue))
        elif self._red == 0 and self._green > 50 and self._blue == 0:
            print(", Color: ({}, {}, {}) Green".format(self._red, self._green, self._blue))
        elif self._red > 50 and self._green == 0 and self._blue == 0:
            print(", Color: ({}, {}, {}) Red".format(self._red, self._green, self._blue))
        else:
            print(", Color: ({}, {}, {})".format(self._red, self._green, self._blue))


def main():
    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()


if __name__ == '__main__':
    main()
