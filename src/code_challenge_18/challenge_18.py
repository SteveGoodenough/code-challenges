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


@dataclass
class IntegerNode:
    item: int
    next: Any = None

    def __str__(self):
        return f'{self.item} {self.next}'


def get_description(linked_list):
    return str(linked_list)


def add_to_list(linked_list, new_item):
    return extend_node(linked_list, Node(new_item))


def extend_node(source_list, target_list):
    if source_list is None:
        return target_list
    else:
        return Node(source_list.item, extend_node(source_list.next, target_list))


def create_integer_list(linked_list):
    return node_to_nodeint(linked_list)


def node_to_nodeint(source_list):
    if source_list is None:
        return None
    else:
        if source_list.item.isnumeric():
            return IntegerNode(int(source_list.item), node_to_nodeint(source_list.next))
        else:
            return IntegerNode(0, node_to_nodeint(source_list.next))
