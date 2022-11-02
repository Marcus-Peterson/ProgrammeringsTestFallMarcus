""" skapa en funktion som tar ett argument som returnerar om värdet är större 5 
namnet på funktionen ska vara:
större_än_fem
"""
def större_än_fem(arg):
    if arg > 5:
        return "Större än fem"
    else:
        return "inte större än fem"

""" skapa en funktion som tar ett argument som returnerar om värdet är större eller lika med 5 
namnet på funktionen ska vara
större_eller_likamed_fem
"""

def större_eller_likamed_fem(arg):
    if arg >= 5:
        return "större eller lika med fem"
    else:
        return "mindre än fem"


print(större_eller_likamed_fem(5))




