import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
  friends = []
  personA = record[0]
  personB = record[1]
    
  scores=[personA, personB]
  sortedScores = (sorted(scores))
  tupleKey = (sortedScores[0], sortedScores[1])
  
  mr.emit_intermediate(tupleKey, record)

def reducer(personA, records):
  if (len(records)==1):
    mr.emit(personA)
    mr.emit((personA[1],personA[0]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
