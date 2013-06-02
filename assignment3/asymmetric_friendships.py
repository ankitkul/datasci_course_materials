import MapReduce
import sys

"""
Asymmetric Frienships
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    record.sort()
    key = (record[0],record[1])
    mr.emit_intermediate(key,1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    for v in list_of_values:
      total += v
    if total == 1:
        mr.emit(key)
        mr.emit(key[::-1])      
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
