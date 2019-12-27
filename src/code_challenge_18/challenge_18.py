from dataclasses import dataclass
from typing import Any

# Create a function that takes the first node of a linked list of strings and returns a string
# that can be printed out to show all of the members of the list.
# Using the sample code above getDescription(firstNode) should return "hello world null".

# Create a function to add a value onto the end of a list.
# So addToList(firstNode, "!") and then running getDescription(firstNode)
# should result in "hello world ! null".

# Create a function that takes a linked list of strings and returns a linked list of integers.
# If the string cannot be converted to an integer, convert it to 0.

# Create a function that takes a linked list of strings and reverses it.
# So a list with a description of "a b c d e f null" would be converted to a list with a
# description of "f e d c b a null".


@dataclass
class Node:
    item: str
    next: Any = None

    def __str__(self):
        return f'{self.item} {self.next}'

    def __getitem__(self, index):
        if index == 0:
            return self.item
        else:
            return self.next[index - 1]

    def __len__(self):
        return 1 + len(self.next) if self.next is not None else 0


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
    new_list = Node(linked_list[len(linked_list)])
    for x in range(len(linked_list) - 1, -1, -1):
        new_list = add_to_list(new_list, linked_list[x])
    return new_list
