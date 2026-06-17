from __future__ import annotations
from json import dumps

class Tree:
    def __init__(self, label, children=None):
        self.label = str(label)
        self.children = children if children is not None else []

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=1):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    # requested by Linter
    def __hash__(self):
        return hash((self.label, tuple(self.children)))

    def path_from_self(self, node: Tree | None, to_node: str):        
        if node.label == to_node:
            return [node]
        
        for child in node.children:
            path = self.path_from_self(child, to_node)
            if path:
                return [node] + path
        
        return None

    def from_pov(self, from_node: str):        
        if self.label == from_node:
            return self

        q = self.path_from_self(self, from_node)
        if q is None:
            raise ValueError('Tree could not be reoriented')
        new_root = Tree(q[-1].label, [c for c in q[-1].children])
        cur_node = new_root
        prev_node = new_root
        for node in q[-2::-1]:
            new_node = Tree(node.label, [c for c in node.children if c != prev_node])
            cur_node.children.append(new_node)
            cur_node = new_node
            prev_node = node
            
        return new_root

    def path_to(self, from_node: str, to_node: str):
        if (trees:= self.path_from_self(self.from_pov(from_node), to_node)) is None:
            raise ValueError('No path found')
        return [t.label for t in trees]