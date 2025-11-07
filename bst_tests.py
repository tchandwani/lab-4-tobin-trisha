import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)
from bst import *
import math

@dataclass (frozen=True)
class Point2:
    x: float
    y: float

    def distance_from_origin(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    
class BSTTests(unittest.TestCase):
    def test_integer_ordering(self):
        compare : Callable[[int, int], bool] = lambda a, b: a < b
        
        bst = BinarySearchTree(compare, None)
        bst = insert(bst, 5)
        bst = insert(bst, 3)
        bst = insert(bst, 7)
        
        self.assertTrue(lookup(bst, 5))
        self.assertTrue(lookup(bst, 3))
        self.assertFalse(lookup(bst, 10))
        
        bst = delete(bst, 5)
        self.assertFalse(lookup(bst, 5))
        
    def test_string_ordering(self):
        string_compare : Callable[[str, str], bool] = lambda a, b: a < b

        bst = BinarySearchTree(string_compare, None)
        bst = insert(bst, "apple")
        bst = insert(bst, "banana")
        bst = insert(bst, "orange")

        self.assertTrue(lookup(bst, "apple"))
        self.assertTrue(lookup(bst, "banana"))
        self.assertFalse(lookup(bst, "avacado"))
        
        bst = delete(bst, "apple")
        self.assertFalse(lookup(bst, "apple"))

    def test_euclidean_distance(self):
        point_compare : Callable[[Point2, Point2], bool] = lambda p1, p2: p1.distance_from_origin() < p2.distance_from_origin()

        bst = BinarySearchTree(point_compare, None)

        p1 = Point2(3, 4) # distance=5
        p2 = Point2(1, 1) # distance=1.41
        p3 = Point2(5, 5) # distance=7.07
        p4 = Point2(0, 2) # distance=2

        bst = insert(bst, p1) 
        bst = insert(bst, p2)  # left 
        bst = insert(bst, p3)  # right
        bst = insert(bst, p4)  # left of p1, right of p2

        self.assertTrue(lookup(bst, p1))
        self.assertTrue(lookup(bst, p2))
        self.assertTrue(lookup(bst, p3))

        bst = delete(bst, p1)
        self.assertFalse(lookup(bst, p1))
        self.assertTrue(lookup(bst, p2))

if (__name__ == '__main__'):
 unittest.main() 