import timeit
from functools import partial
from typing import Union


class Person:
    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email


class PersonSlots:
    __slots__ = ("name", "address", "email")

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email


class EmployeeSlots:
    __slots__ = ("dept",)

    def __init__(self, dept: str):
        self.dept = dept


# uncomment the class below that uses multiple inheritance and see the error
class PersonEmployee(Person, EmployeeSlots):
    pass


def get_set_delete_address(person: Union['Person', 'PersonSlots']):
    person.address = "123 Main St"
    _ = person.address
    del person.address


def main():
    person = Person("Alex", "123 Main St", "alex@gmail.com")
    # print(person.__dict__)
    person_slots = PersonSlots("Mateo", "123 Main St", "Mateo@gmail.com")
    # print(person_slots.__slots__)
    no_slots = min(timeit.repeat(partial(get_set_delete_address, person), number=1000000))
    slots = min(timeit.repeat(partial(get_set_delete_address, person_slots), number=1000000))
    print(f"No slots: {no_slots}")
    print(f"Slots: {slots}")
    print(f"% performance improvement: {(no_slots - slots) / no_slots:.2%}")


if __name__ == "__main__":
    main()
