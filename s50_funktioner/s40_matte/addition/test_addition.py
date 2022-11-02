import unittest
from addition import plus


assert(callable(plus))
assert(plus(5, 7) == 12), "5 + 7 är likamed 12"
assert(plus(2, 7) == 9)
assert(plus(-2, -5) == -7)

