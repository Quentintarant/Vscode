class A:
    x=10
    y=20
    def Add(self):
        print(self.x + self.y)
class B(A):
    def sub(self):
        print(self.x - self.y)
class C(B):
    def mul(self):
        print(self.x * self.y)
obj = C()
obj.Add()
obj.sub()
obj.mul()