from four import type_checking


assert type_checking(True) == "Det var en boolean"
assert type_checking(False) == "Lögnare!"
assert callable(type_checking)
assert type_checking(42) == "Answer to the Ultimate Question of Life, the Universe, and Everything"
assert not type_checking(42.0) == "Answer to the Ultimate Question of Life, the Universe, and Everything"
assert type_checking(100) == "Det var ett heltal"
assert type_checking(100) == "Det var ett heltal"
assert type_checking(0) == "Det var ett heltal"
assert type_checking(0.0) == "Det var ett flyttal"
assert type_checking(-0.1) == "Var inte så negativ"
assert type_checking(-2.1) == "Var inte så negativ"
assert type_checking(True) == "Det var en boolean"
assert type_checking(False) == "Lögnare!"
assert type_checking("en sträng") == "Det var en sträng"
assert type_checking("Hej!") == "Hej på dig!"






