
class SegmentTree(object):
    """
    Note - Algo is for querying sum over interval: Some conditions might change while 
            storing Min, Max, etc... for a range
    st - Segment Tree implementd as array:type of list
    rr - Required Range which we are looking to query for
    A - Array which contains original element
    cr - Current Range which we are looking at:type of list with two elements L & R
    lcr - Left child range of current range
    rcr - Right child range of current range
    x(Update) - value by which st nodes need to be updated
    """

    def build_st(self, A, st, cr, index):
        if cr[0] == cr[1]:
            st[index] = A[cr[0]]
            return st[index]
        
        lcr, rcr = self.getChildRange(cr)
        
        # Below Code will change accordingly
        sum = 0
        sum += self.build_st(A, st, lcr, (2*index) + 1)
        sum += self.build_st(A, st, rcr, (2*index) + 2)

        st[index] = sum
        return st[index]
    
    def query(self, st, cr, rr, index):

        pass
    
    def update(self, st, cr, rr, x, index):
        pass
    
    def query_lazy(self, la, st, cr, rr, index):
        pass
    
    def update_lazy(self, la, st, cr, rr, x, index):
        pass

    def getChildRange(self, r):
        mid = (r[0] + r[1]) / 2
        lcr = list()
        rcr = list()
        lcr.append(r[0])
        lcr.append(mid)
        rcr.append(mid+1)
        rcr.append(r[1])
        return lcr, rcr

