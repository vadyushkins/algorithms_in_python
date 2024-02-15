from typing import List

import pytest
from binary_heap import BinaryHeap


def evaluate_operations(operations: List[str]) -> BinaryHeap:
    result = BinaryHeap()
    for operation in operations:
        if operation.startswith("push"):
            value = int(operation.split()[-1])
            result.push(value)
        elif operation.startswith("remove"):
            value = int(operation.split()[-1])
            result.remove(value)
        elif operation.startswith("change"):
            key, new_value = int(operation.split()[-2]), int(operation.split()[-1])
            result.change(key, new_value)
    return result


def compare_binary_heaps(a: BinaryHeap, b: BinaryHeap):
    assert a.compare == b.compare
    assert a.container == b.container


def create_binary_heap_from_list(data: List[int]) -> BinaryHeap:
    result = BinaryHeap()
    for x in data:
        result.push(x)
    return result


tests = [
    {
        "input": [
            "push 1",
        ],
        "expected": [1],
    },
    {
        "input": [
            "push 1",
            "push 2",
        ],
        "expected": [2, 1],
    },
    {
        "input": [
            "push 1",
            "push 2",
            "push 3",
        ],
        "expected": [3, 1, 2],
    },
    {
        "input": [
            "push 10",
            "push 20",
            "push 30",
            "push 40",
        ],
        "expected": [40, 30, 20, 10],
    },
    {
        "input": [
            "push 10",
            "push 20",
            "push 30",
            "push 40",
            "remove 1",
        ],
        "expected": [40, 10, 20],
    },
    {
        "input": [
            "push 10",
            "push 20",
            "push 30",
            "push 40",
            "change 1 5",
        ],
        "expected": [40, 10, 20, 5],
    },
]


@pytest.mark.parametrize("test", [i for i in range(len(tests))])
def test(test):
    assert compare_binary_heaps(
        evaluate_operations(tests[test]["input"]),
        create_binary_heap_from_list(tests[test]["expected"]),
    )
