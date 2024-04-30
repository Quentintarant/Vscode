class ClassA:
    def method_A(self):
        print("Method A from ClassA")

class ClassB:
    def method_B(self):
        print("Method B from ClassB")

class ClassC(ClassA, ClassB):
    def method_C(self):
        print("Method C from ClassC")
obj_C = ClassC()
obj_C.method_A()
obj_C.method_B()
obj_C.method_C()