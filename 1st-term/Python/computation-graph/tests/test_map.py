import pytest
from compute_graph import ComputeGraph
from compute_graph.operation import Map


def get_simple_data():
    return [
        {"1": 1, "2": 2},
        {"1": 3, "2": 4},
        {"1": 5, "2": 6},
        {"1": 7, "2": 8}
    ]

def mapper_1(r):
    yield {
        "1": r["2"]
    }

def mapper_2(r):
    for key, value in r.items():
        yield {
            key: value
        }


def test_simple_map():
    g = ComputeGraph(inputs=get_simple_data(), outputs=[],
                     save_to_variable=True)
    g.add(Map(mapper=mapper_1))
    g.compile()
    g.run()
    resp = [
        {"1": 2},
        {"1": 4},
        {"1": 6},
        {"1": 8}
    ]
    assert g.output_node.output == resp

def test_one_to_many_map():
    g = ComputeGraph(inputs=get_simple_data(), outputs=[],
                     save_to_variable=True)
    g.add(Map(mapper=mapper_2))
    g.compile()
    g.run()
    resp = [
        {"1": 1}, {"2": 2},
        {"1": 3}, {"2": 4},
        {"1": 5}, {"2": 6},
        {"1": 7}, {"2": 8}
    ]
    assert g.output_node.output == resp





