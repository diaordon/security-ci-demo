# Make repo root importable when tests run on GitHub Actions
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import add, mul

def test_add():
    assert add(2, 3) == 5

def test_mul():
    assert mul(2, 4) == 8

