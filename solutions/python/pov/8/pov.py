"""Tree data structure with path finding and perspective transformation capabilities.

This module provides a Tree class that supports:
- Building hierarchical tree structures
- Finding paths between nodes
- Reorienting trees from different node perspectives
"""

from __future__ import annotations
import json
import dataclasses
import itertools


@dataclasses.dataclass
class Tree:
    """A tree node with a label and zero or more children.
    
    Attributes:
        label: String identifier for this node
        children: List of child Tree nodes (automatically sorted)
    """
    
    label: str
    children: list[Tree] | None = dataclasses.field(default_factory=list)

    def __post_init__(self):
        """Normalize label to string and sort children alphabetically."""
        self.label = str(self.label)
        self.children = sorted(self.children)

    def to_dict(self):
        """Convert tree to nested dictionary representation.
        
        Returns:
            Dictionary with label as key and sorted children as value
        """
        return {self.label: [child.to_dict() for child in sorted(self.children)]}

    def __str__(self, indent=1):
        """Return JSON string representation of the tree."""
        return json.dumps(self.to_dict(), indent=indent)

    def __lt__(self, other):
        """Compare trees by label for sorting."""
        return self.label < other.label

    def __hash__(self):
        """Make tree hashable based on label and children tuple."""
        return hash((self.label, tuple(self.children)))

    def path_from_self(self, node: Tree | None, to_node: str) -> list[Tree] | None:
        """Find path from given node to target node using depth-first search.
        
        Args:
            node: Starting node for the search
            to_node: Label of the target node
            
        Returns:
            List of Tree nodes from start to target, or None if no path exists
        """
        stack = [(node, [node])]
        while stack:
            current, path = stack.pop()
            if current.label == to_node:
                return path
            for child in current.children:
                stack.append((child, path + [child]))

        return None

    def from_pov(self, from_node: str) -> Tree:
        """Reorient the tree from the perspective of a different node.
        
        Transforms the tree so that the specified node becomes the root,
        with parent-child relationships reversed along the path.
        
        Args:
            from_node: Label of the node to become the new root
            
        Returns:
            New Tree with from_node as root
            
        Raises:
            ValueError: If from_node is not found in the tree
        """
        if self.label == from_node:
            return self
            
        path = self.path_from_self(self, from_node)
        if path is None:
            raise ValueError('Tree could not be reoriented')
    
        current_tree = None
        for node, next_node in itertools.pairwise(path):
            children_list = [child for child in node.children if child != next_node]
            if current_tree:
                children_list.append(current_tree)
            current_tree = Tree(node.label, children_list)
            
        return Tree(path[-1].label, path[-1].children + [current_tree] if current_tree else path[-1].children)

    def path_to(self, from_node: str, to_node: str) -> list[str]:
        """Find path between two nodes after reorienting from first node.
        
        Args:
            from_node: Starting node label (becomes temporary root)
            to_node: Target node label
            
        Returns:
            List of node labels from from_node to to_node
            
        Raises:
            ValueError: If either node is not found or no path exists
        """
        if (trees := self.path_from_self(self.from_pov(from_node), to_node)) is None:
            raise ValueError('No path found')
        return [tree.label for tree in trees]