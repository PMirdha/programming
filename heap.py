from collections import defaultdict


class Heap(object):
    
    def HeapSort(self, A, ASC=True):
        if ASC:
            self.BuildMaxHeapMethod1(A)
            self.MaxHeapSort(A)
        else:
            self.BuildMinHeapMethod1(A)
            self.MinHeapSort(A)
        return A
    
    def BuildMaxHeapMethod1(self, A):
        for index in xrange(len(A)>>1, -1, -1):
            A = self.MaxPercolateDown(A, index, len(A))
        return A
    
    def BuildMinHeapMethod1(self, A):
        for index in xrange(len(A)>>1, -1, -1):
            A = self.MinPercolateDown(A, index, len(A))
        return A

    def BuildMaxHeapMethod2(self, A):
        for index in xrange(1, len(A)):
            A = self.MaxHeapifyUp(A, index)
        return A
    
    def BuildMinHeapMethod2(self, A):
        for index in xrange(1, len(A)):
            A = self.MinHeapifyUp(A, index)
        return A
    
    def MaxHeapSort(self, A):
        for i in xrange(len(A)-1, -1, -1):
            self.swap(A, 0, i)
            self.MaxPercolateDown(A, 0, i)
        return A
    
    def MinHeapSort(self, A):
        for i in xrange(len(A)-1, -1, -1):
            self.swap(A, 0, i)
            self.MinPercolateDown(A, 0, i)
        return A
    
    def MaxHeapifyUp(self, A, index):
        p = self.Parent(index)
        while index > 0 and A[p]<A[index]:
            self.swap(A, p, index)
            index = p
            p = self.Parent(p)
        return A
    
    def MinHeapifyUp(self, A, index):
        p = self.Parent(index)
        while index > 0 and A[p]>A[index]:
            self.swap(A, index, p)
            index = p
            p = self.Parent(p)
        return A

    def MaxPercolateDown(self, A, i, n):
        lc = self.Left(i)
        rc = self.Right(i)
        li = self.Largest(A, i, lc, rc, n)
        while li!=i:
            A = self.swap(A, i, li)
            i = li
            lc = self.Left(i)
            rc = self.Right(i)
            li = self.Largest(A, i, lc, rc, n)
        return A
    
    def MinPercolateDown(self, A, i, n):
        lc = self.Left(i)
        rc = self.Right(i)
        si = self.Smallest(A, i, lc, rc, n)
        while si!=i:
            A = self.swap(A, i, si)
            i = si
            lc = self.Left(i)
            rc = self.Right(i)
            si = self.Smallest(A, i, lc, rc, n)
        return A
    
    def Left(self, i):
        return (((i + 1) << 1) - 1)
    
    def Right(self, i):
        return ((i + 1) << 1)
    
    def Parent(self, i):
        return (((i + 1) >> 1) - 1)
    
    def Largest(self, A, i, x, y, n):
        largest = x if x < n and A[i] < A[x] else i
        largest = y if y < n and A[largest] < A[y] else largest
        return largest
    
    def Smallest(self, A, i, x, y, n):
        smallest = x if x < n and A[i] > A[x] else i
        smallest = y if y < n and A[smallest] > A[y] else smallest
        return smallest
    
    def swap(self, A, i, j):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
        return A

class DataObj(object):
    data = None
    q_index = None

    def __init__(self, data, index):
        self.data = data
        self.q_index = index

class PqObj(object):
    q_key = None
    d_index = None

    def __init__(self, q_key, index):
        self.q_key = q_key
        self.d_index = index

class MaxPriorityQueue(object):
    pQueue = list()
    dList = list()

    def PqInsert(self, data, key):
        d_index = len(self.dList)
        q_index = self.qNum
        dobj = DataObj(data, q_index)
        pqobj = PqObj(key, d_index)
        self.dList.append(dobj)
        self.pQueue.append(pqobj)
        self.PqMaxHeapifyUp(q_index)
    
    def PqMax(self):
        if self.qNum:
            return self.pQueue[0]
        else:
            return None
    
    def PqExtractMax(self):
        if not self.dList:
            return None
        dobj = self.dList[self.pQueue[0].d_index]
        qobj = self.pQueue[self.qNum - 1].pop()
        if self.pQueue:
            self.pQueue[0] = qobj
            self.PqMaxHeapifyDown(0)
        return dobj.data
    
    def PqIncreaseProirity(self, index, val):
        temp_obj = None
        for obj in self.dList:
            if obj.data == data:
                temp_obj = obj
                break
        
        pass
        

if __name__ == '__main__':
    obj = Heap()

    ri = raw_input("Enter list items to be sorted\n").strip()
    A = ri.split(" ")
    A = list(map(int, A))
    A = obj.HeapSort(A)

    print(A)




class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        ans = min(A)
        for i in range(2, B + 1):
            tmax = None
            count = 0
            for i in range(0, len(A)):
                if A[i]>ans:
                    if tmax is None or tmax > A[i]:
                        tmax = A[i]
                        count = 1
                    elif tmax == A[i]:
                        count += 1
                i -= (count - 1)
            ans = tmax
print(ans)
        return ans
