import pytest
from dfs import dfs

tests = [
    {
        "input": {
            "graph": {
                0: [1, 2],
                1: [0, 2],
                2: [0, 1],
            },
            "node": 0,
            "reachable": [0, 0, 0],
        },
        "expected": [1, 1, 1],
    },
    {
        "input": {
            "graph": {
                0: [1],
                1: [2],
                2: [3],
                3: [],
            },
            "node": 0,
            "reachable": [0, 0, 0, 0],
        },
        "expected": [1, 1, 1, 1],
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
            "node": 0,
            "reachable": [0, 0, 0, 0, 0],
        },
        "expected": [1, 1, 1, 0, 0],
    },
]


@pytest.mark.parametrize("test", [i for i in range(len(tests))])
def test(test):
    assert dfs(**tests[test]["input"]) == tests[test]["expected"]
