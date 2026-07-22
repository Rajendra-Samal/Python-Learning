s = {1, 2, 3}
s.add(4)          # {1, 2, 3, 4}
s.remove(2)       # raises KeyError if 2 not present
s.discard(2)      # no error if 2 not present
s.pop()           # removes and returns an arbitrary element
s.clear()         # empties the set

