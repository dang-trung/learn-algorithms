import numpy as np
def merge(A, p, q, r): # merge two sorted subarrays into one sorted arrays
    L = A[p:(q+1)] 
    R = A[(q+1):(r+1)]
    L = np.append(L, np.inf)
    R = np.append(R, np.inf)
    i = 0
    j = 0
    for k in range(p, r+1): 
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j = j+1

def sort_merge(A):
    if A.size > 1:
        # Divide
        p = 0 
        r = A.size - 1
        q = round((p+r)/2 + 0.6) - 1 
        # Conquer
        sort_merge(A[p:(q+1)])
        sort_merge(A[(q+1):(r+1)])
        # Combine
        merge(A, p, q, r)
    