# a = input("Enter the number")
# print(f"multipilcation the table of {a} is: ")
# try:
#   for i in range(1,11):
#     print(f"{int(a)} x {i} = {int(a)*i}")
# except:
#     print("invalid input!")

# print("Some imp lines of code")
# print("End of program")

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")

try:
    num = int(input("Enter an integer: "))
    a = [6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")

except IndexError:
    print("IndexError")