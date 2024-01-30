from typing import Any, Optional


class DoublyLinkedList:
    class Node:
        def __init__(self, data: Any):
            self.data = data
            self.prev: Optional[DoublyLinkedList.Node] = None
            self.next: Optional[DoublyLinkedList.Node] = None

    def __init__(self):
        self.head: Optional[DoublyLinkedList.Node] = None
        self.tail: Optional[DoublyLinkedList.Node] = None

    def push_back(self, data: Any):
        if self.tail is None:
            self.tail = DoublyLinkedList.Node(data)
            self.head = self.tail
        else:
            self.tail.next = DoublyLinkedList.Node(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def push_front(self, data: Any):
        if self.head is None:
            self.head = DoublyLinkedList.Node(data)
            self.tail = self.head
        else:
            self.head.prev = DoublyLinkedList.Node(data)
            self.head.prev.next = self.head
            self.head = self.head.prev

    def pop_back(self):
        if self.tail is not None:
            if self.head.next is None:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None

    def pop_front(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

    def find_item(self, data: Any) -> bool:
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            else:
                current = current.next
        return False
