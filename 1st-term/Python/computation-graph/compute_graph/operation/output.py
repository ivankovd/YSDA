import io
import json

from .base_node import BaseNode


class Output(BaseNode):
    def __init__(self, outputs, save_to_variable=False):
        """
        Output node which print or write response to file
        :param outputs: str with path to output file or OutputStream
        :param save_to_variable: bool, if True, then save to variable output
        """
        super().__init__()
        self.save_to_variable = save_to_variable
        self.output, self.info = self._get_output(outputs)
        self.output_array = []

    def run(self):
        for row in self.input_gen():
            if self.save_to_variable:
                self.output.append(row)
            else:
                self.output_array.append(row)
                self.output.write(json.dumps(row) + '\n')

    def close(self):
        try:
            self.output.close()
        except Exception:
            pass

    def _get_output(self, outputs):
        if self.save_to_variable:
            info = "save to variable 'output'"
            return [], info
        if isinstance(outputs, str):
            info = "save to file {}".format(outputs)
            f = open(outputs, "w")
            return f, info
        elif isinstance(outputs, io.TextIOBase):
            info = "save file stream"
            return outputs, info

        else:
            raise ValueError("outputs type must be in ['str', 'dict'], "
                             "not {}".format(type(outputs)))
