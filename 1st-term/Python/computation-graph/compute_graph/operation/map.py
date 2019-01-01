from .base_node import BaseNode


class Map(BaseNode):
    def __init__(self, mapper):
        """
        Node for Map operation
        :param mapper: fumction for map
        """
        super().__init__()
        self.mapper = mapper
        self.info = self._set_info()
        pass

    def run(self):
        for row in self.input_gen():
            yield from self.mapper(row)

    def _set_info(self):
        return "Map with mapper func"
