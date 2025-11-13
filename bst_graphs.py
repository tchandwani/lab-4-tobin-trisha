import sys
import unittest
from typing import *
from dataclasses import dataclass
import math 
import matplotlib.pyplot as plt
import numpy as np
import time
import random
sys.setrecursionlimit(10**6)
from bst import *

TREES_PER_RUN : int = 10000

def height_of_tree(tree: BinTree) -> int:
    if tree is None:
        return 0
    else:
        return 1 + max(height_of_tree(tree.left),height_of_tree(tree.right))
    
# 250 seems to be a good amount
# Returns a BinarySearchTree filled with n random numbers
def random_tree(num: int) -> BinarySearchTree:
    tree: BinarySearchTree = BinarySearchTree(lambda a,b: a < b,None)
    #for _ in range(TREES_PER_RUN):
    for __ in range(num+1):
        tree = insert(tree,random.random())
    return tree

def example_graph_creation() -> None:
     # Return log-base-2 of 'x' + 5.
    def f_to_graph (x: float) -> float:
        return math.log2( x ) + 5.0

     # here we're using "list comprehensions": more of Python's
     # syntax sugar.
    x_coords : List[float] = [ float(i) for i in range( 1, 100 ) ]
    y_coords : List[float] = [f_to_graph( x ) for x in x_coords ]
     # Could have just used this type from the start, but I want
     # to emphasize that 'matplotlib' uses 'numpy''s specific array
     # type, which is different from the built-in Python array
     # type.
    x_numpy : np.ndarray = np.array( x_coords )
    y_numpy : np.ndarray = np.array( y_coords )
    plt.plot( x_numpy, y_numpy, label = 'log_2(x)' )
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Example Graph")
    plt.grid(True)
    plt.legend() # makes the 'label's show up
    plt.show()

if (__name__ == '__main__'):
    print(random_tree(5))
    print(height_of_tree(random_tree(5).bin_tree))
    """
    start = time.perf_counter()
    random_tree(250)
    end = time.perf_counter()
    print(end-start)
    """