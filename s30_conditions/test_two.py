from two import första_mindre_än_andra

assert callable(första_mindre_än_andra)
assert första_mindre_än_andra(100, 200)
assert första_mindre_än_andra(-4, 4)
assert första_mindre_än_andra(-4, -2)
assert första_mindre_än_andra(-1, 0)
assert första_mindre_än_andra(5.1, 6) 
assert not första_mindre_än_andra(0, 0)
assert not första_mindre_än_andra(1, 0)
assert not första_mindre_än_andra(0, -1)


