import pytest
from sccs import strongly_connected_components_search

tests = [
    {
        "input": {
            "graph": {
                0: [1, 2],
                1: [0],
                2: [3],
                3: [2],
            },
        },
        "expected": [[0, 1], [2, 3]],
    },
    {
        "input": {
            "graph": {
                0: [2, 3],
                1: [0],
                2: [1],
                3: [4],
                4: [5],
                5: [3],
            },
        },
        "expected": [[0, 1, 2], [3, 5, 4]],
    },
    {
        "input": {
            "graph": {
                0: [1],
                1: [],
            },
        },
        "expected": [[0], [1]],
    },
    {
        "input": {
            "graph": {
                0: [1],
                1: [2],
                2: [3],
                3: [4],
                4: [0],
            },
        },
        "expected": [[0, 4, 3, 2, 1]],
    },
    {
        "input": {
            "graph": {
                0: [],
                1: [],
                2: [],
            },
        },
        "expected": [[2], [1], [0]],
    },
]


@pytest.mark.parametrize("test", [i for i in range(len(tests))])
def test(test):
    assert (
        strongly_connected_components_search(**tests[test]["input"])
        == tests[test]["expected"]
    )
