from three import första_mellan_andra_tredje

första_mellan_andra_tredje


assert callable(första_mellan_andra_tredje)
assert första_mellan_andra_tredje(5, 0, 10)
assert första_mellan_andra_tredje(1, -1, 5)
assert första_mellan_andra_tredje(101, 100, 102)
assert första_mellan_andra_tredje(-30, -50, -25)
assert not första_mellan_andra_tredje(0, 0, 0) 
assert not första_mellan_andra_tredje(0, 0, 1)
assert not första_mellan_andra_tredje(1, 0, 1)
assert not första_mellan_andra_tredje(-1, -1, 0)


