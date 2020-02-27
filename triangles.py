import time
from fenwick_rmq import FenwickRange
from math import ceil

start = time.time()

s = 0
a = [[0 for _ in range(6000)] for _ in range(3000)]
b = [[0 for _ in range(6000)] for _ in range(3000)]
c = [[0 for _ in range(6000)] for _ in range(3000)]


r, cl = map(float, raw_input().split(' '))

x = 3000

i=1
while (i-1) < r * 2-1:
    row = raw_input()
    if (i-1) % 2 == 0 and (i-1) % 4 != 0:
        row = row[2:]
    
    if (i-1) % 2 == 0:
        cum = 0
        m = 0
        ri = (i-1) / 2
        
        while m < (len(row)-1) / 4:
            if row[m * 4 + 1] == '-':
                cum +=1
            else:
                cum = 0
            m +=1
            a[ri][m + x] = cum
        if cum > 0 and m==(len(row)-1) / 4:
            a[ri][m + x] = cum
    else:
        m = 0
        rs = 0 # right slash
        rl = 0 # left slash
        md = ri % 2
        while m < (len(row) / 2):
            if row[m*2+1] == "\\":
                b[ri + 1][rs + x] = b[ri][rs + x] + 1
                
            if row[m*2+1] == "/":
                c[ri + 1][x + rl] = c[ri][rl + x + 1] + 1
            
            if (md != 0 and m % 2 == 0) or (md == 0 and (m - 1) % 2 == 0):
                rs +=1
                
            if (md != 0 and m % 2 == 0) or (md == 0 and (m - 1) % 2 == 0):
                rl +=1
                
            m += 1

    #print ("i:%s, x:%s, ri:%s - %s" % (i, x, ri, row)) 
    
    
    if i == 1:
        cl = m
    
    i += 1
    # do shift
    if i % 4 == 0 and i != r * 2-1:
        x -=1

print (a[0][2999:3003])
print (a[1][2999:3003])
print (a[2][2999:3003])
#print (a[3][2999:3003])
#print (a[4][2999:3002])

print 
print (b[0][2999:3003])
print (b[1][2999:3003])
print (b[2][2999:3003])
#print (b[2][2999:3002])
#print (b[3][2999:3002])
#print (b[4][2999:3002])

print 
print (c[0][2999:3003])
print (c[1][2999:3003])
print (c[2][2999:3003])
#print (c[3][2999:3002])
#print (c[4][2999:3002])

print (x + int(r) + 1)
#quit()



BITTree = FenwickRange(6000)
'''
if A[1] == 0:
    BITTree.add_range(1,4, 1)
    A[1] = 1
    
if A[1] == 0:
    BITTree.add_range(1,7, 1)
    A[1] = 1


if A[2] == 0:
    BITTree.add_range(2,5, 1)
''' 
#BITTree.add_range(1,2, 1)
#BITTree.add_range(3,3, 1)
#BITTree.add_range(4,5, 1)

#print (BITTree.get_sum_range(1,1))


t = 0
cl2 = (3000 + cl) - x
#print (cl2)
L = int(min(r,cl))
print ("General:", x, cl2, L,int(r)-1)
s = 0
for i in xrange(int(r)):
    BITTree = FenwickRange(6000)
    A = [0 for _ in range(6000)]
    #print 
    for j in xrange(cl2, -1, -1):
        h = min(b[i][j + x], a[i][j + x])
        #print (j, a[i][j + x], b[i][j + x], h, x-j, c[i][j + x - h])
        #print (j, a[i][j + x],b[i][j + x])
        if  c[i][j + x - h] >= h and h > 0 and A[j-h] == 0 and a[i][j+x] >= b[i][j + x]:
            #print (i, "Triangle", j-h+1, j)
            BITTree.add_range(j-h+1, j, 1)
            A[j-h] = 1
        
            
    #print ('A:',A[0:cl2+1])
    #print ('-----------------')
    for j in xrange(cl2 + 1):
        if b[i][j + x] > 0:
            #print ('j:%s, Sum:%s' % (j,BITTree.get_sum_range(j,j)))
            s += BITTree.get_sum_range(j,j)
       
    #print ("Sum:%s" % s)
print (BITTree.get_sum_range(1,1))


#print (s)
print ("Triangles: %s, execution: %s" % (s, time.time()-start))
