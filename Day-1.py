def sort(a):
    l = 0
    m = 0
    h = len(a) - 1
    
    while m <= h:
        if a[m] == 0:
            a[l], a[m] = a[m], a[l]
            l += 1
            m += 1
        elif a[m] == 1:
            m += 1
        else:
            a[h], a[m] = a[m], a[h]
            h -= 1

a = [0, 1, 2, 1, 0, 2, 1, 0]
sort(a)
print(a)

b = [2, 2, 2, 2]
sort(b)
print(b)

c = [0, 0, 0, 0]
sort(c)
print(c)

d = [1, 1, 1, 1]
sort(d)
print(d)

e = [2, 0, 1]
sort(e)
print(e)

f = []
sort(e)
print(e)