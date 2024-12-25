# def factorial(n):
#   if(n==0 or n==1):
#     return 1
#   else:
#     return n * factorial(n-1)

# print(factorial(5))

# Program of Fibonacci sequence
def f(n):
  if(n==0):
   return 0
  elif(n==1):
    return 1
  else:
    return f(n-1) + f(n-2)

print(f(7))