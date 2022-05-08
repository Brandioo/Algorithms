""" Program to implement the Books Stack class with magic methods """
from typing import Union


class BooksStack:
    def __init__(
            self,
            stack_name: str,
            category: Union[None, str] = None
    ):
        self.stack_name = stack_name
        self.category = category
        self.stack: list[str] = []

    def add_new_book(self, title: str):
        self.stack.append(title)

    def get_book(self) -> str:
        return self.stack.pop()

    def all_books(self) -> list[str]:
        return self.stack

    # Magic method to add 2 BookStacks together
    def __add__(self, second_stack: 'BooksStack') -> 'BooksStack':
        new_stack = BooksStack(stack_name=self.stack_name, category=self.category)
        new_stack.stack = self.stack + second_stack.stack
        return new_stack

    # comparision
    def __gt__(self, second_stack: 'BooksStack') -> bool:
        return len(self.stack) > len(second_stack.stack)

    def __lt__(self, second_stack: 'BooksStack') -> bool:
        return len(self.stack) < len(second_stack.stack)

    def __ge__(self, second_stack: 'BooksStack') -> bool:
        return len(self.stack) >= len(second_stack.stack)

    def __le__(self, second_stack: 'BooksStack') -> bool:
        return len(self.stack) <= len(second_stack.stack)

    # Represantation
    def __str__(self) -> str:
        return f'Stack {self.stack_name} with category of books {self.category}'

    def __repr__(self) -> str:
        books = ' '.join(self.stack)
        return f'stack_name: {self.stack_name} \n category: {self.category} \n books: {books}'

    # Length of BooksStack
    def __len__(self) -> int:
        return len(self.stack)
