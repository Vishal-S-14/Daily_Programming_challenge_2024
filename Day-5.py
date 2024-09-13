def leader(a):
    l = []
    rt = a[-1]
    l.append(rt)
    
    for i in range(len(a) - 2, -1, -1):
        if a[i] >= rt:
            l.append(a[i])
            rt = a[i]
    
    l.reverse()
    return l

print(leader([16, 17, 4, 3, 5, 2]))
print(leader([1, 2, 3, 4, 0]))
print(leader([7, 10, 4, 10, 6, 5, 2]))
print(leader([5]))
print(leader([100, 50, 20, 10]))