tab = [5,14,7,9,0,5,18,33,40]

def BubbleSort(arr):
    length = len(arr)
    for i in range(length):
        for j in range (length-1):
            if arr[j]>arr[j+1] :
                (arr[j],arr[j+1]) = (arr[j+1],arr[j])
    return arr

print (BubbleSort(tab))