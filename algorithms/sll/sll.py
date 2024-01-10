from typing import Any, Optional


class SinglyLinkedList:
    class Node:
        def __init__(self, data: Any):
            self.data = data
            self.next: Optional[SinglyLinkedList.Node] = None

    def __init__(self):
        self.head: Optional[SinglyLinkedList.Node] = None
        self.tail: Optional[SinglyLinkedList.Node] = None

    def push_back(self, data: Any):
        if self.tail is None:
            self.tail = SinglyLinkedList.Node(data)
            self.head = self.tail
        else:
            self.tail.next = SinglyLinkedList.Node(data)
            self.tail = self.tail.next

    def push_front(self, data: Any):
        if self.head is None:
            self.head = SinglyLinkedList.Node(data)
            self.tail = self.head
        else:
            new_head = SinglyLinkedList.Node(data)
            new_head.next = self.head
            self.head = new_head

    def pop_back(self):
        if self.tail is not None:
            new_tail = self.head
            while new_tail.next.next is not None:
                new_tail = new_tail.next
            new_tail.next = None
            self.tail = new_tail

    def pop_front(self):
        if self.head is not None:
            self.head = self.head.next

    def find_item(self, data: Any):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            else:
                current = current.next
        return False
