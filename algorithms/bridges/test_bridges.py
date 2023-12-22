import pytest
from bridges import bridges_search

tests = [
    {
        "input": {
            "graph": {
                0: [1, 2],
                1: [0],
                2: [0],
            },
        },
        "expected": [(0, 1), (0, 2)],
    },
    {
        "input": {
            "graph": {
                0: [1, 2],
                1: [0, 2],
                2: [0, 1, 3],
                3: [2],
            },
        },
        "expected": [(2, 3)],
    },
    {
        "input": {
            "graph": {
                0: [1, 5, 7],
                1: [0, 2],
                2: [1, 3, 5, 7],
                3: [2, 4],
                4: [3],
                5: [0, 2, 6],
                6: [5],
                7: [0, 2, 8],
                8: [7],
            },
        },
        "expected": [(2, 3), (3, 4), (5, 6), (7, 8)],
    },
    {
        "input": {
            "graph": {
                0: [1, 2],
                1: [0, 2],
                2: [0, 1],
            },
        },
        "expected": [],
    },
]


@pytest.mark.parametrize("test", [i for i in range(len(tests))])
def test(test):
    order = lambda pairs: sorted([(min(x, y), max(x, y)) for x, y in pairs])
    assert order(bridges_search(**tests[test]["input"])) == order(
        tests[test]["expected"]
    )
