import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # used to implement pytest in a modularized project

from Imports.add import Add
from Imports.divide import Divide


def test_added_answer():
    assert Add(5, 5) == 10
    
def test_divided_fail():
    assert Divide(2, 0) == "CANNOT DIVIDE BY ZERO"

def test_divided_answer():
    assert Divide(9, 3) == 3