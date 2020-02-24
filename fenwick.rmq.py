
N = 6000
m   = [0 for _ in range(N)]
mt  = [0 for _ in range(N)]


def add_range_arr(r, val):
    if r < 0:
        return None
        
    i = r
    while i >= 0:
        mt[i] += val
        i = (i & (i + 1)) - 1
        
    i = r | (r + 1)
    while i < N:
        m[i] += val * (r-(i&(i+1)) + 1)
        i = i | (i + 1)
        

def add_range(l, r, val):
    add_range_arr(r, val)
    add_range_arr(l-1, -val)
    
    
def get_sum(r):
    if r < 0:
        return 0
        
    res = 0
    
    i=r
    while i >=0:
        res += m[i] + mt[i]*(i-(i&(i+1))+1)
        i = (i & (i + 1)) -1
    
    i = r | (r+1)
    while i < N:
        res += mt[i]*(r-(i&(i+1))+1)
        i = i | (i + 1)
        
    return res
    
    
def get_sum_range(l,r):
    return get_sum(r) - get_sum(l-1)
    
    
import time

start = time.time()
sum_ = 0
for i in range(3000):
    for j in range(3000):
        add_range(j,3000,1)
        #add_range(2,6,1)
        #add_range(3,4,1)
    for j in range(3000):
        sum_ += get_sum_range(j,j)

print (time.time()-start)
print (sum_)
#print (get_sum_range(3,3))
#print (get_sum_range(2,2))
#print (get_sum_range(1,1))