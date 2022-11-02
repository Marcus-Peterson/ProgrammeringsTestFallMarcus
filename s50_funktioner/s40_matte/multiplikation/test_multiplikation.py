import unittest
from multiplikation import gånger

assert(callable(gånger))
assert(gånger(2, 7) == 14)
assert(gånger(2, 2) == 4)
assert(gånger(-5, -5) == 25)
