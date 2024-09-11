def duplicate(a):
    l = 1
    h = len(a) - 1

    while l < h:
        m = (l + h) // 2
        count = 0
        for i in a:
            if i <= m:
                count += 1
        if count > m:
            h = m
        else:
            l = m + 1

    return l

a = [1, 3, 4, 2, 2]
print(duplicate(a))  

b = [3, 1, 3, 4, 2]
print(duplicate(b)) 

c = [1, 1]
print(duplicate(c)) 

d = [1, 4, 4, 2, 3]
print(duplicate(d))

e = list(range(1, 100000)) + [50000] 
print(duplicate(e))
