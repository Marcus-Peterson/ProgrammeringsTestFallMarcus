import unittest
from floordivision import heltalsdivision

assert(callable(heltalsdivision))
assert(heltalsdivision(14, 7) == 2)
assert(heltalsdivision(3, 2) == 1)
assert(heltalsdivision(17, 4) == 4)
