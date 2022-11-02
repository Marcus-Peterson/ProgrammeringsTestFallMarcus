from one import större_än_fem
from one import större_eller_likamed_fem

assert callable(större_än_fem)
assert större_än_fem(100)
assert större_än_fem(6)
assert not större_än_fem(5)
assert större_än_fem(5.1) 
assert not större_än_fem(5.0)
assert not större_än_fem(-1)
assert not större_än_fem(0)


assert callable(större_eller_likamed_fem)
assert större_eller_likamed_fem(100)
assert större_eller_likamed_fem(6)
assert större_eller_likamed_fem(5)
assert större_eller_likamed_fem(5.1) 
assert större_eller_likamed_fem(5.0)
assert not större_eller_likamed_fem(4.9)
assert not större_eller_likamed_fem(-1)
assert not större_eller_likamed_fem(0)
