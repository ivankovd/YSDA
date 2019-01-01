"""
The :mod: `compute_graph.operation` module implements generalized operations
with compute graph. It includes Fold, Join, Map ...
"""

from .base_node import BaseNode
from .fold import Fold
from .input import Input
from .join import Join
from .map import Map
from .reduce import Reduce
from .sort import Sort
from .output import Output
