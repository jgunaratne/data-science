import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    li_order = record[0]
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(key, records):
    order = None
    orders = []
    for r in records:
      if r[0] == 'order':
        order = r
      else:
        line_item = r
        joined_order = order + line_item
        orders.append(joined_order)
    
    for o in orders:
      mr.emit(o)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
