from compute_graph import ComputeGraph
from compute_graph.operation import Sort


def get_simple_data():
    return [
        {"1": 1, "2": 2},
        {"1": 3, "2": 4},
        {"1": 5, "2": 6},
        {"1": 7, "2": 8}
    ]


def test_simple_sort():
    g = ComputeGraph(inputs=get_simple_data(), outputs=[],
                     save_to_variable=True)
    g.add(Sort(by="1", reverse=True))
    g.compile()
    g.run()
    resp = [
        {"1": 7, "2": 8},
        {"1": 5, "2": 6},
        {"1": 3, "2": 4},
        {"1": 1, "2": 2},
    ]
    assert g.output_node.output == resp

if __name__ == '__main__':
    test_simple_sort()