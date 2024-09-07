
def puissance1(n) :
    if n == 0 :
        return 1
    else :
        return 2*puissance1(n-1)
    
def puissance2(n) :
    if n == 0 :
        return 1
    else :
        return (puissance2(n-1) + puissance2(n-1))
    
print(puissance2(3))