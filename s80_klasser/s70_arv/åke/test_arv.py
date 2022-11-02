import unittest
from arv import Fisk
from arv import Gädda
from arv import Aborre

enFisk = Fisk(50)
enGädda = Gädda(100)
enAborre = Aborre(75)

assert(type(enFisk) == Fisk)
assert(isinstance(enGädda, Fisk))
assert(isinstance(enAborre, Fisk))
assert(type(enGädda) == Gädda)
assert(type(enAborre) == Aborre)
assert(enFisk.simhastighet == 50)
assert(enGädda.simhastighet == 100)
assert(enAborre.simhastighet == 75)