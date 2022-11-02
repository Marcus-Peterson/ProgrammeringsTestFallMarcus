""" skapa en funktion som heter:
restdivision
som tar två argument och delar det första argumentet med det andra argumentet
 och returnernar resten/modulo"""

def restdivision(arg1,arg2):
    rest = arg1%arg2
    return rest

print(restdivision(4, 2))
