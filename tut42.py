marks = [12,56,78,98,45,67,88,90]
# index = 0
# for mark in marks:
#     print(mark)
#     if(index==2):
#         print("Harry, awesome!")
#     index += 1

for index, mark in enumerate(marks, start = 1):
    print(index, mark)
    if(index==2):
        print("Harry, awesome!")
    
