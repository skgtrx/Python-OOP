''' In this section we'll see how overriding affects the multiple inheritence : Dimond Shape Problem '''

'''
Diamond :
1--            A (Parent)
             /   \
2--       (A)B    C(A)
             \   /
3--            D(B,C)
'''

class A:
    def method(self):
        print("This method belongs to class A")

class B(A):
    def method(self):
        print("This method belongs to class B")

class C(A):
    def method(self):
        print("This method belongs to class C")

class D(B,C):
    def method(self):
        print("This method belongs to class D")
        super().method() # It'll print method belongs to class B as B is first in the order.
                         # If we'll change the order to (C,B) then It'll print C.


d = D()
d.method() # Result is "This method belongs to class D"

# Now point is the it creates a lot how confusion about how to class which method
# That's why we stay away from multiple inheritence.

print("-------------USE OF SUPER-------------")
class A:
    def method(self):
        print("This method belongs to class A")

class B(A):
    def method(self):
        print("This method belongs to class B")
        super().method() # It'll call C as C is at the same level. 

class C(A):
    def method(self):
        print("This method belongs to class C")
        super().method() # It'll call A 

class D(B,C):
    def method(self):
        print("This method belongs to class D")
        super().method() # This will call B as B is first in the order.

# bY the help of super() we'll gonna print all the methods
d1 = D()
d1.method()