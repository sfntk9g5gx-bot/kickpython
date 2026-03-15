from typing import List

class SocialNetwork:
    """
    Базовый класс социальной сети.
    """

    def __init__(self, name: str, year: int) -> None:
        """
        Конструктор социальной сети.

        :param name: название сети
        :param year: год основания
        """
        self.name: str = name
        self.year: int = year
        self._users: List[str] = []  # закрытый список пользователей (инкапсуляция)

    def add_user(self, username: str) -> None:
        """
        Добавляет пользователя в сеть.

        :param username: имя пользователя
        """
        self._users.append(username)

    def user_count(self) -> int:
        """
        Возвращает количество пользователей.

        :return: число пользователей
        """
        return len(self._users)

    def __str__(self) -> str:
        """Строковое представление объекта."""
        return f"Социальная сеть {self.name}, год основания {self.year}"

    def __repr__(self) -> str:
        """Техническое представление объекта."""
        return f"SocialNetwork(name='{self.name}', year={self.year})"

class VK(SocialNetwork):
    """
    Дочерний класс социальной сети VK.
    """

    def __init__(self, year: int, music_service: bool) -> None:
        """
        Расширенный конструктор VK.

        :param year: год основания
        :param music_service: есть ли музыкальный сервис
        """
        super().__init__("VK", year)
        self.music_service: bool = music_service

    def add_user(self, username: str) -> None:
        """
        Перегруженный метод добавления пользователя.

        Причина перегрузки:
        В VK нельзя добавлять одинаковых пользователей.
        """
        if username not in self._users:
            self._users.append(username)

    def play_music(self, track: str) -> str:
        """
        Новый метод для воспроизведения музыки.

        :param track: название трека
        :return: сообщение о воспроизведении
        """
        if self.music_service:
            return f"Играет трек: {track}"
        return "Музыкальный сервис недоступен"

    def __str__(self) -> str:
        """Переопределённое строковое представление."""
        return f"VK (год основания {self.year})"

    def __repr__(self) -> str:
        """Техническое представление объекта VK."""
        return f"VK(year={self.year}, music_service={self.music_service})"

if __name__ == "__main__":
    # Write your solution here

    vk = VK(2006, True)

    vk.add_user("Ivan")
    vk.add_user("Maria")
    vk.add_user("Ivan")

    print(vk)
    print(repr(vk))

    print("Количество пользователей:", vk.user_count())
    print(vk.play_music("Believer"))