# double = lambda x: x*2
cube = lambda x: x*x*x
# avg = lambda x,y: (x+y)/2

# print(double(2))
# print(cube(2))
# print(avg(3,5))

def appl(fx, value):
    return 6 + fx(value)

print(appl(cube, 2))