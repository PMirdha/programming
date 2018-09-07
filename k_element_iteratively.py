def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def kth_elem(A, k):
    p = -1
    s = 0
    e = len(A) - 1
    ans = None
    if k<=0 or k>len(A):
        return None
    
    while(True):
    # while(p+1 != k):
        p = s - 1
        x = A[e]
        for i in range(s, e + 1):
            if A[i] <= x:
                swap(A, i, p+1)
                p += 1
        # print("pivot", p, A, s, e)
        if p+1 == k:
            ans = A[p]
            break
        elif p+1 < k:
            s = p+1
            # k = k-p-1
        elif p+1 > k:
            e = p-1
    return ans

print(kth_elem([5,2,3,1,4], 3))