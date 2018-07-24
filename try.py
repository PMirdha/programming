import math
from collections import OrderedDict

class HeightArrange(object):
    """
    st - Segment Tree implementd as array:type of list
    cr - Current Range which we are looking at:type of list with two elements L & R
    lcr - Left child range of current range
    rcr - Right child range of current range
    x - index to find in array
    """

    def get_palce(self, st, x, cr, index):
        if cr[0] == cr[1]:
            st[index] -= 1
            return cr[0]
        
        lcr, rcr = self.getChildRange(cr)

        if st[(2*index) + 1] >= x:
            val = self.get_palce(st, x, lcr, (2*index) + 1)
        else:
            x -= st[(2*index) + 1]
            val = self.get_palce(st, x, rcr, (2*index) + 2)
        
        st[index] -= 1
        return val
    
    def getChildRange(self, r):
        mid = (r[0] + r[1]) / 2
        lcr = list()
        rcr = list()
        lcr.append(r[0])
        lcr.append(mid)
        rcr.append(mid+1)
        rcr.append(r[1])
        return lcr, rcr

    def populate_st(self, st, cr, index):
        if cr[0] == cr[1]:
            st[index] = 1
            return
        
        lcr, rcr = self.getChildRange(cr)

        self.populate_st(st, lcr, (2*index) + 1)
        self.populate_st(st, rcr, (2*index) + 2)

        st[index] = st[(2*index) + 1] + st[(2*index) + 2]

        return
    
    def solve(self, height, infront):
        n = len(height)
        ans = [0] * n
        ceil_height = math.ceil(math.log(n, 2))
        st_length = int(math.pow(2, ceil_height + 1) - 1)
        # print(st_length)
        st = [0] * st_length
        cr = [0, n - 1 ]
        index = 0
        self.populate_st(st, cr, index)
        temp_list = list()
        i = 0
        for x in height:
            temp_list.append((x, infront[i]))
            i += 1
        temp_list = sorted(temp_list, key=lambda x: x[0])
        for k, v in temp_list:
            # print(st)
            x = self.get_palce(st, v + 1, cr, 0)
            # print(x)
            ans[x] = k

        return ans

if __name__ == '__main__':
    ri = raw_input().strip()
    A = ri.split(" ")
    height = list(map(int, A))

    ri = raw_input().strip()
    B = ri.split(" ")
    infront = list(map(int, B))
    obj = HeightArrange()
    arrangement = obj.solve(height, infront)
    print(arrangement)



