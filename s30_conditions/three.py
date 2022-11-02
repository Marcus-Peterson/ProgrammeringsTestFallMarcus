""" skapa en funktion som tar tre argument
 som returnerar om första argumentet är större än argument två och mindre än argument tre
namnet på funktionen ska vara:
första_mellan_andra_tredje
"""

def första_mellan_andra_tredje(arg1,arg2,arg3):
    if arg1 > arg2 and arg1 < arg3:
        return "arg1 > arg2 and arg1 < arg3"
    else:
        return"NONE"

print(första_mellan_andra_tredje(3, 2, 5))