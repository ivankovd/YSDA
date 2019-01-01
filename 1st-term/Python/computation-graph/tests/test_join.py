from compute_graph import ComputeGraph
from compute_graph.operation import Map, Join


def get_simple_data():
    return [
        {"1": 1, "2": 2},
        {"1": 3, "2": 4},
        {"1": 5, "2": 6},
        {"1": 7, "2": 8}
    ]


def test_simple_join():
    g_1 = ComputeGraph(inputs=get_simple_data(), outputs=[],
                       save_to_variable=True)

    g = ComputeGraph(inputs=get_simple_data(), outputs=[],
                     save_to_variable=True)
    g.add(Join(on_graph=g_1, by="1", strategy="inner"))
    g.compile()
    g.run()
    resp = [
        {"left_1": 1, "left_2": 2, "right_1": 1, "right_2": 2},
        {"left_1": 3, "left_2": 4, "right_1": 3, "right_2": 4},
        {"left_1": 5, "left_2": 6, "right_1": 5, "right_2": 6},
        {"left_1": 7, "left_2": 8, "right_1": 7, "right_2": 8},
    ]
    assert g.output_node.output == resp

if __name__ == '__main__':
    test_simple_join()