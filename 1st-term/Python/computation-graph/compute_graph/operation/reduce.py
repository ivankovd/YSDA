from .base_node import BaseNode


class Reduce(BaseNode):
    def __init__(self, reducer, key=None):
        """
        Node for Reduce operation
        :param reducer: function for reducing
        :param key: string or list of string with keys. If None, then Reduce
        all table
        """
        super().__init__()
        self.reducer = reducer

        if isinstance(key, str):
            self.key = [key]
        else:
            self.key = key

        self.info = self._set_info()

    def run(self):
        if self.key is None:
            yield from self.reducer(list(self.input_gen()))

        else:
            previous_key = None
            stack = []

            for current_value in self.input_gen():
                current_key = {key: current_value[key] for key in self.key}

                if previous_key is None:
                    stack.append(current_value)
                elif current_key == previous_key:
                    stack.append(current_value)
                else:
                    yield from self.reducer(stack)
                    stack = [current_value]

                previous_key = current_key

            if len(stack) > 0:
                yield from self.reducer(stack)

    def _set_info(self):
        try:
            info = ", ".join(self.key)
        except Exception:
            info = self.key
        return "Reduce with keys {}".format(info)
