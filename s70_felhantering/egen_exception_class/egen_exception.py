""" Skapa en egen exception class som heter:
EgenException
Klassen ska ärva utav 
Exception  """

class EgenException(Exception):
    pass

""" Skapa en funktion som heter:
Kasta
Funktionen ska kasta/raise EgenException
"""

def Kasta():
    raise EgenException()

print(Kasta())

