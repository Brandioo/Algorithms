import abc
from abc import abstractmethod


class Client(abc.ABC):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @abstractmethod
    def __str__(self) -> str:
        pass


class Woman(Client):

    def __init__(self, first_name, last_name, age):
        self.age = age
        super().__init__(first_name, last_name)

    def __str__(self) -> str:
        return f"Madam {self.first_name} {self.last_name}"


class Man(Client):
    def __str__(self) -> str:
        return f"Mister {self.first_name} {self.last_name}"


class Child(Client):
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"