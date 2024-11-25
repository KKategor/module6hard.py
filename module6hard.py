# Task "Они все так похожи"

class Figure:
    __sides = []
    __color = []
    filled = False
    sides_count = len(__sides)

    def __init__(self, rgb, *side):
        self.color = list(rgb)
        self.side = side[0]
        self.filled = True

    def get_color(self):
        self.__color = self.color
        self.filled = True
        return self.__color

    def _is_valid_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        if 0 <= self.r <= 255 and 0 <= self.g <= 255 and 0 <= self.b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self.color = [self.r, self.g, self.b]

    def __is_valid_sides(self, *args):
        for side in self.sides:
            if len(self.sides) == self.sides_count and side > 0 and type(side) == int:
                return True
            else:
                return False

    def set_sides(self, *args):
        massive_lst = []
        self.sides = list(args)
        if self.__is_valid_sides(self, *args):
            self.get_sides()
        else:
            for i in range(self.sides_count):
                massive_lst.append(self.sides)
            self.sides = massive_lst
            self.get_sides()



    def get_sides(self):
        self.__sides = self.sides
        return self.__sides

    def __len__(self):
        return sum(self.sides) * self.sides_count

class Circle(Figure):
    sides_count = 1
    __radius = None

    def set_radius(self):
        self.__radius = self.__len__() / (2 * 3.141569)
        return self.__radius

    def get_square(self):
        self.set_radius()
        return (self.__radius ** 2) * 3.141569

class Triangle(Figure):
    site_count = 3
    hm = None

    def get_half_meter(self):
        self.hm = (self.side * 3)/2  # Полуперимерт

    def get_square(self):
        return (self.hm * (3 * self.hm - 3 * self.side)) ** 0.5

class Cube(Figure):
    side_count = 12

    def set_sides(self, *args):
        set_sides_lst = []
        self.sides = set_sides_lst
        for element in range(self.side_count):
            set_sides_lst.append(self.side)
        self.__sides = set_sides_lst
        return self.__sides


    def get_volume(self):
        return self.side ** 3


# Код для проверки:

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((222, 200, 130), 8)

# Проверка на изменение цветов:

circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:

cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:

print(len(circle1))


# Проверка объёма (куба):

print(cube1.get_volume())









