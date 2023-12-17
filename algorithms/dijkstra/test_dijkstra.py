import pytest
from dijkstra import dijkstra

tests = [
    {
        "graph": {
            0: [[1, 1], [2, 1]],
            1: [[0, 1], [2, 1]],
            2: [[0, 1], [1, 1]],
        },
        "source_node": 0,
        "expected": [0, 1, 1],
    },
    {
        "graph": {
            0: [[1, 1]],
            1: [[2, 1]],
            2: [[3, 1]],
            3: [],
        },
        "source_node": 0,
        "expected": [0, 1, 2, 3],
    },
    {
        "graph": {
            0: [[1, 1], [2, 1]],
            1: [[3, 1]],
            2: [[3, 1]],
            3: [],
        },
        "source_node": 0,
        "expected": [0, 1, 1, 2],
    },
]


@pytest.mark.parametrize("test", [i for i in range(len(tests))])
def test_dijkstra(test):
    assert (
        dijkstra(
            graph=tests[test]["graph"],
            source_node=tests[test]["source_node"],
        )
        == tests[test]["expected"]
    )
