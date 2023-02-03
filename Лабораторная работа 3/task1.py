class Book:
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f"Название книги {self.name}. Автор книги {self.author}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError('Количество страниц книги должно быть типа int')
        if pages <= 0:
            raise ValueError('Количество страниц книги должно быть положительным числом')
        self._pages = pages

    def __str__(self) -> str:
        return f"Название бумажной книги {self.name}. Автор книги {self.author}. Количество страниц {self.pages}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError('Продолжительность аудиокниги должна быть типа float')
        if duration <= 0:
            raise ValueError('Продолжительность аудиокниги должна быть положительным числом')
        self._duration = duration

    def __str__(self) -> str:
        return f"Название аудиокниги {self.name}. Автор аудиокниги {self.author}. Продолжительность {self.duration}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
