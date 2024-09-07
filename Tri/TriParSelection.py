tab = [5,14,7,9,0,5,18,33,40]


def triParSelection(tab) :
    length = len(tab)
    temp = 0
    for i in range(length) :
        min = i
        for j in range(i+1,length):
            if(tab[j]<tab[min]) :
                min = j

        (tab[min],tab[i]) = (tab[i],tab[min])
    return tab

print (triParSelection(tab))    
