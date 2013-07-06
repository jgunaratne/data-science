import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
  mtx = record[0]
  i = record[1]
  j = record[2]
  val = record[3]
  
  for k in range(0,5):
    if mtx == 'a':
      key = (i, k)
      mr.emit_intermediate(key, (mtx,j,val))
    if mtx == 'b':
      key = (k, j)
      mr.emit_intermediate(key, (mtx,i,val))
  
def reducer(key, vals):
  mtx_dict = {}
  for n in vals:
    mtx = n[0]
    if mtx in mtx_dict:
      mtx_dict[mtx] = mtx_dict[mtx] + [(n[1], n[2])]
    else:
      mtx_dict[mtx] = [(n[1], n[2])]
      
  #for v in vals:
  #  print v, v[1]
  
  a = mtx_dict['a']
  b = mtx_dict['b']
  c = mtx_dict['a'] + mtx_dict['b']
  c = sorted(c)
  
  tupleDict = {}

  for n in c:
    i = n[0]
    if i in tupleDict:
      tupleDict[i] = tupleDict[i] + [n[1]]
    else:
      tupleDict[i] = [n[1]]
    
  sum = 0
  for elem in tupleDict:
    if len(tupleDict[elem]) == 2:
      sum = sum + (tupleDict[elem][0] * tupleDict[elem][1])

  mr.emit((key[0], key[1], sum))
  
  

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
