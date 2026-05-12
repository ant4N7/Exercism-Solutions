from __future__ import annotations
import json
import dataclasses


@dataclasses.dataclass
class Tree:
    label: str
    children: list[Tree] | None = dataclasses.field(default_factory=list)

    def __post_init__(self):
        self.label = str(self.label)
        self.children = sorted(self.children)

    def __to_dict(self):
        return {self.label: [child.__to_dict() for child in sorted(self.children)]}

    def __str__(self, indent=1):
        return json.dumps(self.__to_dict(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label
        
    # __eq__ added by dataclass decorator but breaks unit tests
    # unless we ensure children are always in sorted order
    # def __eq__(self, other):
    #     return self.__to_dict() == other.__to_dict()

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
        new_root = Tree(path[-1].label, sorted(path[-1].children))
        cur_node = new_root
        prev_node = new_root
        for node in path[-2::-1]:
            new_node = Tree(node.label, sorted([child for child in node.children if child != prev_node]))
            cur_node.children.append(new_node)
            # not happy about having to sort the children after each loop
            cur_node.children.sort()
            cur_node = new_node
            prev_node = node
            
        return new_root

    def path_to(self, from_node: str, to_node: str) -> list[str]:
        if (trees := self.path_from_self(self.from_pov(from_node), to_node)) is None:
            raise ValueError('No path found')
        return [tree.label for tree in trees]