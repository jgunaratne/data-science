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
  sequence_id = record[0]
  nucleotides = record[1]
  mr.emit_intermediate(nucleotides[:-10], sequence_id)

def reducer(nucleotides, sequence_id):
  mr.emit(nucleotides)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
