from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    item: str
    next: Any = None

    def __str__(self):
        return f'{self.item} {self.next}'


@dataclass
class IntegerNode:
    item: int
    next: Any = None

    def __str__(self):
        return f'{self.item} {self.next}'


def get_description(linked_list):
    return str(linked_list)


def add_to_list(linked_list, new_item):
    if linked_list is None:
        return Node(new_item)
    else:
        return Node(linked_list.item, add_to_list(linked_list.next, new_item))


def create_integer_list(linked_list):
    if linked_list is None:
        return None
    else:
        if linked_list.item.isnumeric():
            return IntegerNode(int(linked_list.item), create_integer_list(linked_list.next))
        else:
            return IntegerNode(0, create_integer_list(linked_list.next))


def reverse_list(linked_list):
    if linked_list is None:
        return None
    else:
        return add_to_list(reverse_list(linked_list.next), linked_list.item)
