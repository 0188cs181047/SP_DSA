# In Python, Monkey Patching refers to dynamically modifying or extending behavior of a class or module at runtime. 
# This allows developers to change how functions, methods or classes behave without altering original source code.

class Monkey:
    def data(self):
        print("data() is being called ")

def monkey_f(self):
    print("monkey_f() is being called")


obj = Monkey()
obj.data = monkey_f

obj.data(obj)


