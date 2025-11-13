import sys
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

# Returns the max height/depth of a binary tree
def height_of_tree(tree: BinTree) -> int:
    if tree is None:
        return 0
    else:
        return 1 + max(height_of_tree(tree.left),height_of_tree(tree.right))

# 250 seems to be a good amount
# Returns a BinarySearchTree filled with n random numbers
def random_tree(num: int) -> BinarySearchTree:
    tree: BinarySearchTree = BinarySearchTree(lambda a,b: a < b,None)
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

def graph_1(n_max: int):
    print(list(range(0,n_max+1,int(n_max/50))))
    valid_N_values: list[int] = list(range(0,n_max+1,int(n_max/50)))
    results: list[float] = []
    for N in valid_N_values:
        heights_per_N: list[int] = []
        #start = time.perf_counter()
        for _ in range(TREES_PER_RUN):
            height = height_of_tree(random_tree(N).bin_tree)
            heights_per_N.append(height)
            #print(f"run {i+1}/{TREES_PER_RUN} at N={N} complete")
        #print(heights_per_N)
        results.append(sum(heights_per_N) / len(heights_per_N))
        print(f"graph 1 Analysis at N={N} complete")
    print(results)

    x_coords : List[int] = valid_N_values
    y_coords : List[float] = results
     # Could have just used this type from the start, but I want
     # to emphasize that 'matplotlib' uses 'numpy''s specific array
     # type, which is different from the built-in Python array
     # type.
    x_numpy : np.ndarray = np.array( x_coords )
    y_numpy : np.ndarray = np.array( y_coords )
    plt.plot( x_numpy, y_numpy, label = 'log_2(N)' )
    plt.xlabel(f"N={valid_N_values[0]} to {valid_N_values[len(valid_N_values)-1]}")
    plt.ylabel("Average height of binary tree at size N)")
    plt.title("Average heights of binary trees at size N")
    plt.grid(True)
    plt.legend() # makes the 'label's show up
    plt.show()

def graph_2(n_max: int):
    print(list(range(0,n_max+1,int(n_max/50))))
    valid_N_values: list[int] = list(range(0,n_max+1,int(n_max/50)))
    results: list[float] = []
    for N in valid_N_values:
        #times_per_N: list[float] = []
        #start = time.perf_counter()
        start = time.perf_counter()
        for _ in range(TREES_PER_RUN):
            random_tree(N)
            #print(f"run {i+1}/{TREES_PER_RUN} at N={N} complete")
        end = time.perf_counter()
        #times_per_N.append(end-start)
        results.append(end-start)
        print(f"graph 2 Analysis at N={N} complete")
    print(results)

    x_coords : List[int] = valid_N_values
    y_coords : List[float] = results
     # Could have just used this type from the start, but I want
     # to emphasize that 'matplotlib' uses 'numpy''s specific array
     # type, which is different from the built-in Python array
     # type.
    x_numpy : np.ndarray = np.array( x_coords )
    y_numpy : np.ndarray = np.array( y_coords )
    plt.plot( x_numpy, y_numpy, label = 'O(N)' )
    plt.xlabel(f"N={valid_N_values[0]} to {valid_N_values[len(valid_N_values)-1]}")
    plt.ylabel("Average insertion time into binary tree of size N")
    plt.title("Average times taken to insert a value into binary trees of size N")
    plt.grid(True)
    plt.legend() # makes the 'label's show up
    plt.show()

if (__name__ == '__main__'):
    #graph_1(100)
    graph_2(100)    