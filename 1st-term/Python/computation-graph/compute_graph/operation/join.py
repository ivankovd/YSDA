from operator import itemgetter

from .base_node import BaseNode


class Join(BaseNode):
    def __init__(self, on_graph, by, strategy='inner'):
        """
        Node for Join operation
        :param on: other ComputeGraph
        :param by: str or list columns for join
        :param strategy: ['inner']
        """
        super().__init__()
        self.on_graph = on_graph
        if isinstance(by, str):
            self.by = [by]
        else:
            self.by = by
        self.strategy = strategy

        self.on_graph_data = self._get_data_from_other_graph()
        self.info = self._set_info()

    def run(self):
        self.our_data = list(self.input_gen())

        if self.strategy == "inner":
            yield from self._inner_strategy()

        elif self.strategy == "left":
            yield from self._left_strategy()

        elif self.strategy == "right":
            yield from self._right_strategy()

        elif self.strategy == "full":
            yield from self._full_strategy()

        else:
            raise ValueError("strategy must be in ['inner', 'left', "
                             "'right', 'full'], not {}".format(self.strategy))

    def _get_data_from_other_graph(self):
        if not self.on_graph.is_compile:
            self.on_graph.compile()

        if not self.on_graph.is_compute:
            self.on_graph.run(save_to_variable=True)

        return self.on_graph.output_node.output

    def _inner_strategy(self):
        sorted_our_data = sorted(self.our_data, key=itemgetter(*self.by))
        sorted_on_graph_data = sorted(self.on_graph_data,
                                      key=itemgetter(*self.by))

        for our_row in sorted_our_data:
            for on_graph_row in sorted_on_graph_data:
                key = itemgetter(*self.by)
                if key(our_row) < key(on_graph_row) or \
                        key(our_row) > key(on_graph_row):
                    continue
                else:
                    response = {}
                    for key, value in our_row.items():
                        response["left_" + key] = value
                    for key, value in on_graph_row.items():
                        response["right_" + key] = value

                    yield response

    def _left_strategy(self):
        sorted_our_data = sorted(self.our_data, key=itemgetter(*self.by))
        left_in_inner_join = [False for _ in range(len(sorted_our_data))]
        sorted_on_graph_data = sorted(self.on_graph_data,
                                      key=itemgetter(*self.by))
        key = itemgetter(*self.by)
        for i, our_row in enumerate(sorted_our_data):
            for on_graph_row in sorted_on_graph_data:
                if key(our_row) < key(on_graph_row) or \
                        key(our_row) > key(on_graph_row):
                    continue
                else:
                    left_in_inner_join[i] = True
                    response = {}
                    for key, value in our_row.items():
                        response["left_" + key] = value
                    for key, value in on_graph_row.items():
                        response["right_" + key] = value

                    yield response

        for i, is_in_inner_join in enumerate(left_in_inner_join):
            if not is_in_inner_join:
                response = {}
                for key, value in sorted_our_data[i].items():
                    response["left_" + key] = value

                for key, value in sorted_on_graph_data[0].items():
                    response["right_" + key] = None

                yield response

    def _right_strategy(self):
        sorted_our_data = sorted(self.our_data, key=itemgetter(*self.by))
        sorted_on_graph_data = sorted(self.on_graph_data,
                                      key=itemgetter(*self.by))
        right_in_inner_join = [False for _ in range(len(sorted_on_graph_data))]
        key = itemgetter(*self.by)
        for our_row in sorted_our_data:
            for i, on_graph_row in enumerate(sorted_on_graph_data):
                if key(our_row) < key(on_graph_row) or \
                        key(our_row) > key(on_graph_row):
                    continue
                else:
                    right_in_inner_join[i] = True
                    response = {}
                    for key, value in our_row.items():
                        response["left_" + key] = value
                    for key, value in on_graph_row.items():
                        response["right_" + key] = value

                    yield response

        for i, is_in_inner_join in enumerate(right_in_inner_join):
            if not is_in_inner_join:
                response = {}
                for key, value in sorted_our_data[0].items():
                    response["left_" + key] = None
                for key, value in sorted_on_graph_data[i].items():
                    response["right_" + key] = value

                yield response

    def _full_strategy(self):
        sorted_our_data = sorted(self.our_data, key=itemgetter(*self.by))
        sorted_on_graph_data = sorted(self.on_graph_data,
                                      key=itemgetter(*self.by))
        left_in_inner_join = [False for _ in range(len(sorted_our_data))]
        right_in_inner_join = [False for _ in range(len(sorted_on_graph_data))]
        key = itemgetter(*self.by)
        for i, our_row in enumerate(sorted_our_data):
            for j, on_graph_row in enumerate(sorted_on_graph_data):
                if key(our_row) < key(on_graph_row) or \
                        key(our_row) > key(on_graph_row):
                    continue
                else:
                    left_in_inner_join[i] = True
                    right_in_inner_join[j] = True
                    response = {}
                    for key, value in our_row.items():
                        response["left_" + key] = value
                    for key, value in on_graph_row.items():
                        response["right_" + key] = value

                    yield response

        for i, is_in_inner_join in enumerate(left_in_inner_join):
            if not is_in_inner_join:
                response = {}
                for key, value in sorted_our_data[i].items():
                    response["left_" + key] = value

                for key, value in sorted_on_graph_data[0].items():
                    response["right_" + key] = None

                yield response

        for i, is_in_inner_join in enumerate(right_in_inner_join):
            if not is_in_inner_join:
                response = {}
                for key, value in sorted_our_data[0].items():
                    response["left_" + key] = None
                for key, value in sorted_on_graph_data[i].items():
                    response["right_" + key] = value

                yield response

    def _set_info(self):
        return "on: {}, by: {}, strategy: {}".format(self.on_graph, self.by,
                                                     self.strategy)
