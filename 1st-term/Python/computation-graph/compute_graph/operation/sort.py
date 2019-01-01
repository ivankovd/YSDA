from .base_node import BaseNode
from operator import itemgetter


class Sort(BaseNode):
    def __init__(self, by, reverse=False):
        """
        Node for Sort operation
        :param by: str or list with columns for sorting
        :param reverse: if True, then sort descending
        """
        super().__init__()

        self.reverse = reverse
        if isinstance(by, str):
            self.by = [by]
        elif isinstance(by, list):
            self.by = by
        else:
            raise ValueError("Unknown type for 'by'")

        self.info = self._set_info()

    def run(self):
        table = list(self.input_gen())
        table = sorted(table, key=itemgetter(*self.by), reverse=self.reverse)
        for row in table:
            yield row

    def _set_info(self):
        return "by: {}".format(self.by)
