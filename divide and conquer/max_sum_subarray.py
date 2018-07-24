

class MaxSumSubarrayClass(object):

    def MSSRec(self, A, l, r):
        if l == r:
            return A[l], l, r
        
        m = (l+r)/2
        left_list = self.MSSRec(A, l, m)
        right_list = self.MSSRec(A, m+1, r)
        mid_list = self.CrossSum(A, l, r)

        temp = self.MaxSumList(left_list, right_list, mid_list)
        return temp
    
    def CrossSum(self, A, l, r):
        m = (l+r)/2
        curr_sum = 0
        mls = -999999999
        mlindex = l
        for i in xrange(m, l-1, -1):
            curr_sum += A[i]
            if mls < curr_sum:
                mls = curr_sum
                mlindex = i
        curr_sum = 0
        mrs = -999999999
        mrindex = r
        for j in xrange(m+1, r+1):
            curr_sum += A[j]
            if mrs < curr_sum:
                mrs = curr_sum
                mrindex = j
        
        return (mls+mrs), mlindex, mrindex

    
    def MaxSumList(self, l, r, m):
        ans_list = l
        temp = list()
        # temp = l if l[0]>r[0] else r
        if l[0] >= r[0] and l[0] >= m[0]:
            ans_list = l
        
        if r[0] >= l[0] and r[0] >= m[0]:
            ans_list = r
        
        if m[0] >= r[0] and m[0] >= l[0]:
            ans_list = m
        
        # if not ans_list and ans_list[0]<temp[0]:
        #     ans_list = temp
        
        # temp = l if l[0]>m[0] else m
        # if not ans_list and ans_list[0]<temp[0]:
        #     ans_list = temp
        
        # temp = m if m[0]>r[0] else r
        # if not ans_list and ans_list[0]<temp[0]:
        #     ans_list = temp
        
        return ans_list

if __name__ == '__main__':
    
    obj = MaxSumSubarrayClass()

    ri = raw_input("Enter list items to be sorted\n").strip()
    A = ri.split(" ")
    A = list(map(int, A))
    x = obj.MSSRec(A, 0, len(A)-1)

    print(x)
        