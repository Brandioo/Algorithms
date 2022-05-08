class BookStack:

    def __init__(
            self,
            name: str,
            category: str = None
    ):
        self.name = name
        self.category = category
        self.stack = []

    def add_new_book(self, title: str):
        self.stack.append(title)

    def add_new_books(self, titles: list[str]):
        if titles:
            for title in titles:
                self.add_new_book(title)

    def get_book(self):
        return self.stack.pop()

    def all_books(self):
        return self.stack

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return f"Name: {self.name} - Category: {self.category}"

    def __gt__(self, other):
        return len(self) > len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __eq__(self, other):
        return len(self) == len(other)

    def __add__(self, other):
        book_stack_3 = BookStack(name='3')
        all_books = self.all_books() + other.all_books()
        book_stack_3.add_new_books(titles=all_books)
        return book_stack_3


if __name__ == '__main__':
    book_stack_1 = BookStack(name='1', category='Fictional')
    book_stack_1.add_new_books(['a', 'b', 'c'])
    book_stack_1.get_book()
    print(book_stack_1)
    print(book_stack_1.all_books())

    book_stack_2 = BookStack(name='2', category='Romance')
    book_stack_2.add_new_book('a')
    print(book_stack_2)
    print(book_stack_2.all_books())

    print(book_stack_1 > book_stack_2)
    print(book_stack_1 >= book_stack_2)
    print(book_stack_1 <= book_stack_2)
    print(book_stack_1 < book_stack_2)
    print(book_stack_1 == book_stack_2)

    book_stack_3 = book_stack_1 + book_stack_2
    print(book_stack_3.all_books())