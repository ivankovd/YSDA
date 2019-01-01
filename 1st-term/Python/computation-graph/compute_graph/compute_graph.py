from compute_graph.operation import Input, Output


class ComputeGraph:
    def __init__(self, inputs, outputs, verbose=False, save_to_variable=False):
        """
        init ComputeGraph
        :param inputs: string with path to input file of output dict
        :param outputs: string with path to output file or output dict
        :param verbose: bool
        :param save_to_variable: if True, then output saved in
        self.output_node.output
        """
        self.input_node = Input(inputs)
        self.output_node = Output(outputs, save_to_variable)
        self.is_compile = False
        self.is_compute = False

        self.operations = [self.input_node]
        self.dependencies = []
        self.sorted_operations = []

        self.verbose = verbose

    def compile(self):
        """
        prepare graph for compute
        """
        if not self.is_compile:
            self.operations.append(self.output_node)
            for i_op, op in enumerate(self.operations):
                if i_op == 0:
                    continue
                op.set_input_gen(self.operations[i_op - 1].run)

            self.sorted_operations = self._sort()
            self.is_compile = True

    def summary(self):
        """
        print info about CoumputeGraph
        """
        for op in self.sorted_operations:
            print(op)

    def _sort(self):
        """
        sorting operation for solving diamond inheritance
        :return: sorted list with operations
        """
        sorted_operations = []
        num_dep = 0
        for op in self.operations:
            if op.get_node_name() == 'Join':
                sorted_operations.append(self.dependencies[num_dep])
                num_dep += 1
            sorted_operations.append(op)

        return sorted_operations

    def _set_is_joined(self, value):
        self.is_joined = value

    def run(self, save_to_variable=None):
        """
        Compute response
        """
        if save_to_variable is not None:
            self.output_node.save_to_variable = save_to_variable

        if not self.is_compute:
            self.sorted_operations[-1].run()
            self.sorted_operations[-1].close()
            self.is_compute = True
        else:
            self.output_node.output = self.output_node.output_array

    def add(self, node):
        """
        function for stacking operations
        :param node: operation
        """
        if node.get_node_name() == "Join":
            self.dependencies.append(node.on_graph)

        self.operations.append(node)
