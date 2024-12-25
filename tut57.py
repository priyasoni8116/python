class Person:
    name = "Harry"
    occupation = "Software Developer"
    def info(self):
        print(f"{self.name} is a{self.occupation} ")

a = Person()
# a.name = "Vikrant"
a.info()