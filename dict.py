d1 = {3:2, 1:4, 5:6}
d2 = {2:4, 6:6}
d3 = {4:1, 9:9, 4:16, 5:25}

def find_in_L(Ld,k):
    for d in Ld:
        if k in d:
            return True
    return False

def count_match(d):
    count = 0
    for k,v in list(d.items()):
        if k == v:
            count+=1
    return count



dcopy = d1.copy()

print(dcopy)