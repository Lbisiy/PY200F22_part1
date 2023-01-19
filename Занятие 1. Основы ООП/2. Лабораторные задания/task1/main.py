import doctest
from math import pi
from typing import Optional, Union


class Circle:
    """
    Класс фигуры Circle (круг)

    Examples:
    >>> circle = Circle()  # инициализация экземпляра класса с атрибутами по умолчанию
    >>> circle = Circle(radius=10, x=5.0, y=-7)  # инициализация экземпляра класса с заданными атрибутами
    >>> circle_a = Circle()
    >>> circle_b = Circle(radius=10)
    >>> c = circle_a.intersection(circle_b)
    >>> c
    311.02
    """
    def __init__(self, radius: Union[int, float] = 1, x: Union[int, float] = 0, y: Union[int, float] = 0,
                 color: Optional[str] = None):
        """
        Метод инициализации экземпляра класса Circle
        :param radius: Радиус экземпляра класса
        :param x: Центр экземпляра класса относительно оси х
        :param y: Центр экземпляра класса относительно оси у
        """
        self.x = None
        self.y = None
        self.radius = radius
        self.init_x(x)
        self.init_y(y)
        self.color = color

    def init_x(self, x: Union[int, float] = 0):
        """
        Метод инициализации центра экземпляра класса Circle относительно оси х
        :param x: Центр экземпляра класса Circle относительно оси х
        """
        if not isinstance(x, (int, float)):
            raise TypeError(f'Вы выбрали неподходящий тип данных {type(x)} вместо [int, float]')
        self.x = x

    def init_y(self, y: Union[int, float] = 0):
        if not isinstance(y, (int, float)):
            raise TypeError(f'Вы выбрали неподходящий тип данных {type(y)} вместо [int, float]')
        self.y = y

    def set_circle_center(self, dx, dy):
        """
        Метод изменения расположения центра экземпляра класса Circle
        относительно осей системы координат
        :param dx: Смещение по оси х
        :param dy: Смещение по оси y
        """
        self.x += dx
        self.y += dy

    def get_circle_center(self):
        """
        Метод получения координат центра экземпляра класса Circle относительно системы координат
        :return: координаты х, у
        """
        return self.x, self.y

    def get_circle_square(self):
        """
        Метод получения площади круга
        :return: площадь экземпляра класса Circle
        """
        return pi * self.radius ** 2

    def change_color(self, color: str):
        """
        Класс изменения цвета экземпляра класса Circle
        :param color: Цвет экземпляра класса
        """
        self.color = color

    def intersection(self, circle):
        """
        Метод нахождения площади пересечения двух экзепляров класса Circle
        :param circle: Экземпляр класса Circle
        :return: Площадь пересечения между экземпляром класса (a), к которому
        применяется метод и экхмепляром класса (b), передаваемым в качестве
        атрибута
        """
        if self.x != circle.x and self.y != circle.y:
            raise ValueError('Для нахождения пересечения центры двух экземпляров класса должны совпадать')
        square_a = self.get_circle_square()
        square_b = circle.get_circle_square()
        return abs(round(square_a - square_b, 2))


if __name__ == "__main__":
    doctest.testmod()
