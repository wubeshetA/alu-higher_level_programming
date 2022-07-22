#!/usr/bin/python3
"""Define a class Node"""


class Node:
    """ Represent a node in a singly linked list"""

    def __init__(self, data, next_node=None):
        """ Initialize a new Node

         Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ Return the data"""

        return self.__data

    @data.setter
    def data(self, value):
        """ Set the data"""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Return the next node"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Set the next node"""

        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Respresent singly linked list"""

    def __init__(self):
        """Initialize a singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list

        Args:
            value: The Node to insert into the list."""

        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """Define the string representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
