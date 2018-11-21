
def präf(tupel):
    
    raus= ""
    raus+=tupel[1]
    if type(tupel[0])==tuple:
        raus+=präfix(tupel[0])
    else:
        raus+=str(tupel[0])
    if type(tupel[2])== tuple:
        raus+=präfix(tupel[2])
    else:
        raus+=str(tupel[2])
    return raus

def postf(tupel):
    raus = ""
    if type(tupel[0]) ==  tuple:
        raus+=postfix(tupel[0])
    else:
        raus+=str(tupel[0])
    if type(tupel[2])==  tuple:
        raus +=postfix(tupel[2])
    else:
        raus+= str(tupel[2])
    raus += tupel[1]
    return raus

def inf(tupel):
    
    raus = "("
    if type(tupel[0])==tuple:
        raus+=infix(tupel[0])
    else:
        raus+=str(tupel[0])
    raus+=tupel[1]
    if type(tupel[2])== tuple:
        raus+=infix(tupel[2])
    else:
        raus+=str(tupel[2])
    return raus+")"


x = ((2, "+", 3), "+", 4)
print("Präfixnotation: " + präfix(x))
print("Postfixnotation: " + postfix(x))
print("Infixnotation: " + infix(x))

