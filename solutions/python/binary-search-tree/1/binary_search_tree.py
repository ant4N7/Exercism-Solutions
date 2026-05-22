from __future__ import annotations
import dataclasses


@dataclasses.dataclass
class TreeNode:
    data: str
    left: TreeNode = None
    right: TreeNode = None

class BinarySearchTree:
    def __init__(self, tree_data: list[str]):
        self.root = None
        for data in tree_data:
            self.insert(data)

    def data(self) -> TreeNode:
        return self.root

    def sorted_data(self) -> list[str]:
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node: TreeNode, result: list[str]):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.data)
            self._inorder_traversal(node.right, result)
    
    def insert(self, data: str):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node: TreeNode, data: str):
        if int(data) <= int(node.data):
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)