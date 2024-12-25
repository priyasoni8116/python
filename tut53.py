# MAP
l = [1,2,3,4]
# newl = list(map(lambda x: x*x*x, l))
# print(newl)

# FILTER
newnewl = list(filter(lambda a: a<4, l))
print(newnewl)

# REDUCE
from functools import reduce 
sum = reduce(lambda x,y: x+y, l)
print(sum)