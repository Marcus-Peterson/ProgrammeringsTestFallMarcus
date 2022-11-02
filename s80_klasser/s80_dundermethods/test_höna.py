from höns import Höna
from höns import Tupp
from höns import Kyckling
from höns import Ägg


enHöna = Höna()
enTupp = Tupp()
enKyckling = Kyckling()
ettÄgg = Ägg()

assert issubclass(Höna, Kyckling)
assert issubclass(Tupp, Kyckling)
assert issubclass(Höna, Ägg)
assert issubclass(Tupp, Ägg)
assert issubclass(Kyckling, Ägg)
assert str(enTupp) == "kukeliku"
assert str(enKyckling) == "tvi tvi"
assert str(enHöna) == "kack kack"
assert str(ettÄgg) == "krack"