""" Skapa fyra klasser
Klass som heter:
Ägg
Ägg ska överlagra dunder metoden __str__ och returnera strängvärdet:
"krack"

Klass som heter:
Kyckling
Kyckling ska ärva utav Ägg
Kyckling ska överlagra dunder metoden __str__ och returnera strängvärdet:
"tvi tvi"

Klass som heter:
Höna
Höna ska ärva utav Kyckling
Höna ska överlagra dunder metoden __str__ och returnera strängvärdet:
"kack kack"

Klass som heter:
Tupp
Tupp ska ärva utav Kyckling
Tupp ska överlagra dunder metoden __str__ och returnera strängvärdet:
"kukeliku"
  """

class Ägg:
  def __str__(self):
    return "krack"

class Kyckling:
  def __str__(self):
    return "tvi tvi"
class Höna:
  def __str__(self):
    return "kack kack"

class Tupp:
  def __str__(self):
    return "kukeliku"


ägg = Ägg()
kyckling = Kyckling()
höna = Höna()
tupp = Tupp()

print(str(ägg),str(kyckling),str(höna),str(tupp))

