tab = [5,14,7,9,0,5,18,33,40]

def quicksort(array):
  if len(array) < 2:
    return array
  else:
    pivot = array[0] 
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot] 
    return quicksort(less) + [pivot] + quicksort(greater)
  

print(quicksort(tab))