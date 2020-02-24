class FenwickRange:
    N   = 0
    m   = []
    mt  = []
    
    def __init__(self, N):
        self.N  = N
        self.m  = [0 for _ in range(N)]
        self.mt = [0 for _ in range(N)]

    def add_range_arr(self, r, val):
        if r < 0:
            return None
            
        i = r
        while i >= 0:
            self.mt[i] += val
            i = (i & (i + 1)) - 1
            
        i = r | (r + 1)
        while i < self.N:
            self.m[i] += val * (r-(i&(i+1)) + 1)
            i = i | (i + 1)
            

    def add_range(self, l, r, val):
        self.add_range_arr(r, val)
        self.add_range_arr(l-1, -val)
        
        
    def get_sum(self, r):
        if r < 0:
            return 0
            
        res = 0
        
        i=r
        while i >=0:
            res += self.m[i] + self.mt[i]*(i-(i&(i+1))+1)
            i = (i & (i + 1)) -1
        
        i = r | (r+1)
        while i < self.N:
            res += self.mt[i]*(r-(i&(i+1))+1)
            i = i | (i + 1)
            
        return res
        
        
    def get_sum_range(self, l,r):
        return self.get_sum(r) - self.get_sum(l-1)
        
'''        
import time

start = time.time()
sum_ = 0

BITTree = FenwickRange(6000)
for i in xrange(1, 2999):
    for j in xrange(1,5999):
        BITTree.add_range(j,j,1)
    for j in xrange(1,5999):
        sum_ += BITTree.get_sum_range(j,j)

print (time.time()-start)
print (sum_)
#print (get_sum_range(3,3))
#print (get_sum_range(2,2))
#print (get_sum_range(1,1))
'''
