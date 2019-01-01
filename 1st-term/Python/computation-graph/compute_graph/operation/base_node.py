class BaseNode:
    def __init__(self):
        """
        Base class for every node with base operations
        """
        self.input = None

    def set_input_gen(self, input_gen):
        self.input_gen = input_gen

    def get_node_name(self):
        return self.__class__.__name__

    def get_info(self):
        return self.info

    def __str__(self):
        return "{}---{}".format(self.get_node_name(), self.get_info())