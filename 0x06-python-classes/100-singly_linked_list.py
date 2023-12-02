#!/usr/bin/python3
"""A Node class"""


class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = data

        if not isinstance(next_node, None) and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node

        @property
        def data(self):
            return (self.__data)

        @data.setter
        def data(self, data):
            if not isinstance(data, int):
                raise TypeError("data must be an integer")
            else:
                self.__data = data

        @property
        def next_node(self):
            return (self.__next_node)

        @next_node.setter
        def next_node(self, next_node):
            if not isinstance(next_node, None) and not isinstance(next_node, Node):
                raise TypeError("next_node must be a Node object")
            else:
                self.__next_node = next_node

"""A class that defines a singly linked list"""


class SinglyLinkedList:
    """Singly Linked List"""

    def __init__(self, head=None):
        self.__head = head

    def sorted_insert(self, value):
        node = Node(value)
        if self.__head is None:
            self.__head = node
            return
        
        current = self.__headclear

        while current.next_node() is not None and current.next_node.data < value:
            current = current.next_node()
        next = node.next_node()
        next = current.next_node()
        current.next_node() = node

