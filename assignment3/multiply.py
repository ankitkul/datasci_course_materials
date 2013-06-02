import MapReduce
import sys

"""
Matrix Multiplication
"""

mr = MapReduce.MapReduce()
# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    """
    if record[0] == 'a':   
        key = record[2] #jth for M
        value = [record[0],record[1],record[3]] #complete
    else:
        key = record[1] #jth for N
        value = [record[0],record[2],record[3]] #complete         
    mr.emit_intermediate(key, value)
    """
    for i in range(0,5):
        if record[0] == 'a':
            key = (record[1],i)
            value = record
        else:
            key = (i,record[2])
            value = record    
        mr.emit_intermediate(key,value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    """
    alist=[]
    blist=[]
    for v in list_of_values:
        if v[0] == 'a':
            alist.append(v)
        else:
            blist.append(v)    

    for a in alist:
        for b in blist:
            key = (a[1],b[1])
            value = a[2]*b[2]  
            mr.emit((key, value))   
    """
    alist={}
    blist={}
    for v in list_of_values:
        if v[0] == 'a':
            key1 = (v[1],v[2])
            alist[key1] = v[3]
        else:
            key1 = (v[1],v[2])
            blist[key1] = v[3] 

    total = 0     
    for j in range(0,5):
        if (key[0],j) in alist and (j,key[1]) in blist:
            total += alist[(key[0],j)] * blist[j,key[1]]        
    mr.emit((key[0],key[1], total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
 