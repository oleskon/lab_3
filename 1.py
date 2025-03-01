class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):

        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    name = property(get_name)
    author = property(get_author)

    def str(self):
        return f"Книга {self.name}. Автор {self.author}"

    def repr(self):
        return f"{self.class.name}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def init(self, name: str, author: str, pages: int):
        super().init(name, author)
        self.set_pages(pages)

    def get_pages(self):
        return self._pages

    def set_pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    pages = property(get_pages, set_pages)

    def repr(self):
        return f"{self.class.name}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    def init(self, name: str, author: str, duration: float):
        super().init(name, author)
        self.set_duration(duration)

    def get_duration(self):
        return self._duration

    def set_duration(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = float(value)

    duration = property(get_duration, set_duration)

    def repr(self):
        return f"{self.class.name}(name={self.name!r}, author={self.author!r}, duration={self.duration})"