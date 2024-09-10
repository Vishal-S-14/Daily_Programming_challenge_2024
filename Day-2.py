def miss_n(a):
    n = len(a) + 1
    e_s = n * (n + 1) // 2
    a_s = sum(a)
    return e_s - a_s

print(miss_n([1, 2, 4, 5]))  
print(miss_n([2, 3, 4, 5])) 
print(miss_n([1, 2, 3, 4]))  
print(miss_n([1]))       
print(miss_n(list(range(1, 1000000))))