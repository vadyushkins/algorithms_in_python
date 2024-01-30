from typing import List

import pytest
from dll import DoublyLinkedList


def create_list(data: List[int]) -> DoublyLinkedList:
    result = DoublyLinkedList()
    for x in data:
        result.push_back(x)
    return result


def evaluate_operations(operations: List[str]) -> DoublyLinkedList:
    result = DoublyLinkedList()
    for operation in operations:
        if operation.startswith("push_back"):
            value = int(operation.split()[-1])
            result.push_back(value)
        elif operation.startswith("push_front"):
            value = int(operation.split()[-1])
            result.push_front(value)
        elif operation.startswith("pop_back"):
            result.pop_back()
        elif operation.startswith("pop_front"):
            result.pop_front()
        elif operation.startswith("find_item"):
            value = int(operation.split()[-1])
            assert result.find_item(value) is True
    return result


def compare_lists(a: DoublyLinkedList, b: DoublyLinkedList) -> bool:
    cur_a = a.head
    cur_b = b.head
    while (cur_a is not None) and (cur_b is not None):
        if cur_a.data != cur_b.data:
            return False
        cur_a = cur_a.next
        cur_b = cur_b.next
    return (cur_a is None) and (cur_b is None)


tests = [
    {
        "input": [
            "push_back 1",
        ],
        "expected": [1],
    },
    {
        "input": [
            "push_back 1",
            "push_front 2",
        ],
        "expected": [2, 1],
    },
    {
        "input": [
            "push_back 1",
            "push_front 2",
            "pop_back",
        ],
        "expected": [2],
    },
    {
        "input": [
            "push_back 1",
            "push_front 2",
            "pop_front",
        ],
        "expected": [1],
    },
    {
        "input": [
            "push_back 1",
            "push_front 2",
            "push_back 3",
            "find_item 3",
        ],
        "expected": [2, 1, 3],
    },
    {
        "input": [
            "push_back 1",
            "pop_back",
        ],
        "expected": [],
    },
    {
        "input": [
            "push_back 1",
            "pop_front",
        ],
        "expected": [],
    },
]


@pytest.mark.parametrize("test", [i for i in range(len(tests))])
def test(test):
    assert compare_lists(
        evaluate_operations(tests[test]["input"]),
        create_list(tests[test]["expected"]),
    )
