# tuples are unchangeable 
tup = (1,2,3,8,9)
print(type(tup), tup)
print(tup[0])

if 2 in tup:
    print("yes 2 is present")
tup2 = tup[1:4]
print(tup2)
