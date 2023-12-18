import pytest
from bfs import bfs

tests = [
    {
        "input": {
            "graph": {
                0: [1, 2],
                1: [0, 2],
                2: [0, 1],
            },
            "source_node": 0,
        },
        "expected": [0, 1, 1],
    },
    {
        "input": {
            "graph": {
                0: [1],
                1: [2],
                2: [3],
                3: [],
            },
            "source_node": 0,
        },
        "expected": [0, 1, 2, 3],
    },
    {
        "input": {
            "graph": {
                0: [1],
                1: [2],
                2: [0],
                3: [4],
                4: [3],
            },
            "source_node": 0,
        },
        "expected": [0, 1, 2, -1, -1],
    },
]


@pytest.mark.parametrize("test", [i for i in range(len(tests))])
def test(test):
    assert bfs(**tests[test]["input"]) == tests[test]["expected"]
