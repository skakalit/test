#((3,5,-26),4,((3,3,2),1,((-12,9,120),-11,7)))
#((111,-16,-26),81,-7))
def summiere(tupel,ebene):
    summe=0
    summe+=ebene*tupel[1]
    if type(tupel[0])==tuple:
        summe+=summiere(tupel[0], ebene+1)
    else:
        summe+=(ebene+1)*tupel[0]
    if type(tupel[2]) == tuple:
        summe+=summiere(tupel[2], ebene+1)
    else:
        summe+=(ebene+1)*tupel[2]
    return summe

x=((111,-16,-26),81,-7)
y=((3,5,-26),4,((3,3,2),1,((-12,9,120),-11,7)))
print("290 =", summiere(x,1),"und 547 =", summiere(y,1))

