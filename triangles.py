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
'''
BITTree = FenwickRange(6000)
BITTree.add_range(2,2, 1)
BITTree.add_range(3,3, 1)
#BITTree.add_range(4,5, 1)

print (BITTree.get_sum_range(2,2))
quit()
'''
t = 0
cl2 = (3000 + cl) - x
#print (cl2)
L = int(min(r,cl))
print ("General:", x, L,int(r)-1)
s = 0
for i in xrange(int(r)):
    BITTree = FenwickRange(6000)
    for j in xrange(cl2 + 1):
        h = min(b[i][j + x], j)
        print (j, a[i][j + x], b[i][j + x], h, c[i][j + x - h])
        if  c[i][j + x - h] >= h and h>0:
            print ("Triangle", j-h+1, j)
            BITTree.add_range(j-h+1, j, 1)
        #print (x + j, i, a[i][x + j], b[i][j + x], l, c[i][j + x - l])
        #if c[i][j + x - ] >= b[i][j + x] and l>0:
        #   BITTree.add_range(j+1, j + l, 1)
        #h = min(b[i][j + x], j)
        #if c[i][j + x - cl2] >= h:
        #    BITTree.add_range(j+1, h, 1)
        #    print('triangle:', j+1, h)
        #print (a[i][x + j], x + j)
        #if a[i][j] > 0 and b[i][j] > 0:
        #BITTree.add_range(j, j + c[i][j + x], 1)
    # if i == 1:
        # print (1,1,BITTree.get_sum_range(1,1))
        # print (2,2,BITTree.get_sum_range(2,2))
        # print (3,3,BITTree.get_sum_range(3,3))
        # quit()
    for j in xrange(cl2 + 1):
        s += BITTree.get_sum_range(j,j)
        
       
    #print ("Sum:%s" % s)
print (BITTree.get_sum_range(1,1))
print (BITTree.get_sum_range(2,2))
#print (s)

# calculate height triangles
'''

Nlog3
for l in range(1,L+1):
    i = 0
    #print (l,ceil((r-1) / l) )
    while i <= r - l - 1:
        j = 0
        #print (l, i)
        #if l == 2:
        #    print(i)
        while j <= cl2 -l-1:
            #print ("\t%s" % j)
            #print ("count")
            #if l == 2:
            #    print (i, j, x, l)
            if a[i][int(j + x + l)] - a[i][int(j + x)] >=l and b[i+l][j+x] - b[i][j + x] >= l and c[i+l][j + x] - c[i][j +x +l]>=l:
                #print (l,"found", "top -> bottom")
                s +=1
            #if l == 2:
            #    print ("\t%s => x:%s, r:%s, a1:%s va2:%s, va1:%s, vb2:%s, vb1:%s, vc2:%s, vc1:%s" % (j, x, i + l, j + x, a[i + l][j + l +x], a[i + l][j + x], b[i+l][j+ x + l],b[i][j+ x + l], c[i+l][x+j],c[i][x + j +l]))
            # bottom -> top
            if a[i+l][int(j+x+l)] - a[i+l][int(j+x)]>=l and b[i+l][j+ x + l] - b[i][j + x + l] >= l and c[i+l][x+j] - c[i][x + j +l] >=l:
                #print (l,"found", "bottom -> top")
                s +=1

            
            j +=1
        i +=1
    

    t = s
'''
        # A[i] == 0 
        # activiruem tochku = 1 
        # if D > bezhim po tochkam i zapolnjaem 1 
        
        # A[i] == 0 i mi prodolzhaem schitatj annuliruem

#print (s)
print ("Triangles: %s, execution: %s" % (s, time.time()-start))
