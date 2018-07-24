class LinkList:
    value = None
    next = None

class DoublyLinkList:
    value = None
    next = None
    prev = None

class Sort:
    
    def ListInsertionSort(self, A):
        n = len(A)

        for i in range(1, n):
            j = i-1
            key = A[i]
            while(j>=0 and A[j]>key):
                A[j+1] = A[j]
                j -= 1
            A[j+1] = key
        
        return A
    
    def SelectionSort(self, A):
        n = len(A)

        for p1 in xrange(n-1):
            key = p1
            c_min = A[key]
            for p2 in xrange(p1+1, n):
                if c_min>A[p2]:
                    c_min = A[p2]
                    key = p2
            if key != p1:
                self.swap(A, key, p1)
        return A

    def MergeSortRec(self, A, l, r):
        if l<r:
            m = int((l+r)/2)
            self.MergeSortRec(A, l, m)
            self.MergeSortRec(A, m+1, r)
            self.Merge(A, l, m, r)
        return A

    def MergeSortIter(self, A):
        L = 0
        R = len(A) - 1
        i = 1
        while(i<len(A)):
        # for i in range(l+1, r+2):
            c = i
            i *= 2
            j=L
            while(j<R):
            # for j in range(l, r+1):
                l = j
                m = min(R, j+c-1)
                r = min(R, j+(2*c)-1)
                # print(c, l, m, r)
                # self.MergeSentinal(A, l, m, r)
                self.MergeOriginal(A, l, m, r)
                # print(A)
                j += (c*2)
        return A
    
    def MergeSentinal(self, A, l, m, r):
        B = list()
        C = list()
        for i in range(l, m+1):
            B.append(A[i])
        for i in range(m+1, r+1):
            C.append(A[i])
        B.append(100000000000)
        C.append(100000000000)
        p1=p2=0
        for i in range(l, r+1):
            if B[p1]<C[p2]:
                A[i] = B[p1]
                p1 += 1
            else:
                A[i] = C[p2]
                p2 += 1
        return A

    def MergeOriginal(self, A, l, m, r):
        B = list()
        C = list()
        for i in range(l, m+1):
            B.append(A[i])
        for i in range(m+1, r+1):
            C.append(A[i])
        p1 = len(B)
        p2 = len(C)
        i = r
        while(p1 and p2):
            if B[p1 -1]>C[p2 - 1]:
                A[i] = B[p1 - 1]
                p1 -= 1
            else:
                A[i] = C[p2 - 1]
                p2 -= 1
            i -= 1
        
        if p1:
            while(p1):
                A[i] = B[p1 - 1]
                i -= 1
                p1 -= 1
        if p2:
            while(p2):
                A[i] = C[p2 - 1]
                i -= 1
                p2 -= 1
    
    def swap(self, A, p1, p2):
        t = A[p1]
        A[p1] = A[p2]
        A[p2] = t
    
    def BinarySearch(self, A, L, R, val):

        if L <= R:
            m = ((L+R)/2)
            if A[m] > val:
                return self.BinarySearch(A, L, m-1, val)
            elif A[m] < val:
                return self.BinarySearch(A, m+1, R, val)
            else:
                return True
        return False


if __name__ == '__main__':

    obj = Sort()

    ri = raw_input("Enter list items to be sorted\n").strip()
    A = ri.split(" ")
    A = list(map(int, A))
    # A = obj.ListInsertionSort(A)
    # A = obj.SelectionSort(A)
    # A = obj.MergeSortRec(A, 0, len(A)-1)
    # A = obj.MergeSortIter(A)
    A = obj.BinarySearch(A, 0, len(A)-1, 30)

    print(A)

