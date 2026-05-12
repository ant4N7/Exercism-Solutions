from __future__ import annotations
import json
import dataclasses
import itertools


@dataclasses.dataclass
class Tree:
    label: str
    children: list[Tree] | None = dataclasses.field(default_factory=list)

    def __post_init__(self):
        self.label = str(self.label)
        self.children = sorted(self.children)

    def to_dict(self):
        return {self.label: [child.to_dict() for child in sorted(self.children)]}

    def __str__(self, indent=1):
        return json.dumps(self.to_dict(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    # requested by Linter
    def __hash__(self):
        return hash((self.label, tuple(self.children)))

    def path_from_self(self, node: Tree | None, to_node: str) -> list[Tree] | None:        
        if node.label == to_node:
            return [node]
        
        for child in node.children:
            path = self.path_from_self(child, to_node)
            if path:
                return [node] + path
        
        return None

    def from_pov(self, from_node: str) -> Tree:        
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
        if (trees := self.path_from_self(self.from_pov(from_node), to_node)) is None:
            raise ValueError('No path found')
        return [tree.label for tree in trees]