import unittest
from modulo import restdivision

assert(callable(restdivision))
assert(restdivision(1, 2) == 1)
assert(restdivision(4, 5) == 4)
assert(restdivision(15, 3) == 0)
