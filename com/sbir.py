
l = [3, 5, 7, 8, 2]
def get_indexes_max_value(l):
  max_value = max(l)
  if l.count(max_value) > 1:
        return [i for i, x in enumerate(l) if x == max(l)]
  else:
        return l.index(max(l))

print(get_indexes_max_value(l))




