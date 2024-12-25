# if-else:
# a = int(input("Enter your age: ")) 
# print("Your age is: ",a)

# if(a>18):
#     print("You can drive")
# else:
#     print("You cannot drive")

#  elif-else:
# num = int(input("Enter the value of num: "))
# if(num < 0):
#     print("num is negative")
# elif(num == 0):
#     print("num is zero")
# else:
#     print("num is positive")

# nested-if
num = int(input("Enter the value of num: "))
if(num<0):
   print("num is negative")
elif(num>0):
   if(num <= 10):
      print("num is between 1-10") 
   elif(num > 10 and num <= 20):
        print("num is between 11-20")
   else:
        print("num is greater than 20")    
else:
    print("num is zero")       

