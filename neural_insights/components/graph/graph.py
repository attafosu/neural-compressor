# -*- coding: utf-8 -*-
# Copyright (c) 2023 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Graph class."""

from typing import Dict, List

from neural_insights.components.graph.edge import Edge
from neural_insights.components.graph.node import Node
from neural_insights.utils.exceptions import NotFoundException
from neural_insights.utils.json_serializer import JsonSerializer
from neural_insights.utils.logger import log


class Graph(JsonSerializer):
    """Model graph definition."""

    def __init__(self) -> None:
        """Construct object."""
        super().__init__()
        self._nodes: Dict[str, Node] = {}
        self._edges: List[Edge] = []

    def add_node(self, node: Node) -> None:
        """Add a Node to graph."""
        self._nodes[node.id] = node

    @property
    def nodes(self) -> List[Node]:
        """Return nodes as a list."""
        return list(self._nodes.values())

    @property
    def edges(self) -> List[Edge]:
        """Return edges as a list."""
        return self._edges

    def add_edge(self, source_id: str, target_id: str) -> bool:
        """Add an Edge to graph."""
        try:
            source = self.get_node(source_id)
            target = self.get_node(target_id)
        except NotFoundException as err:
            log.debug(
                f"Got an error: {str(err)} while attempted "
                f"to add an Edge from {source_id} to {target_id}",
            )
            return False
        self._edges.append(Edge(source, target))
        return True

    def get_node(self, id: str) -> Node:
        """Get a node by id."""
        if id not in self._nodes:
            raise NotFoundException(f"Node id: {id} not found in Graph")
        return self._nodes[id]

    def highlight_pattern(self, op_name: str, pattern: List[str]) -> None:
        """Highlight pattern in graph."""
        source_op = op_name
        self.get_node(source_op).highlight = True
        for op in pattern[1:]:
            target_nodes = self.get_target_nodes(source_op)
            for target_node in target_nodes:
                if target_node.label == op:
                    self.get_node(target_node.id).highlight = True
                    source_op = target_node.id
                    continue

    def get_target_nodes(self, op_name: str) -> List[Node]:
        """Get target nodes from specified op."""
        target_nodes: List[Node] = []

        for edge in self.edges:
            if edge.source == op_name:
                target_nodes.append(self.get_node(edge.target))

        return target_nodes
