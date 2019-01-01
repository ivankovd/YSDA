from compute_graph import ComputeGraph


def get_simple_data():
    return [
        {"1": 1, "2": 2},
        {"1": 3, "2": 4},
        {"1": 5, "2": 6},
        {"1": 7, "2": 8}
    ]


def test_input_equal_to_output():
    g = ComputeGraph(inputs=get_simple_data(), outputs=[],
                     save_to_variable=True)
    g.compile()
    g.run()
    assert g.output_node.output == get_simple_data()


def test_empty_input_equal_to_output():
    g = ComputeGraph(inputs=[], outputs=[],
                     save_to_variable=True)
    g.compile()
    g.run()
    assert g.output_node.output == []
