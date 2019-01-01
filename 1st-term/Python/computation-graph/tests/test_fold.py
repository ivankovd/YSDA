import pytest
from compute_graph import ComputeGraph
from compute_graph.operation import Fold


def get_simple_data():
    return [
        {"1": 1, "2": 2},
        {"1": 3, "2": 4},
        {"1": 5, "2": 6},
        {"1": 7, "2": 8}
    ]


def sum_columns_folder(state, record):
    for column in state:
        state[column] += record[column]
    return state


def test_simple_fold():
    g = ComputeGraph(inputs=get_simple_data(), outputs=[],
                     save_to_variable=True)
    g.add(Fold(folder=sum_columns_folder, state={"1": 0}))
    g.compile()
    g.run()
    resp = [
        {"1": 16}
    ]
    assert g.output_node.output == resp
