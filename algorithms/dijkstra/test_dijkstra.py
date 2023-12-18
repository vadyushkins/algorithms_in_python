import pytest
from dijkstra import dijkstra

tests = [
    {
        "input": {
            "graph": {
                0: [[1, 1], [2, 1]],
                1: [[0, 1], [2, 1]],
                2: [[0, 1], [1, 1]],
            },
            "source_node": 0,
        },
        "expected": [0, 1, 1],
    },
    {
        "input": {
            "graph": {
                0: [[1, 1]],
                1: [[2, 1]],
                2: [[3, 1]],
                3: [],
            },
            "source_node": 0,
        },
        "expected": [0, 1, 2, 3],
    },
    {
        "input": {
            "graph": {
                0: [[1, 1], [2, 1]],
                1: [[3, 1]],
                2: [[3, 1]],
                3: [],
            },
            "source_node": 0,
        },
        "expected": [0, 1, 1, 2],
    },
]


@pytest.mark.parametrize("test", [i for i in range(len(tests))])
def test(test):
    assert dijkstra(**tests[test]["input"]) == tests[test]["expected"]
