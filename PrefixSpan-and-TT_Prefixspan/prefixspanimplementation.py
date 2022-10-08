from collections import defaultdict
import numpy as np

db_orig = np.array([
    [ 4, 3, 2, 2],
    [ 3, 3, 2, 1],
    [ 4, 4, 2, 2],
    [ 4, 3, 2, 2],
    [ 3, 3, 2, 1],
    [ 4, 4, 2, 2],
    [ 4, 3, 2, 2],
    [ 3, 3, 2, 1],
    [ 4, 4, 2, 2],
    [ 4, 3, 2, 2],
    [ 3, 3, 2, 1],
    [ 4, 4, 2, 2],
    [ 4, 3, 2, 2],
    [ 3, 3, 2, 1],
    [ 4, 4, 2, 2],
    [ 4, 3, 2, 2],
    [ 3, 3, 2, 1],
    [ 4, 4, 2, 2],
    [ 4, 3, 2, 2],
    [ 3, 3, 2, 1],
    [ 4, 4, 2, 2],
])
db = db_orig.T
print(db)

minsup = 1

results = []

def mine_rec(patt, mdb):
    def localOccurs(mdb):
        occurs = defaultdict(list)

        for (i, stoppos) in mdb:
            seq = db[i]
            for j in range(stoppos, len(seq)):
                l = occurs[seq[j]]
                if len(l) == 0 or l[-1][0] != i:
                    l.append((i, j + 1))

        return occurs

    for (c, newmdb) in localOccurs(mdb).items():
        newsup = len(newmdb)

        if newsup >= minsup:
            newpatt = patt + [c]

            results.append((newpatt, [i for (i, stoppos) in newmdb]))
            mine_rec(newpatt, newmdb)

mine_rec([], [(i, 0) for i in range(len(db))])

print(results)
l = len(results)
b = results[0][1]
print(len(b))

k=[0] * 24
for i in range(0,l,1):
    a = results[i][1]
    for j in range(0,len(a)):
        print(j)
        if(a[j]==0):
            k[a[j]]=k[a[j]]+1
            # print(k)
        if(a[j]==1):
            k[a[j]]=k[a[j]]+1
        if(a[j]==2):
            k[a[j]]=k[a[j]]+1
print("Time       Number of patterns")
print("12:00-1:00       "+str(k[0]))
print("1:00-2:00        "+str(k[1]))
print("2:00-3:00        "+str(k[2]))

# print(i)