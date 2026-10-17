# In Python, Monkey Patching refers to dynamically modifying or extending behavior of a class or module at runtime. 
# This allows developers to change how functions, methods or classes behave without altering original source code.


from types import MethodType

class Monkey:
    pass

def monkey_f(self):
    print("monkey_f() is being called")

def add(self, a, b):
    return a+b

obj = Monkey()
obj.check = MethodType(monkey_f, obj)
obj.addition = MethodType(add, obj)

obj.check()
print(obj.addition(12, 12))

