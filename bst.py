import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6) 

BinTree: TypeAlias = Union['Node', None]

@dataclass (frozen=True)
class Node:
    val: Any
    left: BinTree
    right: BinTree

@dataclass(frozen=True)
class BinarySearchTree:
    comes_before: Callable[[Any, Any], bool]
    bin_tree: BinTree = None

def is_empty(bst: BinarySearchTree) -> bool:
    return bst.bin_tree is None
    
def insert(bst: BinarySearchTree, value: Any) -> BinTree:
    if bst.bin_tree is None:
        return Node(value, None, None)
    
    def insert_helper(bin_tree: BinTree), value: Any, comes_before: Callable[[Any, Any], bool]):
        if bst.comes_before(value, bst.bin_tree.val):
            return Node(value, bst.bin_tree.left, bst.bin_tree.right)
    

    



    
