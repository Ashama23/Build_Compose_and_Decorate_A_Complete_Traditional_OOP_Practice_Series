class A:
    def show(self):
        print("This is the show() method from class A")

class B(A):
    def show(self):
        print("This is the show() method from class B")

class C(A):
    def show(self):
        print("This is the show() method from class C")

class D(B, C):
    pass

d_object = D()
print("Calling show() on an object of class D:")
d_object.show()

print("\n--------------------------------------------")
print("The Method Resolution Order (MRO) for class D is:")
print(D.mro())