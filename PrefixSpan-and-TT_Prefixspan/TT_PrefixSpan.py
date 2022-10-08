from collections import defaultdict
# import numpy as np
# import pandas as pd
# tti= pd.read_excel("TTI.xlsx",index_col=[0])
# tti =np.array(tti)

# db= [
#     [3, 3, 3, 4, 3, 4, 4, 4, 4, 4, 3, 1, 1,1, 1, 2, 1, 2, 2, 2, 2, 3, 1, 2],
#     [3, 3, 4, 4, 3, 3, 4, 4, 4, 4, 3, 1, 1,1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3],
#     [3, 3, 4, 4, 3, 3, 4, 4, 4, 4, 3, 2, 3,1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
#     [3, 3, 4, 4, 3, 3, 4, 4, 4, 4, 3, 1, 1,1, 1, 2, 1, 2, 2, 2, 2, 3, 1, 2],
#     [3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 3, 3, 1,1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2],
#     ]
db = [
    [0, 1, 2, 3, 4],
    [1, 1, 1, 3, 4],
    [2, 1, 2, 2, 0],
    [1, 1, 1, 2, 2],
]

minsup = 2

results = []

def mine_rec(patt, mdb):
    def localOccurs(mdb):
        occurs = defaultdict(list)
        for (i, stoppos) in mdb:
            for k in range(0,len(db)):
                m=0
                #condition for TT PrefixSpan
                if(db[k][m]<db[k][m+1] and db[k][m+1]<db[k][m+2] and db[k][m+2]<db[k][m+3]):
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
print("RESULTS")
print(len(results))






