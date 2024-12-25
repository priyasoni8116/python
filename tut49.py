# READING A FILE
# f = open('myfile.txt', 'r')
# text = f.read()
# print(text)
# f.close()

# WRITING A FILE
f = open('myfile.txt', 'w')
f.write('hello world')


with open('myfile.txt','a'):
   f.write("i am inside with")

