import operator
from typing import Any


class BinaryHeap:
    def __init__(self, container: Any = list, compare: Any = operator.ge) -> None:
        self.container = container()
        self.compare = compare

    def sift_up(self, key: int):
        if len(self.container) > key:
            while (
                key > 0
                and self.compare(self.container[(key - 1) >> 1], self.container[key])
                == False
            ):
                (self.container[(key - 1) >> 1], self.container[key]) = (
                    self.container[key],
                    self.container[(key - 1) >> 1],
                )
                key >>= 1

    def sift_down(self, key: int):
        if len(self.container) > key:
            while (
                2 * key + 1 < len(self.container)
                and self.compare(self.container[key], self.container[2 * key + 1])
                == False
            ) or (
                2 * key + 2 < len(self.container)
                and self.compare(self.container[key], self.container[2 * key + 2])
                == False
            ):
                if 2 * key + 2 < len(self.container):
                    if (
                        self.compare(
                            self.container[2 * key + 1], self.container[2 * key + 2]
                        )
                        == True
                    ):
                        (self.container[2 * key + 1], self.container[key]) = (
                            self.container[key],
                            self.container[2 * key + 1],
                        )
                        key = 2 * key + 1
                    else:
                        (self.container[2 * key + 2], self.container[key]) = (
                            self.container[key],
                            self.container[2 * key + 2],
                        )
                        key = 2 * key + 2
                else:
                    (self.container[2 * key + 1], self.container[key]) = (
                        self.container[key],
                        self.container[2 * key + 1],
                    )
                    key = 2 * key + 1

    def push(self, new_value: Any):
        self.container.append(new_value)
        self.sift_up(len(self.container) - 1)

    def remove(self, key: int):
        if len(self.container) > key:
            (self.container[len(self.container) - 1], self.container[key]) = (
                self.container[key],
                self.container[len(self.container) - 1],
            )
            self.container.pop()
            self.sift_down(key)

    def pop(self):
        self.remove(0)

    def change(self, key: int, new_value: Any):
        if len(self.container) > key and self.container[key] != new_value:
            self.container[key] = new_value
            if (
                key > 0
                and self.compare(self.container[(key - 1) >> 1], self.container[key])
                == False
            ):
                self.sift_up(key)
            else:
                self.sift_down(key)

    def top(self) -> Any:
        return self.container[0] if len(self.container) > 0 else None

    def size(self) -> int:
        return len(self.container)
