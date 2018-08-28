
class QuickSort(object):

    def divideM1(self, A, s, e, index):
        val = A[index]
        self.swap(A, index, s)
        p1 = s + 1
        p2 = e
        while p1<p2:
            if A[p1] <= val:
                p1 += 1
            else:
                if A[p2] <= val:
                    self.swap(A, p1, p2)
                    p1 += 1
                p2 -= 1
        d_index = s

        if A[p1] > val:
            self.swap(A, p1-1, s)
            d_index = p1-1
        else:
            self.swap(A, p1, s)
            d_index = p1

        return d_index
    
    def divideM2(self, A, s, e, index):
        X = A[index]
        self.swap(A, index, e)
        LEP = s-1
        for FP in range(s, e+1):
            if A[FP] <= X:
                self.swap(A, LEP+1, FP)
                LEP += 1
        
        return LEP
    
    def swap(self, A, i, j):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
        return A

if __name__ == '__main__':
    obj = QuickSort()
    
    ri = raw_input("Enter list items to be sorted\n").strip()
    A = ri.split(" ")
    A = list(map(int, A))
    ri = raw_input("Enter list items to be sorted\n").strip()
    index = int(ri)
    print(obj.divideM2(A, 0, len(A) - 1, index))
    print(A)
