class A:
    x=10
    y=20
    def Add(self):
        print(self.x + self.y)
class B(A):
    def sub(self):
         print(self.x - self.y)
obj = B()
obj.Add()
obj.sub()