import json

from .base_node import BaseNode


class Input(BaseNode):
    def __init__(self, inputs):
        """
        Operathion from which start computing graph
        :param inputs: path to input file or list[dict]-like variable
        """
        super().__init__()
        self.table, self.info = self._get_input(inputs)

    def run(self):
        for row in self.table:
            yield row

    def _get_input(self, inputs):
        if isinstance(inputs, str):
            table = []
            with open(inputs, 'r') as file:
                for line in file.readlines():
                    table.append(json.loads(line))

            info = "file readed from {}".format(inputs)
            return table, info

        elif isinstance(inputs, list):
            info = "file read from variable"
            return inputs, info

        else:
            raise ValueError("inputs type must be in ['str', dict], "
                             "not {}".format(type(inputs)))
