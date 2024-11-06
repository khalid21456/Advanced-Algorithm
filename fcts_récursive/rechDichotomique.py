
tab = [1,4,5,9,14,30,31,45,100]


def binarySearch(T,elem,debut,fin):
    if fin<debut:
        return -1
    milieu = (debut+fin)//2
    if elem == T[milieu] :
        return milieu
    elif elem < T[milieu] :
        return binarySearch(T,elem,debut,milieu-1)
    else :
        return binarySearch(T,elem,milieu+1,fin)

result = binarySearch(tab,5,0,8)
print (result)