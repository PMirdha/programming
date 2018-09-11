from utility import swap



def median_of_medians(A, x, s, e):
    pass

def partition(A, index, s, e):
    swap(A, index, e)
    x = A[e]
    p = s-1
    for i in range(s, e+1):
        if A[i] <= x:
            swap(A, i, p+1)
            p += 1
    return p

def selection_linear(A, k, s, e):
    median_index = median_of_medians(A, 5, s, e)
    pivot = partition(A, median_index, s, e)
    p = pivot-s+1
    if p==k:
        return A[p]
    elif p>k:
        return selection_linear(A, k, s, p-1)
    elif p<k:
        return selection_linear(A, k-p, p+1, e)

def solve(A, k):
    print("kth smallest", selection_linear(A, k, 0, len(A)-1))



solve([9,8,7,6,5,4,3,2,1], 3)