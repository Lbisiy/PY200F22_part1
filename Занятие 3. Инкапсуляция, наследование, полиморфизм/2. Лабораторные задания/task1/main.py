class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name_ = name
        self.author_ = author

    @property
    def name(self):
        return self.name_

    @property
    def author(self):
        return self.author_

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, pages: int):
        super(Book, self).__init__()
        self.pages = pages

    def init_pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError('Атрибут pages должен быть типа int')
        if pages < 1:
            raise ValueError('Атрибут pages должен быть положительным')
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, duration: float):
        super(Book, self).__init__()
        self.duration = self.init_duration(duration)

    def init_duration(self, duration: float):
        if not isinstance(duration, float):
            raise TypeError('Атрибут duration должен быть типа float')
        if duration <= 0:
            raise ValueError('Атрибут duration должен быть положительным')
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
