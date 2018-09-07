
def q_sort(R, B, s, e):
    if e <= s:
        return
    pivot = divide(R, B, s, e)
    q_sort(R, B, s, pivot -1)
    q_sort(R, B, pivot + 1, e)

def divide(R, B, s, e):
    pivot, equal_index = rearrange(R, B[e], s, e)
    swap(R, pivot, equal_index)
    pivot, equal_index = rearrange(B, R[pivot], s, e)
    swap(B, pivot, equal_index)
    return pivot

def rearrange(A, x, s, e):
    LEP = s - 1
    equal_index = None
    for i in range(s, e + 1):
        if A[i] <= x:
            if A[i] == x:
                equal_index = LEP + 1
            swap(A, LEP + 1, i)
            LEP += 1
    return LEP, equal_index

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def solve(R, B):
    q_sort(R, B, 0, len(R) - 1)
    print("R = ", R)
    print("B = ", B)




solve([4,2,5,1,3], [3,1,4,5,2])

