import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6) 

BinTree: TypeAlias = Union['Node', None]

@dataclass(frozen=True)
class Node:
    val: Any
    left: BinTree
    right: BinTree

@dataclass(frozen=True)
class BinarySearchTree:
    comes_before: Callable[[Any, Any], bool]
    bin_tree: BinTree = None

# Returns True if 'bst' is empty
def is_empty(bst: BinarySearchTree) -> bool:
    return bst.bin_tree is None
    
# Returns the given binary search tree with the 'value' inserted
def insert(bst: BinarySearchTree, value: Any) -> BinarySearchTree:

    def insert_helper(tree: BinTree, value: Any, comes_before: Callable[[Any, Any], bool]) -> BinTree:
        if tree is None:
            return Node(value, None, None)
        elif bst.comes_before(value, tree.val):
            return Node(
                tree.val,
                insert_helper(tree.left, value, comes_before),
                tree.right )
        else:
            return Node(
                tree.val,
                tree.left,
                insert_helper(tree.right, value, comes_before) )
        return tree
     
    new_bin_tree = insert_helper(bst.bin_tree, value, bst.comes_before)
    return BinarySearchTree(bst.comes_before, new_bin_tree)

# Returns True if the 'value' is in the binary search tree
def lookup (bst: BinarySearchTree, value: Any) -> bool:
    
    def lookup_helper(tree: BinTree, value: Any) -> bool:
        if tree is None:
            return False
        if bst.comes_before(tree.val, value):
            return lookup_helper(tree.right, value)
        elif bst.comes_before(value, tree.val):
            return lookup_helper(tree.left, value)
        else:
            return True

    return lookup_helper(bst.bin_tree, value)

# Returns the minimum value of a given binary tree
def find_min(tree: BinTree) -> Any:
    if tree is None:
        return None
    while tree.left is not None:
        tree = tree.left
    return tree.val

# Returns the binary search tree with the value deleted from it
def delete(bst: BinarySearchTree, value:Any) -> BinarySearchTree:
    
    def delete_helper(tree: BinTree, value: Any) -> BinTree:
        if tree is None:
            return None
        
        if bst.comes_before(value, tree.val):
            return Node(tree.val, delete_helper(tree.left, value), tree.right)
        elif bst.comes_before(tree.val, value):
            return Node(tree.val, tree.left, delete_helper(tree.right, value))
        else:
            if tree.left is None and tree.right is None:
                return None
            elif tree.left is None:
                return tree.right
            elif tree.right is None:
                return tree.left
            else:
                smallest = find_min(tree.right)
                return Node(smallest, tree.left, delete_helper(tree.right, smallest))
            
    return BinarySearchTree(bst.comes_before, delete_helper(bst.bin_tree, value))


        

    


    



    