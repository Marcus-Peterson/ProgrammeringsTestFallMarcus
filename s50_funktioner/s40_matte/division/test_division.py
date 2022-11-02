import unittest
from division import delat


assert(callable(delat))
assert(delat(4, 2) == 2.0)
assert(delat(5, 2) == 2.5)
assert(delat(-2, 1) == -2)
assert(delat(0, 1) == 0)
assert(delat(1, 2) == 0.5)


