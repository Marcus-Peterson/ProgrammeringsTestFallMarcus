import unittest
from subtraktion import minus

assert(callable(minus))
assert(minus(2, 7) == -5)
assert(minus(2, 2) == 0)
assert(minus(0, 5) == -5)
assert(minus(0, -5) == 5)
