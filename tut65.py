class Math:
    def __init__(self, num):
        self.num = num

    def addtonumber(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a,b):
        return a + b

result = math.add(1,2)
print(result)