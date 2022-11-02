""" skriv en funktion för upphöjt som tar två argument
namnet på funktionen ska vara: 
upphöjt """


from math import pow

def upphöjt(arg1,arg2):
    upp = pow(arg1,arg2)
    return upp

def upphöjt_2(arg1,arg2):
    upp = arg1**arg2
    return upp

print(upphöjt(4, 4))
print(upphöjt_2(4, 4))