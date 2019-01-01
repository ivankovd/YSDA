from .base_node import BaseNode


class Fold(BaseNode):
    def __init__(self, folder, state):
        """
        Node, which make Fold operation
        :param folder: multiplicative function for fold
        :param state: start state for Fold
        """
        super().__init__()
        self.folder = folder
        self.state = state

        self.info = self._set_info()

    def run(self):
        for row in self.input_gen():
            self.state = self.folder(state=self.state, record=row)
        yield self.state

    def _set_info(self):
        return "Fold with folder"
