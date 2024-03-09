def theorem_3(arr):
    A = max(abs(x) for x in arr[:-2])
    B = max(abs(x) for x in arr[1:])    
    
    r = 1 / (1 + B / abs(arr[0])) 
    R = 1  + A / abs(arr[-1]) 
    
    return r, R

def theorem_4(arr):
    if arr[-1] < 0:
        arr = [-x for x in arr]
        
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < 0:
            break
    C = max(abs(a) for a in arr if a < 0)

    return 1 + (C / arr[-1]) ** (1 / (len(arr)-1 - i)) 

def theorem_5(arr):
    R = theorem_4(arr)
    R_1 = theorem_4(list(reversed(arr)))
    R_2 = theorem_4([-a for a in arr])
    R_3 = theorem_4([-a for a in list(reversed(arr))])
    
    return (1/R_1, R), (-R_2, 1/R_3)

arr = [1, 2, -5, 8, -7, -3] 

print(theorem_3(arr))  
print(theorem_4(arr)) 
print(theorem_5(arr))