# Python Interview Preparation

## 1. Explain 'Everything in Python is an object'.
What's an object? An object in a object-oriented programming language is an entity that contains data along with some methods for operations related to that data. <br>
Everything from numbers, lists, strings, functions and classes are python objects. 
```python
>>> a = 10.5
>>> a.is_integer() # Float type has is_integer() method cause a is an object of float class
False
>>> type(a)
<class 'float'>
>>> def func()
....    pass
>>> type(func)
<class 'function'>
>>> # like functions, classes are also objects of 'type' class
```
Look at the below example
```python
>>> var = 'Tom' # Object 'Tom' is created in memory and name 'var' is binded to it. 
>>> var = 'Harry' # Another object is created however note that name 'var' is now binded to 'Harry' but 'Tom' is still somewhere in memory and is unaffected.
```
Ref: [Nina Zakharenko - Memory Management in Python - The Basics - PyCon 2016](https://www.youtube.com/watch?v=F6u5rhUQ6dU)

## 2. What is mutable and immutable objects/data types in Python?
Mutation generally refers to 'change'. So when we say that an object is mutable or immutable we meant to say that the value of object can/cannot change. <br>
When an object is created in Python, it is assigned a type and an id. An object/data type is mutable if with the same id, the value of the object changes after the object is created. 
##
<b>Mutable objects in Python</b>
-- Objects that can change after creation. Lists, byte arrays, sets, and dictionaries.
```python
>>> list_var = [17, 10]
>>> list_var
[17, 10]
>>> id(list_var)
2289772854208
>>> list_var += [17]
>>> list_var
[17, 10, 17]
>>> id(list_var) # ID of the object didn't change.
2289772854208
```

## 
<b>Immutable objects in Python</b>
-- Numeric data types, strings, bytes, frozen sets, and tuples.
```python
>>> # Example of tuples
>>> tuple_var = (17,)
>>> tuple_var
(17,)
>>> id(tuple_var)
1753146091504
>>> tuple_var += (10,)
>>> tuple_var
(17,10)
>>> id(tuple_var) # ID changes when made changes in object.
1753153466880
```
##
<b>Mutable objects and functon arguments</b>
```python
def sample_func(sample_arg):
    sample_agr.append(10)
    # No need to return the obj since it is utilizing the same memory block

sample_list = [7, 8, 9]
sample_func(sample_list)
print(sample_list) # [7, 8, 9, 10]
```

## 3. What is the difference between list and tuples in Python?

| Parameter | List | Tuples |
| :-------------:|:-------------:| :-------------:| 
|  Syntax   | Square brackets or list keyword | Round brackets/parenthesis or tuple keyword |
| Nature    | Mutable  | Immutable |
| Item Assignment | Possible  | Not Possible |
| Reusablity | Copied  | Not Copied |
| Performance | Relatively slower  | Relatively faster |
| Memory | Large-Extra than the element size | Fixed to element size |

Note: It is not required for tuples to have parenthesis, one can also define tuple ```python a = 2, 3, 4 ```

### Memory Allocation of Tuple and List
Tuple does not allot any extra memory during construction because it will be immutable so does not have to worry about addition of elements. 
```python
>>> tuple_var = tuple()
>>> tuple_var.__sizeof__() # take 24 bytes for empty tuple
24
>>> tuple_var = (1,2) # additional 8 bytes for each integer element
>>> tuple_var.__sizeof__()
40
```
List over-allocates memory otherwise list.append would be an O(n) operation. 
```python
>>> list_var = list()
>>> list_var.__sizeof__() # take 40 bytes for empty list
40
>>> list_var.append(1)
>>> list_var.__sizeof__() # append operation allots extra memory size considering future appends
72
>>> list_var
[1]
>>> list_var.append(2)
>>> list_var.__sizeof__() # size remains same since list has space available
72
>>> list_var
[1,2]
```
### Reusablity
Tuple literally assigns the same object to the new variable while list basically copies all the elements of the existing list.
```python
>>> # List vs Tuples | Reused vs. Copied
>>> old_list = [1,2]
>>> old_list.append(3)
>>> old_list
[1, 2, 3]
>>> id(old_list) 
2594206915456
>>> old_list.__sizeof__()
88

>>> # Copying list
>>> new_list = list(old_list)
>>> new_list
[1, 2, 3]
>>> id(new_list) # new id so new list is created
2594207110976
>>> new_list.__sizeof__() # size is also not same as old_list
64

>>> Tuple Copy
>>> old_tuple = (1,2)
>>> id(old_tuple)
2594206778048
>>> old_tuple.__sizeof__()
40
>>> new_tuple = tuple(old_tuple)
>>> id(new_tuple) # same id as old_tuple
2594206778048
>>> new_tuple.__sizeof__() # also same size as old_tuple since it is refering to old_tuple
40
```

### Performance-Speed
Tuples and List takes almost same time in indexing, but for construction, tuple destroys list. See example, 'List vs Tuple'. 


## 4. How Is Memory Managed in Python?

Python manages memory automatically using a private heap, a memory manager, reference counting, and garbage collection. Developers generally do not need to allocate or release memory manually.

### 4.1 Python Memory Management Architecture

Python memory management involves the following components:

1. **Private Heap:** Stores Python objects and their data.
2. **Memory Manager:** Allocates and manages memory for Python objects.
3. **Reference Counting:** Tracks references to objects and allows objects with no remaining references to be deallocated.
4. **Garbage Collection:** Detects and reclaims unreachable objects involved in reference cycles.
5. **Memory Allocator:** Uses allocation strategies to manage memory efficiently and reuse memory where possible.

### 4.2 Reference Counting

Reference counting is one of the primary memory management mechanisms in CPython. Each object maintains a reference count that tracks references to it.

When an object's reference count reaches zero, the object can generally be deallocated immediately.

**Example:**

```python
a = [10, 20, 30]  # A list object is created
b = a              # b references the same list object

del a              # Removes the reference held by a
print(b)           # [10, 20, 30]

del b              # No references remain; the list can be deallocated
```

**Important points:**

- Multiple variables can reference the same object.
- The `del` statement removes a reference; it does not necessarily destroy the object.
- An object can remain alive as long as references to it exist.
- Reference counting alone cannot reclaim unreachable reference cycles.

### 4.3 Garbage Collection

Python's cyclic garbage collector detects unreachable objects that reference one another, allowing cycles to be reclaimed even when their reference counts are nonzero.

**Example:**

```python
import gc

class Node:
    pass

a = Node()
b = Node()

a.other = b
b.other = a  # Creates a reference cycle

del a
del b

gc.collect()  # Requests a garbage-collection cycle
```

In this example, the two objects reference each other. After the external references are deleted, the cycle becomes unreachable. The cyclic garbage collector can identify and reclaim it.

**Note:** `gc.collect()` requests garbage collection, but it does not guarantee that all memory will be returned to the operating system.

### 4.4 Private Heap and Memory Allocation

Python objects and their data are generally stored in a private heap managed by the Python runtime.

When an object is created, the memory manager allocates the required memory. When the object is no longer needed, that memory can be released or retained for reuse.

```python
numbers = [1, 2, 3, 4, 5]
```

Here, Python creates a list object and allocates memory for the list and its elements or references to them.

CPython uses specialized memory allocation mechanisms for many small objects. Consequently, deleting an object does not necessarily cause the process's memory usage to decrease immediately.

### 4.5 Stack vs. Heap Memory

| Stack | Heap |
|---|---|
| Associated with function execution frames and local execution state | Stores Python objects and their data |
| Function frames are unwound when functions return | Objects can outlive the function that created them if references remain |
| Managed by the Python execution runtime | Managed by the Python memory manager |

**Note:** This is a simplified description of CPython. Exact memory implementation details vary across Python implementations.

### 4.6 Best Practices for Memory Optimization

- **Use generators:** Process large datasets incrementally instead of loading everything into memory.
- **Release unnecessary references:** Avoid retaining large objects longer than necessary.
- **Use context managers:** Close files and database connections reliably with `with` statements.
- **Manage caches carefully:** Prevent caches and global variables from retaining unnecessary objects.
- **Profile memory usage:** Use tools such as `tracemalloc` to investigate Python memory allocations.
- **Understand garbage collection:** Use the `gc` module when diagnosing reference cycles rather than forcing collection without a specific reason.

**Example using a generator:**

```python
def generate_numbers(limit):
    for number in range(limit):
        yield number

for number in generate_numbers(1_000_000):
    pass
```

The generator produces values incrementally rather than creating and retaining a list containing all one million numbers.

### 4.7 Interview Summary

Python manages memory automatically through its memory manager and private heap. In CPython, reference counting allows objects with no remaining references to be deallocated, while the cyclic garbage collector handles unreachable reference cycles. Python also uses specialized allocation mechanisms and may reuse freed memory.

As developers, we can improve memory efficiency by using generators, releasing unnecessary references, managing resources with context managers, and profiling memory usage when required.


## 5. Explain exception handling in Python.
Exception handling is the way by which a programmer can control an error within the program without breaking out the flow of execution. 
```python
try:
    # Part which might cause an error
except TypeError:
    # What happens when error occurs | In this case what happens what a TypeError occurs
else:
    # what happens if there is no exception | Optional
finally:
    # Executed after try and except| always executed | Optional
```
Examples :- TypeError, ValueError, ImportError, KeyError, IndexError, NameError, PermissionError, EOFError, ZeroDivisionError, StopIteration

##  6. Explain some changes in Python 3.8
Positional arguments representation
```python
def sum(a,b,/,c=10):
    return a+b+c
sum(10,12,c=12)
```
F String can also do operations
```python
a,b = 10, 12
f"Sum of a and b is {a+b}"
f"Value of c is {(c := a+b)}"
```


## 7. Explain Python Design Patterns

Design patterns are reusable solutions to commonly occurring software design problems. They provide a structured way to organize code, improve maintainability, reduce coupling, and make applications easier to extend.

In Python, design patterns are commonly grouped into three categories:

1. **Creational Patterns:** Deal with object creation.
2. **Structural Patterns:** Deal with how classes and objects are composed.
3. **Behavioral Patterns:** Deal with communication and responsibility between objects.

---

### 7.1 Creational Design Patterns

Creational patterns provide different ways to create objects while keeping object creation flexible and manageable.

#### 1. Singleton Pattern

**Definition:** Ensures that a class has only one shared instance and provides a common access point to it.

**Use cases:**
- Application configuration.
- Shared application services.
- Certain resource managers.

**Python example:**

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  # True
```

**Explanation:** The `__new__()` method controls object creation. Once an instance exists, subsequent calls return that same instance.

**Note:** This basic implementation is not thread-safe. In production applications, consider dependency injection or a properly synchronized implementation when necessary.

#### 2. Factory Pattern

**Definition:** Encapsulates object creation so that the calling code does not need to know the concrete class being instantiated.

**Use cases:**
- Creating different notification services.
- Selecting payment providers.
- Choosing database or storage implementations.

**Python example:**

```python
class EmailNotification:
    def send(self, message):
        print(f"Email: {message}")


class SMSNotification:
    def send(self, message):
        print(f"SMS: {message}")


def notification_factory(channel):
    if channel == "email":
        return EmailNotification()
    elif channel == "sms":
        return SMSNotification()
    raise ValueError("Unsupported notification channel")


notification = notification_factory("email")
notification.send("Your order has been shipped.")
```

**Explanation:** The factory decides which object to create. The calling code uses the returned object without directly constructing the concrete class.

#### 3. Builder Pattern

**Definition:** Separates the construction of a complex object from its representation, allowing it to be created step by step.

**Use cases:**
- Building complex configuration objects.
- Constructing API request payloads.
- Creating objects with many optional fields.

**Python example:**

```python
class User:
    def __init__(self, name, email=None, role="user"):
        self.name = name
        self.email = email
        self.role = role


class UserBuilder:
    def __init__(self, name):
        self.name = name
        self.email = None
        self.role = "user"

    def set_email(self, email):
        self.email = email
        return self

    def set_role(self, role):
        self.role = role
        return self

    def build(self):
        return User(self.name, self.email, self.role)


user = (
    UserBuilder("Shiv")
    .set_email("shiv@example.com")
    .set_role("admin")
    .build()
)

print(user.name, user.role)
```

**Explanation:** The builder creates the object incrementally. Method chaining makes the construction process readable.

---

### 7.2 Structural Design Patterns

Structural patterns describe how objects and classes can be combined to form larger, flexible structures.

#### 4. Adapter Pattern

**Definition:** Allows incompatible interfaces to work together by converting one interface into another expected by the client.

**Use cases:**
- Integrating third-party APIs.
- Supporting legacy services.
- Standardizing different payment providers.

**Python example:**

```python
class LegacyPayment:
    def make_payment(self, amount):
        print(f"Legacy payment: {amount}")


class PaymentAdapter:
    def __init__(self, legacy_payment):
        self.legacy_payment = legacy_payment

    def pay(self, amount):
        self.legacy_payment.make_payment(amount)


payment = PaymentAdapter(LegacyPayment())
payment.pay(500)
```

**Explanation:** The adapter exposes the `pay()` interface while delegating the actual operation to the legacy implementation.

#### 5. Decorator Pattern

**Definition:** Adds behavior to an object or function without modifying its underlying implementation.

**Use cases:**
- Logging.
- Authentication and authorization.
- Timing and performance measurement.
- Caching and retries.

**Python example:**

```python
from functools import wraps


def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@log_execution
def get_user():
    return {"id": 1, "name": "Shiv"}


print(get_user())
```

**Explanation:** The decorator wraps the original function and adds logging before calling it. Python's function decorators are a common way to implement this pattern.

#### 6. Facade Pattern

**Definition:** Provides a simple interface to a complex subsystem.

**Use cases:**
- Simplifying interactions with multiple services.
- Wrapping complex SDKs.
- Coordinating several operations behind one method.

**Python example:**

```python
class InventoryService:
    def reserve(self, product_id):
        print(f"Reserved product {product_id}")


class PaymentService:
    def charge(self, amount):
        print(f"Charged {amount}")


class OrderFacade:
    def __init__(self):
        self.inventory = InventoryService()
        self.payment = PaymentService()

    def place_order(self, product_id, amount):
        self.inventory.reserve(product_id)
        self.payment.charge(amount)


order = OrderFacade()
order.place_order(101, 1500)
```

**Explanation:** The facade hides the details of coordinating inventory and payment operations behind a single method.

---

### 7.3 Behavioral Design Patterns

Behavioral patterns focus on communication, control flow, and the responsibilities assigned to objects.

#### 7. Strategy Pattern

**Definition:** Defines a family of interchangeable algorithms and allows the algorithm to be selected at runtime.

**Use cases:**
- Payment processing.
- Discount calculations.
- Selecting different retry or routing policies.

**Python example:**

```python
class CardPayment:
    def pay(self, amount):
        print(f"Paid {amount} using card")


class UPIPayment:
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


class Checkout:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def complete_payment(self, amount):
        self.payment_strategy.pay(amount)


checkout = Checkout(UPIPayment())
checkout.complete_payment(1000)
```

**Explanation:** `Checkout` delegates payment processing to the selected strategy. A different strategy can be supplied without changing the checkout logic.

#### 8. Observer Pattern

**Definition:** Establishes a one-to-many relationship so that multiple subscribers can be notified when an event occurs.

**Use cases:**
- Event-driven systems.
- Notification services.
- Application event handling.
- Kafka-based event workflows, where the broader event-driven concept is related but Kafka is not itself the Observer pattern.

**Python example:**

```python
class Order:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, callback):
        self.subscribers.append(callback)

    def place_order(self):
        print("Order placed")

        for callback in self.subscribers:
            callback()


def send_email():
    print("Sending order confirmation email")


def update_inventory():
    print("Updating inventory")


order = Order()
order.subscribe(send_email)
order.subscribe(update_inventory)
order.place_order()
```

**Explanation:** When the order is placed, all registered subscribers are notified.

#### 9. Command Pattern

**Definition:** Encapsulates a request as an object, allowing the request to be executed, queued, logged, or potentially undone.

**Use cases:**
- Task queues.
- Background jobs.
- Undo/redo functionality.
- Scheduling operations.

**Python example:**

```python
class Light:
    def turn_on(self):
        print("Light turned on")


class TurnOnCommand:
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


light = Light()
command = TurnOnCommand(light)
command.execute()
```

**Explanation:** The command object encapsulates the action, separating the requester from the object that performs the operation.

---

### 7.4 Summary of Common Design Patterns

| Pattern | Category | Main Purpose |
|---|---|---|
| Singleton | Creational | Reuse one shared instance |
| Factory | Creational | Centralize object creation |
| Builder | Creational | Construct complex objects step by step |
| Adapter | Structural | Make incompatible interfaces work together |
| Decorator | Structural | Add behavior without changing the original implementation |
| Facade | Structural | Simplify access to a complex subsystem |
| Strategy | Behavioral | Switch between interchangeable algorithms |
| Observer | Behavioral | Notify subscribers when an event occurs |
| Command | Behavioral | Encapsulate a request as an object |

### 7.5 Which Design Patterns Are Useful in Backend Development?

For Python backend development with Django, FastAPI, microservices, and GenAI applications, these patterns are especially useful:

- **Factory:** Create different LLM clients, notification providers, or storage backends.
- **Strategy:** Switch between embedding models, retrieval strategies, or payment algorithms.
- **Adapter:** Standardize interfaces for external APIs and third-party services.
- **Decorator:** Implement logging, caching, timing, and cross-cutting behavior.
- **Facade:** Simplify workflows that coordinate multiple backend services.
- **Observer:** React to application events and trigger notifications or downstream processing.
- **Dependency Injection:** Supply repositories, database sessions, or service implementations to components instead of constructing dependencies directly.

Dependency injection is a design technique rather than one of the original Gang of Four patterns, but it is particularly important in modern Python backend frameworks.

### 7.6 Interview Summary

Design patterns are reusable approaches to common software design problems. They are classified into creational, structural, and behavioral patterns. In Python backend development, Factory, Strategy, Adapter, Decorator, and Facade patterns are particularly useful for building maintainable, extensible, and loosely coupled applications.

**Best practice:** Choose a pattern when it solves a real design problem. Applying too many patterns unnecessarily can make code more complicated rather than improving it.


## 8. How would you load large data file in Python?
The best way is to load data in chunks, Pandas provides option to define chunk size while loading any file. 
```python
for chunk in pd.read_csv(file.csv, chunksize=1000):
    process(chunk)
    
pd.read_csv('file.csv', sep='\t', iterator=True, chunksize=1000)
```
Another way is to use context manager.
```python
with open("log.txt") as infile:
    for line in infile:
        do_something_with(line)
```

## 9. Explain Generators and use case of it.
A function or method which uses the yield statement is called a generator function. Such a function, when called, always returns an iterator object which can be used to execute the body of the function: calling the iterator’s iterator.\__next__()method will cause the function to execute until it provides a value using the yield statement. <br>
When the function executes a return statement or falls off the end, a StopIteration exception is raised and the iterator will have reached the end of the set of values to be returned. Note that a generator can have n numbers of yield statements
#### Use Case
Generators are good for calculating large sets of results where you don't know if you are going to need all results, or where you don't want to allocate the memory for all results at the same time.

```python
# Search function as generator, effective for returning some set as result with functionality like 'Load 10 more items'
def search_result(keyword):
    while keyword in dataset:
        yield matched_data

search_object = search_result('keyword')
# type(search_function)  --> <class 'generator'>

search_object.__next__()
```
Note: You can only iterate over a generator once, if you try to loop over it second time it will return nothing. Generators also do not store all the values in memory, they generate the values on the fly
```python
mygenerator = (x*x for x in range(3))
```
When you call a generator function, the code you have written in the function body does not run. The function only returns the generator object.
Example: https://github.com/baliyanvinay/Python-Advanced/blob/main/Generator.py

## 10. Is there a sequence in defining exceptions in except block for exception handling?
Yes can be defined in a tuple. From left to right will be executed based on the exception raised. 
```python
try:
    pass
except (TypeError, IndexError, RuntimeError) as error:
    pass
```

## 11. Explain Closures in Python
A closure is a functionality in Python where some data is memorized in the memory for lazy execution. Decorators heavily rely on the concept of closure. <br>
To create a closure in python:-
1. There must be a nested function(function within a enclosing/outer function)
2. The nested function must refer to a value defined in the enclosing function
3. The enclosing function must return(not call it) the nested function.
```python
def enclosing_function(defined_value):
    def nested_function():
        return defined_value+some_operation
    return nested_function

closure_function = enclosing_function(20)
closure_function() # returns 20+some_operation
```
Objects are data with methods attached, closures are functions with data attached.

## 12. How to make a chain of function decorators?
```python
def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@make_bold
@make_italic
def index():
    return "hello world"

print(index()) 
## returns "<b><i>hello world</i></b>"

```

## 13. Three different ways to fetch every 3rd item of a list
Using index jump
```python
>>> example_list = [0,1,2,3,4,5,6]
>>> example_list = [::3] # returns [0,3,6]
```
Using list comphrehension
```python
>>> [x for x in example_list if example_list.index(x)%3==0]
>>> [0,3,6]
```
Using while loop
```python
i = 0
while i < len(example_list):
    print(example_list[i])
    i += 3
```

## 14. What is MRO in Python? How does it work?
Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes. Especially it plays vital role in the context of multiple inheritance as single method may be found in multiple super classes. 
```python
class A:
    def process(self):
        print('A')
        
class B(A):
    pass
    
class C(A):
    def process(self):
        print('C')

class D(B,C):
    pass
    
obj = D()
obj.process()
# D -> B -> C -> A -> object 
```
Note: a class can't be called before its superclass in resolving MRO. Super Class has to be called after derived class

## 15. What is monkey patching? How to use it in Python?
Monkey patching refers to the practice of dynamically modifying or extending code at runtime, typically to change the behavior of existing classes, modules, or functions. 

Monkey patching can be useful in several scenarios:
1. Testing: It allows to replace parts of code during testing with mock objects or functions. 
2. Hotfixes: In situations where you can't immediately deploy a fix to production code, monkey patching can be used as a temporary solution to address critical issues without waiting for a formal release cycle.
3. Extending functionality: It enables to add new features or alter the behavior of existing code without modifying the original source. This can be useful when working with third-party libraries or legacy code that you can't modify directly.

```python
# Original module
class OriginalClass:
    def method(self):
        return "Original method"

# Monkey patching
def new_method(self):
    return "Patched method"

# Patching the class method
OriginalClass.method = new_method
# Using the patched code
obj = OriginalClass()
print(obj.method())  # Output: "Patched method"
```

## 16. What is the difference between staticmethod and classmethod?
| Parameter | Class Method | Static Method |
| :-------------:|:-------------:| :-------------:|
| Decorator | @classmethod | @staticmethod |
| Use Case| More widely used as a factory method to class | Acts as utility functions |
| Scope | Bound to the classs and not objects | Also bound to class and not objects |
| Behaviour | Can modify the state of the class | Can't access class state |
| Parameter | Takes cls as first parameter | No specific parameter |
```python
class Circle:
    no_of_circles = 0
    def __init__(self, radius):
        self.radius = radius
        Circle.no_of_circles += 1
        
    @staticmethod
    def square(num):
        return num**2
    
    @classmethod
    def getCircleCount(cls):
        return cls.no_of_circles
```

## 17. What is the purpose of the single underscore “_” variable in Python?
Python automatically stores the value of last expression in interpreter in single underscore. 
```python
>>> 78 + 89
167
>>> _
167
```
Single underscore used in unpacking to ignore value(s). 
```python
>>> a, _, b = (1, 12, 2)
>>> a, *_, b = (1, 12, 13, 14, 15, 16, 2) # only want first and last value
>>> a, *x, b = (1, 12, 13, 14, 15, 16, 2) # note that any other name can also be used
>>> _ # returns a list of elements
[12, 13, 14, 15, 16]
```
It is most commonly used in loops where we are not interested in the value returned by the iterator.
```python
for _ in range(5):
    print('Some operations')
```
Note that it is entirely the convention to use single underscore in all these ways to avoid having defined extra variable for such operations.

## 18. What's the difference between a Python module and a Python package?
#### Module
The module is a Python file that contains collections of functions and global variables and with having a .py extension file.
### Package
The package is a directory having collections of modules. This directory contains Python modules and also having __init__.py file by which the interpreter interprets it as a Package. 


## 19. What Is the Global Interpreter Lock (GIL)?

The **Global Interpreter Lock (GIL)** is a mechanism used by the standard CPython interpreter that, in traditional GIL-enabled builds, allows only one thread at a time to execute Python bytecode within a process.

The GIL simplifies aspects of memory management and object access in CPython, but it can limit parallel execution of CPU-bound Python code using multiple threads.

### 19.1 Why Does Python Have a GIL?

In traditional CPython, the GIL helps protect interpreter state and simplifies the implementation of reference counting and other internal operations.

Without appropriate synchronization, concurrent access to shared interpreter data could cause consistency and memory-management problems.

**Important:** The GIL is an implementation detail of CPython, not a rule that applies to every Python implementation or every Python build.

### 19.2 How Does the GIL Work?

Consider two threads executing Python code in the same process:

1. Thread 1 acquires the GIL and executes Python bytecode.
2. Thread 2 waits until it can acquire the GIL.
3. The interpreter may switch execution between threads.
4. Only one thread at a time executes Python bytecode under the traditional GIL.

Threads can still be useful for I/O-bound tasks because the GIL is commonly released while a thread waits for I/O. Some native extensions also release the GIL while performing operations in native code.

### 19.3 Example: Using Multiple Threads

```python
import threading
import time


def task(name):
    print(f"{name} started")
    time.sleep(1)
    print(f"{name} completed")


start = time.perf_counter()

t1 = threading.Thread(target=task, args=("Thread 1",))
t2 = threading.Thread(target=task, args=("Thread 2",))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Total time: {time.perf_counter() - start:.2f} seconds")
```

**Explanation:**

- Both threads perform an I/O-like waiting operation using `time.sleep()`.
- While one thread sleeps, another can run.
- The tasks can overlap, so the total time is approximately one second rather than two seconds, excluding overhead.

This example demonstrates why threading is useful for waiting tasks; it does not demonstrate CPU-bound parallelism.

### 19.4 CPU-Bound Tasks and the GIL

CPU-bound tasks perform substantial computation, such as large calculations or repeated numerical operations.

In a traditional GIL-enabled CPython build, multiple threads generally cannot execute Python bytecode in parallel across multiple CPU cores.

```python
import threading


def calculate():
    total = 0
    for i in range(10_000_000):
        total += i


t1 = threading.Thread(target=calculate)
t2 = threading.Thread(target=calculate)

t1.start()
t2.start()

t1.join()
t2.join()
```

Both threads perform CPU-intensive work, but the GIL limits parallel execution of their Python bytecode. Depending on the workload and overhead, using threads may not improve performance.

### 19.5 How Can We Overcome GIL Limitations?

**1. Multiprocessing**

The `multiprocessing` module creates separate processes. Each process has its own interpreter and, in traditional CPython, its own GIL.

```python
from multiprocessing import Process


def calculate():
    total = sum(range(10_000_000))
    print(total)


if __name__ == "__main__":
    p1 = Process(target=calculate)
    p2 = Process(target=calculate)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
```

Separate processes can execute CPU-bound work in parallel on multiple CPU cores, subject to available hardware and process overhead.

**2. Use Native Libraries**

Libraries such as NumPy can perform computationally intensive operations in optimized native code. Some operations release the GIL, allowing parallel execution when supported by the library and operation.

**3. Use Asynchronous Programming for I/O**

`asyncio` helps manage many concurrent I/O operations, such as HTTP requests and database calls. It does not, by itself, enable CPU-bound Python code to execute in parallel across multiple cores.

**4. Consider Free-Threaded CPython**

Python 3.13 introduced an optional free-threaded CPython build designed to run without the GIL. Compatibility, extension support, and performance characteristics depend on the environment and workload.

### 19.6 GIL vs. Multithreading vs. Multiprocessing

| Feature | Multithreading | Multiprocessing |
|---|---|---|
| Execution unit | Threads | Processes |
| Memory | Usually shared within a process | Separate process memory by default |
| CPU-bound Python code in traditional CPython | Limited by the GIL | Can execute in parallel |
| I/O-bound work | Often effective | Can work, but may add unnecessary overhead |
| Communication | Shared objects require synchronization when needed | Often uses queues, pipes, or other IPC |
| Overhead | Usually lower | Usually higher |

### 19.7 Common Interview Questions

**Q1. Does the GIL prevent multithreading?**

No. It permits multiple threads, but in traditional GIL-enabled CPython, only one thread at a time executes Python bytecode in a process. Threads can still overlap I/O operations.

**Q2. Is Python threading useless because of the GIL?**

No. Threading is useful for I/O-bound tasks, such as network requests, file operations, and waiting for responses from external services.

**Q3. Does the GIL make every Python operation thread-safe?**

No. Shared mutable state may still require synchronization, such as locks, to prevent race conditions.

**Q4. Does `asyncio` solve the GIL problem?**

No. `asyncio` supports cooperative concurrency, particularly for I/O-bound work. It does not remove the GIL or automatically parallelize CPU-bound Python code.

**Q5. Is the GIL present in every Python implementation?**

No. The GIL discussed here applies primarily to traditional CPython builds. Other implementations and optional free-threaded CPython builds have different behavior.

### 19.8 Interview Summary

The Global Interpreter Lock is a mechanism in traditional GIL-enabled CPython that allows only one thread at a time to execute Python bytecode within a process. It simplifies interpreter and memory-management implementation, but can limit CPU-bound multithreading. For I/O-bound workloads, threading and asynchronous programming are useful; for CPU-bound workloads, multiprocessing or suitable native libraries can provide parallelism.


## 20. Which is faster, list comprehension or for loop?
List comprehensions are generally faster than 'a for loop' because of the implementation of both. One key difference is that 'for loop' generally rounds up more than one statement/operation as compared to 'list comprehension' which has to perform single operation on all the elements. For example, creating a list or update in an existing list is faster when done using list comprehension.


## 21. Explain Singleton Class and Its Uses

### 21.1 What Is the Singleton Pattern?

The **Singleton Pattern** is a creational design pattern that ensures a class has only one instance and provides a shared access point to that instance.

It is useful when multiple parts of an application need to access the same shared resource or service.

**Key characteristics:**
- A single shared instance is reused.
- Object creation is controlled by the class or a dedicated provider.
- Multiple callers access the same instance.
- It can help centralize access to shared resources.

### 21.2 How to Implement a Singleton in Python

Python does not have a built-in `Singleton` keyword. One way to implement the pattern is by overriding `__new__()`, which controls object creation.

**Example:**

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance


obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  # True
print(id(obj1) == id(obj2))  # True
```

**Output:**

```text
True
True
```

**Explanation:**

1. The class variable `_instance` initially stores `None`.
2. When `Singleton()` is called for the first time, `__new__()` creates an instance.
3. The created instance is stored in `_instance`.
4. On subsequent calls, the existing instance is returned.
5. Both `obj1` and `obj2` reference the same object.

**Important:** This simple implementation is not thread-safe. Concurrent calls could create multiple instances unless object creation is synchronized.

### 21.3 Singleton Using a Class Decorator

A decorator can also control instance creation. However, a decorator that returns a function changes the decorated class name into a callable wrapper rather than leaving it as the original class.

```python
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)

        return instances[cls]

    return get_instance


@singleton
class AppConfig:
    def __init__(self):
        self.environment = "development"


config1 = AppConfig()
config2 = AppConfig()

print(config1 is config2)  # True
```

This example demonstrates the concept, but it is not inherently thread-safe.

### 21.4 Real-World Uses of the Singleton Pattern

**1. Application Configuration**

A shared configuration object can provide access to application settings such as environment names, feature flags, and service endpoints.

**2. Logging**

Applications can share a configured logging facility. In Python, the standard `logging` module already manages named loggers, so a custom Singleton class is usually unnecessary.

**3. Shared Resource Managers**

A singleton-like provider may coordinate access to a shared resource manager, such as a cache client or connection pool.

**4. Feature or Settings Registry**

A centralized registry can expose application-wide settings or registered components.

**5. Shared Service Objects**

An application may reuse a stateless service object when creating a new instance each time provides no benefit.

### 21.5 Singleton vs. Normal Class

| Feature | Normal Class | Singleton Pattern |
|---|---|---|
| Instance creation | Multiple instances can be created | Intended to reuse one instance |
| State | Each instance may have independent state | State is shared through the same instance |
| Access | Each object has its own identity | Callers share the same object |
| Typical use | Independent business objects | Shared configuration or coordinated services |

### 21.6 Advantages of Singleton

- Provides a shared instance across multiple callers.
- Can avoid repeated creation of expensive objects.
- Centralizes access to certain shared resources.
- Can simplify access to application-wide state.

### 21.7 Disadvantages of Singleton

- Introduces global shared state, which can make testing harder.
- Can create tight coupling between components.
- Shared mutable state may cause concurrency problems.
- Can make dependencies less visible.
- May complicate scaling when each process needs its own independent state.

**Best practice:** Consider dependency injection instead of a custom Singleton when building larger applications. For example, a FastAPI application can create a shared service or database connection pool during application startup and inject it into request handlers.

### 21.8 Interview Questions

**Q1. What is the difference between `__new__()` and `__init__()`?**

- `__new__()` creates and returns an instance.
- `__init__()` initializes an already-created instance.

**Q2. Is a Singleton automatically thread-safe?**

No. A basic implementation using a class variable can create multiple instances under concurrent calls. Appropriate synchronization or another design is required when thread safety matters.

**Q3. Is a Singleton shared across multiple processes?**

No. A normal Python Singleton exists within its process. Separate worker processes generally have separate instances.

**Q4. Is Singleton always a good design choice?**

No. It is appropriate when a single shared instance is genuinely required, but dependency injection is often more flexible and easier to test.

### 21.9 Interview Summary

The Singleton Pattern is a creational design pattern that restricts a class to one shared instance. In Python, it can be implemented using `__new__()`, a metaclass, or another instance provider. Common use cases include application configuration and shared service objects. However, developers should consider thread safety, testing, process boundaries, and dependency injection before adopting it.


## 22. Explain Metaclasses in Python

### 22.1 What Is a Metaclass?

A **metaclass is a class that creates or controls the creation of other classes**.

In Python, objects are created from classes, and classes themselves are also objects. By default, Python uses the built-in `type` metaclass to create classes.

In simple terms:

- A class defines how its instances behave.
- A metaclass defines how a class is created or customized.

**Example:**

```python
class Employee:
    pass


employee = Employee()

print(type(employee))  # <class '__main__.Employee'>
print(type(Employee))  # <class 'type'>
```

**Explanation:**

1. `Employee` is a class.
2. `employee` is an instance of `Employee`.
3. `type(employee)` returns the class of the object.
4. `type(Employee)` returns `type`, because `type` is the default metaclass used to create the class.

### 22.2 How Does `type()` Work?

Python's `type()` has two common uses.

**Use 1: Inspect an object's type**

```python
x = 10

print(type(x))  # <class 'int'>
```

**Use 2: Create a class dynamically**

```python
Employee = type(
    "Employee",
    (),
    {"role": "Developer"}
)

employee = Employee()

print(employee.role)  # Developer
```

The three arguments are:

1. **Class name:** `"Employee"`
2. **Base classes:** `()` means there are no explicitly specified base classes.
3. **Class attributes:** A dictionary containing `{"role": "Developer"}`.

This example creates a class dynamically instead of using a traditional `class` statement.

### 22.3 Creating a Custom Metaclass

A custom metaclass usually inherits from `type`. You can override methods such as `__new__()` to customize class creation.

**Example:**

```python
class MyMeta(type):
    def __new__(mcls, name, bases, namespace):
        print(f"Creating class: {name}")

        return super().__new__(
            mcls,
            name,
            bases,
            namespace
        )


class Employee(metaclass=MyMeta):
    role = "Developer"


class Manager(metaclass=MyMeta):
    role = "Manager"
```

**Output:**

```text
Creating class: Employee
Creating class: Manager
```

**Explanation:**

1. Python encounters the `Employee` class definition.
2. It calls the custom metaclass's `__new__()` method.
3. The metaclass receives the class name, base classes, and class namespace.
4. The method can inspect or modify the class definition.
5. `super().__new__()` creates and returns the class object.

The same process occurs when Python defines `Manager`.

**Important:** The custom metaclass runs when the class is created, not every time an instance of that class is created.

### 22.4 Practical Example: Automatically Validating Class Attributes

Suppose every class representing a database model must define a `table_name` attribute.

A metaclass can validate this requirement when the class is defined.

```python
class ModelMeta(type):
    def __new__(mcls, name, bases, namespace):
        is_base_model = name == "BaseModel"

        if not is_base_model and "table_name" not in namespace:
            raise TypeError(
                f"{name} must define a table_name"
            )

        return super().__new__(
            mcls,
            name,
            bases,
            namespace
        )


class BaseModel(metaclass=ModelMeta):
    pass


class User(BaseModel):
    table_name = "users"


class Product(BaseModel):
    table_name = "products"
```

Both `User` and `Product` are created successfully because they define `table_name`.

If a subclass omits this attribute, Python raises a `TypeError` during class creation.

**Note:** This example deliberately requires each subclass to declare its own `table_name`. Frameworks may use different inheritance and validation rules.

### 22.5 What Is the Difference Between a Metaclass and a Class Decorator?

| Feature | Metaclass | Class Decorator |
|---|---|---|
| Purpose | Customizes class creation | Modifies or wraps a class after it is created |
| Mechanism | Usually inherits from `type` | A function or callable receives a class |
| When it runs | During class creation | After the class object has been created |
| Typical use | Enforcing rules across a family of classes | Adding attributes, registering classes, or wrapping behavior |
| Complexity | Generally more advanced | Often simpler |

Use a class decorator when the requirement is straightforward. Consider a metaclass when class creation itself must be customized systematically.

### 22.6 Common Uses of Metaclasses

**1. Framework Development**

Frameworks can use metaclasses to inspect class definitions and register models or components automatically.

**2. Class Validation**

Enforce required class attributes, methods, or naming conventions when a class is defined.

**3. Automatic Registration**

Register subclasses in a central registry so that plugins or implementations can be discovered automatically.

**4. ORM Design**

Object-relational mapping frameworks can inspect model declarations and construct metadata. Metaclasses are one technique for this; modern frameworks may also use class hooks, descriptors, or other mechanisms.

**5. API and Plugin Frameworks**

Metaclasses can enforce conventions across plugin classes or API component definitions.

### 22.7 Advantages and Disadvantages

**Advantages:**
- Centralizes class-level rules.
- Enables automatic class registration and validation.
- Supports advanced framework and library development.
- Reduces repetitive setup across related classes.

**Disadvantages:**
- Makes code harder to understand and debug.
- Can introduce unexpected behavior during class creation.
- May complicate inheritance and metaclass compatibility.
- Is often unnecessary for ordinary application code.

### 22.8 Metaclass vs. `__new__()` vs. `__init__()`

| Method | Responsibility |
|---|---|
| Metaclass `__new__()` | Creates the class object |
| Metaclass `__init__()` | Initializes the created class object |
| Class `__new__()` | Creates an instance of that class |
| Class `__init__()` | Initializes that instance |

The meaning of `__new__()` and `__init__()` depends on which class defines them. When defined on a metaclass, they participate in creating and initializing classes.

### 22.9 Interview Summary

A metaclass is a class that controls how other classes are created. Python's default metaclass is `type`. Custom metaclasses typically inherit from `type` and can inspect, validate, modify, or register classes during class creation. They are useful in frameworks, ORMs, plugin systems, and class validation, but should be used only when simpler approaches such as class decorators or `__init_subclass__()` are insufficient.


## 23. Best way to concatenate n number of strings together into one.
The best way of appending a string to a string variable is to use + or +=. This is because it's readable and fast. However in most of the codebases we see use of append and join when joining strings together, this is done for readablity and cleaner code. Sometimes it is more important to have code readablity to actually understand the operation.
```python
first_name = 'Max '
last_name = 'Verstappen'
full_name = first_name + last_name
# using join string method
full_name = ''.join( (first_name, last_name) ) # takes in tuple of string in case of multiple values
```

## 24. Explain briefly about map() and lambda() functions.
### map(function, iterable)
Map function returns an iterator that applies function to every item in the iterable. In case multiple iterables are passed, the iterator stops when the shortest iterable is exhausted.
```python
def custom_power(x, y):
    return x**y

values = [1,2,3,4]
powers = [2,1,2] 
map_iterator = map(custom_power, values, powers) # will skip the power of 4
print(list(map_iterator)) # [1,2,9]
```
### lambda parameters: expression
Lambda expression yields an anonymous function object. Note that functions created with lambda expressions cannot contain statements or annotations. For example, can't assign variables in lambda definition.
```python
>>> # lambda [parameter list] : expression
>>> list(map(lambda x: x+10, [1,2,3])) # [11,12,13]
>>> func =  lambda x: x+10 # <function <lambda> at 0x7fdb99e9c310>
>>> func(25) # returns 35
>>> lambda : 'hello' # with no parameter
```

## 25. Explain Abstract Classes and its uses.
An abstract class can be considered as a blueprint for other classes. It allows you to create a set of methods that must be created within any child classes built from the abstract class. Or in more general terms, a class which contains one or more abstract methods is called an abstract class.<br>
By default Python does not provide abstract class, ABC module of Python can be used to define an abstract class. 
### Abstract Method
Abstract method is a method that has a declaration but does not have an implementation. This ensures that any class built from this class will have to implement the method. 
```python
from abc import ABC, abstractmethod
class DB_PLugin(ABC):
    @abstractmethod
    def add_source(self):
        pass
```

## 26. Explain object creation process in detail. Which method is called first?
When an object of a class is created or a class is instantiated, the \__new__() method of class is called. This particular method is resposible for returning a new class object. It can be overriden to implement object creational restrictions on class. <br>
- The constructor of the class is \__new__() and 
- the initializer of the class is \__init__(). <br>
Initializer is called right after the constructor, if the constructor has not returned a class object, the initializer call is useless. <br>
Note that the reason \__init__() could use class object(self) to initialize is because when the code flow reaches \__init__() the object of the class is already created. 

## 27. Difference between a class variable and instance variable.
| Parameter | Class Variable | Instance Variable |
| :-------------:|:-------------:| :-------------:|
| Declaration | Inside class definition but outside of any instance methods | Inside constructor method i.e., \__init__ |
| Scope | Shared across all objects | Tied to the object instance |
| Behaviour | Any change is reflected across all instances | Change limited to instances only |
| Access | cls.variable_name | self.variable_name |

```python
class Car:
    total_cars, wheels = 0, 4
    def __init__(self, engine_power):
        self.engine_power =  engine_power
        Car.total_cars += 1 # incremented anytime a new car is added. 
        
kia_sonet = Car(120)
print(kia_sonet.wheels) # returns 4
kia_sonet.wheels += 1 # extra wheel
print(kia_sonet.wheels) # returns 5

print(Car.total_cars) # returns 1
print(Car.wheels) # returns 4 not 5
Car.wheel = 6 # two extra wheels

print(kia_sonet.wheels) # returns 6 now
```
Example: https://github.com/baliyanvinay/Python-Advanced/blob/main/Class%20Variables.py

## 28. Explain the concept behind dictionary in Python
- A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value.
- A key can appear in a dictionary only once. Duplicate keys are not allowed
- Using a key twice in initial dict definition will override the first entry
- Key must be of a type that is immutable. Values can be anything

```python
>>> dict_sample_01 = {1: 12, 2: 14, 1: 16}
>>> dict_sample_02 # {1: 16, 2: 14}
>>> dict_sample_02 = dict.fromkeys('123')
>>> dict_sample_02 # {'1': None, '2': None, '3': None}
```

## 29. Difference between an expression and a statement in Python
A statement is a complete line of code that performs some action, while an expression is any section of the code that evaluates to a value. An expression is also a statement. Note that lambda function in Python only accepts expressions. 


## 30. Explain Threading in Python

### 30.1 What Is Threading in Python?

**Threading is a technique that allows multiple threads to execute concurrently within the same process.**

A thread is a lightweight unit of execution. Threads within the same process share memory and resources, making it convenient to perform multiple tasks without creating separate processes.

Python provides the built-in `threading` module to create, manage, and synchronize threads.

**Common use cases:**
- Sending multiple HTTP requests.
- Reading and writing files.
- Performing database operations.
- Downloading multiple files.
- Handling I/O-bound tasks concurrently.

### 30.2 How Does Threading Work?

Suppose an application needs to download three files.

Without threading, the application may download each file one after another. With threading, it can start multiple download operations so their waiting periods overlap.

**Execution flow:**

1. The main thread creates worker threads.
2. Each worker thread executes a specified function.
3. The threads run concurrently, sharing the process's memory.
4. The main thread can wait for completion using `join()`.
5. The application continues after the required threads finish.

### 30.3 Creating a Thread in Python

Python provides `threading.Thread()` to create a thread.

**Example:**

```python
import threading


def task(name):
    print(f"{name} is executing")


t1 = threading.Thread(target=task, args=("Thread 1",))
t2 = threading.Thread(target=task, args=("Thread 2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("All threads completed")
```

**Explanation:**

- `target`: Specifies the function the thread executes.
- `args`: Passes positional arguments to the target function.
- `start()`: Starts the thread.
- `join()`: Waits for that thread to finish.
- The execution order of the worker threads is not guaranteed.

**Important:** Calling `task()` directly executes the function in the current thread. Using `target=task` and calling `start()` schedules it to execute in a worker thread.

### 30.4 Threading for I/O-Bound Tasks

Threading is particularly useful when tasks spend substantial time waiting for network responses, files, or other I/O operations.

**Example:**

```python
import threading
import time


def download_file(file_name):
    print(f"Downloading {file_name}")
    time.sleep(2)  # Simulates waiting for I/O
    print(f"Downloaded {file_name}")


start = time.perf_counter()

threads = []

for name in ["file1", "file2", "file3"]:
    thread = threading.Thread(
        target=download_file,
        args=(name,)
    )
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Total time: {time.perf_counter() - start:.2f} seconds")
```

**Expected behavior:** The three simulated waiting periods overlap, so execution takes approximately two seconds plus overhead, rather than six seconds.

The exact timing depends on system load and scheduling. `time.sleep()` simulates waiting; it does not perform an actual download.

### 30.5 Threading vs. the Global Interpreter Lock (GIL)

In traditional GIL-enabled CPython builds, the Global Interpreter Lock allows only one thread at a time to execute Python bytecode within a process.

This affects CPU-bound workloads differently from I/O-bound workloads.

- **I/O-bound tasks:** Threads can be effective because the GIL is commonly released while a thread waits for I/O.
- **CPU-bound tasks:** Threads generally do not provide parallel execution of Python bytecode across multiple CPU cores in traditional GIL-enabled CPython.
- **Alternative for CPU-bound tasks:** Consider multiprocessing or suitable native libraries that support parallel execution.

**Example:**

| Task | Recommended approach |
|---|---|
| Multiple HTTP requests | Threading or `asyncio` |
| File I/O | Threading |
| Waiting for database responses | Threading or asynchronous database clients |
| CPU-intensive Python calculations | Multiprocessing |
| Large numerical computations | Suitable optimized native libraries |

Python 3.13 and later also offer optional free-threaded CPython builds, so the GIL behavior depends on the interpreter build.

### 30.6 Race Conditions in Threading

A **race condition** occurs when the correctness of a program depends on the timing or interleaving of concurrent operations.

For example, multiple threads incrementing the same shared counter can produce incorrect results if the read-modify-write operations are not properly synchronized.

**Example using a lock:**

```python
import threading

counter = 0
lock = threading.Lock()


def increment():
    global counter

    for _ in range(10_000):
        with lock:
            counter += 1


t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print(counter)  # 20000
```

**Explanation:**

1. Both threads access the same global variable, `counter`.
2. `threading.Lock()` creates a mutual-exclusion lock.
3. `with lock:` allows only one thread at a time to execute the protected increment.
4. The lock is released automatically when execution leaves the `with` block.
5. The final result is `20000`.

**Important:** The GIL is not a substitute for proper synchronization of shared mutable state.

### 30.7 Common Threading Synchronization Tools

| Tool | Purpose |
|---|---|
| `Lock` | Allows one thread at a time into a protected section |
| `RLock` | Allows the same thread to acquire a lock recursively |
| `Semaphore` | Limits how many threads can access a resource simultaneously |
| `Event` | Signals a condition to waiting threads |
| `Condition` | Allows threads to wait for and signal specific conditions |
| `Queue` | Safely transfers work or data between threads |

**Example: Using a Queue**

```python
import threading
from queue import Queue

tasks = Queue()


def worker():
    while True:
        item = tasks.get()

        try:
            if item is None:
                return

            print(f"Processing {item}")
        finally:
            tasks.task_done()


thread = threading.Thread(target=worker)
thread.start()

tasks.put("Task 1")
tasks.put("Task 2")

tasks.join()
tasks.put(None)
thread.join()
```

The queue coordinates work between the main thread and the worker. `task_done()` marks each dequeued item as processed, including the sentinel item.

### 30.8 Threading vs. Multiprocessing vs. Asyncio

| Feature | Threading | Multiprocessing | Asyncio |
|---|---|---|---|
| Concurrency model | Multiple threads | Multiple processes | Cooperative tasks |
| Memory | Shared within a process | Separate process memory by default | Usually one process and event loop |
| I/O-bound tasks | Effective | Effective, but can add overhead | Highly effective for supported asynchronous I/O |
| CPU-bound Python code | Limited by the traditional GIL | Can run in parallel across CPU cores | Does not automatically provide CPU parallelism |
| Best suited for | Blocking I/O and concurrent tasks | CPU-intensive parallel work | Many concurrent I/O operations |

### 30.9 Advantages and Disadvantages

**Advantages:**
- Enables concurrent execution of tasks.
- Improves responsiveness during I/O waits.
- Shares memory within a process.
- Has less process-creation overhead than multiprocessing in many situations.

**Disadvantages:**
- Shared state can cause race conditions.
- Synchronization can make code more complex.
- Incorrect lock usage can lead to deadlocks.
- CPU-bound Python workloads may not benefit from additional threads under the traditional GIL.

### 30.10 Common Interview Questions

**Q1. What is the difference between `start()` and `run()`?**

- `start()` creates a separate thread of execution and invokes `run()` in that thread.
- Calling `run()` directly executes the method in the current thread.

**Q2. What is the purpose of `join()`?**

`join()` blocks the calling thread until the target thread terminates, unless a timeout is specified.

**Q3. What is a daemon thread?**

A daemon thread does not prevent the Python process from exiting. Daemon threads may be stopped abruptly at shutdown, so use explicit coordination and cleanup for important work.

**Q4. Can multiple Python threads execute at the same time?**

They can run concurrently. In traditional GIL-enabled CPython, only one thread at a time executes Python bytecode within a process, although threads may overlap I/O and native operations that release the GIL.

**Q5. What is a deadlock?**

A deadlock occurs when threads wait indefinitely for resources or locks held by one another.

**Q6. When should you use threading instead of multiprocessing?**

Use threading mainly for concurrent I/O-bound tasks. Consider multiprocessing when CPU-bound Python code needs parallel execution and the overhead is justified.

### 30.11 Interview Summary

Threading in Python allows multiple threads to execute concurrently within the same process. It is especially useful for I/O-bound tasks such as HTTP requests, file operations, and database calls. The `threading` module provides tools such as `Thread`, `Lock`, `Event`, and `Semaphore` to manage execution and shared resources. For CPU-bound Python code in traditional GIL-enabled CPython, multiprocessing is often a better choice.

## 31. Can set have lists as elements?
You can't add a list to a set because lists are mutable, meaning that you can change the contents of the list after adding it to the set. You can however add tuples to the set, because you cannot change the contents of a tuple. <br>
The objects have to be hashable so that finding, adding and removing elements can be done faster than looking at each individual element every time you perform these operations. <br>
Some unhashable datatypes:
- list: use tuple instead
- set: use frozenset instead

## 32. Is method overloading possible in Python?
Yes method overloading is possible in Python. It can be achived using different number of arguments. 
```python
def increment(value, by=1):
   return value+by

# calling function
increment(5) # returns 6
increment(5, 2) # return 7
```

## 33. Explain inheritance in Python.
![Inheritance in Python](https://github.com/baliyanvinay/Python-Interview-Preparation/blob/main/Inheritance.png)


## 34. Explain Method Resolution Order (MRO) for Multiple Inheritance

### 34.1 What Is Method Resolution Order (MRO)?

**Method Resolution Order (MRO)** is the order in which Python searches classes to find a method or attribute when inheritance is involved.

In multiple inheritance, a class can inherit from two or more parent classes. If multiple parents define the same method, Python uses the MRO to determine which implementation to call.

Python uses the **C3 linearization algorithm** to calculate the MRO. It provides a consistent ordering while respecting the inheritance relationships and declared parent-class order.

### 34.2 Simple Multiple Inheritance Example

```python
class A:
    def show(self):
        print("Class A")


class B:
    def show(self):
        print("Class B")


class C(A, B):
    pass


obj = C()
obj.show()

print(C.mro())
```

**Output:**

```text
Class A
[<class '__main__.C'>, <class '__main__.A'>,
 <class '__main__.B'>, <class 'object'>]
```

**Explanation:**

1. `C` inherits from `A` and `B`.
2. Python first checks class `C`.
3. Since `C` does not define `show()`, Python checks `A`.
4. `A` defines `show()`, so its method is executed.
5. Python does not continue searching for another implementation after finding the method.

The MRO is:

```text
C → A → B → object
```

### 34.3 Understanding MRO in a Diamond Inheritance Problem

A diamond inheritance structure occurs when two parent classes inherit from the same base class, and another class inherits from both parents.

```python
class A:
    def show(self):
        print("Class A")


class B(A):
    def show(self):
        print("Class B")


class C(A):
    def show(self):
        print("Class C")


class D(B, C):
    pass


obj = D()
obj.show()

print(D.mro())
```

**Output:**

```text
Class B
[<class '__main__.D'>, <class '__main__.B'>,
 <class '__main__.C'>, <class '__main__.A'>,
 <class 'object'>]
```

**MRO order:**

```text
D → B → C → A → object
```

**Explanation:**

- Python first checks `D`.
- `D` does not define `show()`.
- Python checks `B` before `C` because `D` declares its bases as `(B, C)`.
- `B` defines `show()`, so Python executes `B.show()`.
- The shared base class `A` appears only once in the MRO.

The C3 linearization algorithm ensures a consistent order for this inheritance hierarchy.

### 34.4 How Does `super()` Work with MRO?

The `super()` function allows a method to continue searching for the next implementation according to the MRO.

**Example:**

```python
class A:
    def show(self):
        print("A")
        super().show()


class B:
    def show(self):
        print("B")
        super().show()


class C(A, B):
    def show(self):
        print("C")
        super().show()


obj = C()
obj.show()
```

**Output:**

```text
C
A
B
```

**Explanation:**

The MRO for `C` is:

```text
C → A → B → object
```

1. `C.show()` prints `C`.
2. `super().show()` in `C` continues to `A.show()`.
3. `super().show()` in `A` continues to `B.show()`.
4. `B.show()` prints `B`.
5. `B` does not explicitly call `super().show()`, so the chain stops.

**Important:** `super()` does not simply mean "call my direct parent." It follows the next class in the MRO.

### 34.5 How to Check MRO in Python

Python provides two common ways to inspect the method resolution order.

**Using `mro()`:**

```python
print(C.mro())
```

**Using `__mro__`:**

```python
print(C.__mro__)
```

Both show the ordered sequence of classes Python searches.

### 34.6 Rules of Method Resolution Order

1. The child class is checked before its parent classes.
2. The declared order of base classes is respected.
3. A class appears only once in the resulting MRO.
4. The ordering must respect inheritance relationships.
5. If Python cannot construct a consistent MRO, it raises a `TypeError` when the class is defined.
6. `super()` follows the MRO rather than selecting a parent by name.

### 34.7 Advantages of MRO

- Makes method lookup predictable in multiple inheritance.
- Helps avoid inconsistent inheritance ordering.
- Supports cooperative multiple inheritance through `super()`.
- Ensures shared ancestors are handled consistently.
- Makes complex class hierarchies easier to inspect and debug.

### 34.8 Common Interview Questions

**Q1. What is MRO?**

MRO is the order Python follows to search for methods and attributes in a class hierarchy.

**Q2. Which algorithm does Python use for MRO?**

Python uses the C3 linearization algorithm.

**Q3. How can you check a class's MRO?**

Use `ClassName.mro()` or `ClassName.__mro__`.

**Q4. What happens if two parent classes define the same method?**

Python executes the first matching implementation found in the MRO.

**Q5. What is the diamond problem?**

It occurs when a class inherits from two classes that share a common ancestor. Python's MRO determines a consistent search order through that hierarchy.

**Q6. Does `super()` always call the immediate parent class?**

No. It calls the next implementation according to the current class's MRO.

### 34.9 Interview Summary

Method Resolution Order determines how Python searches for methods and attributes in an inheritance hierarchy. For multiple inheritance, Python uses C3 linearization to create a consistent order that respects the declared parent order and inheritance relationships. Use `mro()` or `__mro__` to inspect the order, and use `super()` for cooperative method calls that follow the MRO.

## 35. What can be used as keys in dictionary?
Any immutable object type can be used as dictionary key even functions and classes can also be used as dictionary keys. 
#### Why can't list or another dict(mutable object) be used as key in dictionary?
Dict implementation reduces the average complexity of dictionary lookups to O(1) by requiring that key objects provide a "hash" function. Such a hash function takes the information in a key object and uses it to produce an integer, called a hash value. This hash value is then used to determine which "bucket" this (key, value) pair should be placed into. Mutuable objects like list or dict cannot provide a valid /__hash__ method.

## 36. Explain shallow and deep copy in Python
For collections that are mutable or contain mutable items, a copy is sometimes needed so one can change one copy without changing the other. <br>
Python follows a pattern of compiling the original source to byte codes, then interpreting the byte codes on a virtual machine. The .pyc file generated contains byte code. 
```python
>>> import copy
>>> sample_1 = [1,2,3]
>>> id(sample_1)
139865052152768
>>> sample_2 = sample_1
>>> id(sample_2)
139865052152768
>>> sample_3 = copy.copy(sample_1)
>>> id(sample_3)
139865052236736
```
- A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
- A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.

Ref: [Python Docs Copy](https://docs.python.org/3/library/copy.html)

## 37. Why Python generates a .pyc file even when it is an interpreted language?
.pyc files are created by the Python interpreter when a .py file is imported, and they contain the "compiled bytecode" of the imported module/program, the idea being that the "translation" from source code to bytecode (which only needs to be done once) can be skipped on subsequent imports if the .pyc is newer than the corresponding .py file, thus speeding startup a little. But it's still interpreted.

## 38. How private varibles are declared in Python?
Python does not have anything called private member however by convention two underscore before a variable or function makes it private. 
```python
class XSpecial:
    normal_var = 10
    __private_var = 17

>>> special_obj = XSpecial()
>>> special_obj.normal_var
>>> special_obj.__private_var # AttributeError
```
## 39. Difference between an array and list
| List | Array | 
| :-------------:|:-------------:|
| Can contain elements of different data types | Contains homogeneous elements only i.e. same data type |
| No need to import | Need to import via numpy or array |
| Preferred for short sequence of data items | Preferred for large sequence of data items i.e., data analysis |
| Can't perform airthmetic operations on whole list | Great for airthmetic operations |

## 40. What is an iterator? How is iterator is different from a generator? 
An iterator is an object that implements /__next__, which is expected to return the next element of the iterable object, and raise a StopIteration exception when no more elements are available.
### Differnce between iterator and generator
| Iterator | Generator | 
| :-------------:|:-------------:|
| Class is used to implement an iterator | Function is used to implement a generator |
| Iterator uses iter() and next() functions | Generator uses yield keyword |
| Every iterator is not a generator | Every generator is an iterator |
| Saves the states of local variables every time ‘yield’ pauses execution | An iterator does not make use of local variables |
| Memory efficient | More memory allocated than iterator |

## 41. How do you define a dict where several keys has same value?
```python
products = {}
products.update(
    dict.keys(['Apple','Mango','Oranges'], 20)
)
products.update(
    dict.keys(['Pizza','Kind Pizza','Bad Pizza'], 30)
)
```
## 42. What are different types of namespaces in Python?
Namespace is a way to implement scope. In Python, each package, module, class, function and method function owns a "namespace" in which variable names are resolved. Plus there's a global namespace that's used if the name isn't in the local namespace.<br>
Each variable name is checked in the local namespace (the body of the function, the module, etc.), and then checked in the global namespace.
### Types of Namespaces
- <b>Local Namespace: </b>The local namespace for a function is created when the function is called, and deleted when the function returns or raises an exception that is not handled within the function. 
- <b>Global Namespace: </b>The global namespace for a module is created when the module definition is read in; normally, module namespaces also last until the interpreter quits.
- <b>Built-in Namespace: </b>The namespace containing the built-in names is created when the Python interpreter starts up, and is never deleted.

## 43. How can you access attribute of parent class bypassing the attribute with the same name in derived class?
```python
class Parent:
    variable = 12
    
class Derived(Parent):
    variable = 10

Parent.variable # returns 12
```

## 44. Evaulation of boolean expressions
- The expression x and y first evaluates x; if x is false, its value is returned; otherwise, y is evaluated and the resulting value is returned.
- The expression x or y first evaluates x; if x is true, its value is returned; otherwise, y is evaluated and the resulting value is returned.
```python
x = 'Some Value'
y = 24
z = False
x or y # returns x
z or y # returns y
x and y # returns y
z and x # returns z
```

## 45. Difference between multiprocessing and multithreading
The threading module uses threads, the multiprocessing module uses processes. The difference is that threads run in the same memory space, while processes have separate memory. This makes it a bit harder to share objects between processes with multiprocessing. Since threads use the same memory, precautions have to be taken or two threads will write to the same memory at the same time. 
- Multithreading is concurrent and is used for IO-bound tasks
- Multiprocessing achieves true parallelism and is used for CPU-bound tasks
Use Multithreading if most of your task involves waiting on API-calls, because why not start up another request in another thread while you wait, rather than have your CPU sit idly by. 

## 46. How to merge two dictionaries together?
```python
first_dict = {'name': 'Tom', 'age': 44}
second_dict = {'occupation': 'actor', 'nationality': 'British'}
# merging
final_dict = {**first_dict, **second_dict}
```
In case any key is repeated in both dictionaries, the second key will hold supremacy. 


## 47. How do you overload a Python constructor?

### 1. What is Constructor Overloading?

Constructor overloading means defining multiple constructors with different parameter lists so that an object can be initialized in different ways.

In languages such as Java and C++, we can define multiple constructors with different parameter lists.

**Python does not support traditional constructor overloading directly.** A Python class generally has one `__init__()` method. If we define multiple `__init__()` methods, the last definition overrides the previous ones.

However, we can achieve similar behavior using:
1. Default arguments
2. Variable-length arguments (`*args` and `**kwargs`)
3. Class methods as alternative constructors
4. Type checking and conditional logic

---

### 2. Example: Python Does Not Support Traditional Constructor Overloading

```python
class Employee:
    def __init__(self):
        print("Default constructor")

    def __init__(self, name):
        print(f"Employee name: {name}")


# Creating objects
emp1 = Employee()
emp2 = Employee("Shiv")
```

**Output:**

```text
TypeError: Employee.__init__() missing 1 required positional argument: 'name'
```

**Explanation:**

Python keeps only the last `__init__()` definition. The first constructor is overwritten, so calling `Employee()` raises a `TypeError`.

---

### 3. Approach 1: Using Default Arguments

We can provide default values for constructor parameters to support different initialization scenarios.

```python
class Employee:
    def __init__(self, name=None, salary=0):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


# Different initialization scenarios
emp1 = Employee()
emp2 = Employee("Shiv")
emp3 = Employee("Rahul", 50000)

emp1.display()
emp2.display()
emp3.display()
```

**Output:**

```text
Name: None, Salary: 0
Name: Shiv, Salary: 0
Name: Rahul, Salary: 50000
```

**Explanation:**

- `Employee()` initializes an employee with default values.
- `Employee("Shiv")` initializes an employee with a name.
- `Employee("Rahul", 50000)` initializes an employee with both name and salary.

This is one of the simplest ways to simulate constructor overloading in Python.

---

### 4. Approach 2: Using `*args`

The `*args` parameter allows a constructor to accept a variable number of positional arguments.

```python
class Calculator:
    def __init__(self, *args):
        self.numbers = args

    def calculate_sum(self):
        return sum(self.numbers)


c1 = Calculator(10)
c2 = Calculator(10, 20)
c3 = Calculator(10, 20, 30)

print(c1.calculate_sum())
print(c2.calculate_sum())
print(c3.calculate_sum())
```

**Output:**

```text
10
30
60
```

**Explanation:**

- `*args` collects positional arguments into a tuple.
- The constructor accepts one, two, three, or more numbers.
- The method processes the collected arguments.

You can also check the number of arguments to perform different initialization logic.

```python
class Example:
    def __init__(self, *args):
        if len(args) == 0:
            print("Initialized without arguments")
        elif len(args) == 1:
            print(f"Initialized with one argument: {args[0]}")
        elif len(args) == 2:
            print(f"Initialized with two arguments: {args[0]}, {args[1]}")
        else:
            raise TypeError("Unsupported number of arguments")


Example()
Example(10)
Example(10, 20)
```

**Output:**

```text
Initialized without arguments
Initialized with one argument: 10
Initialized with two arguments: 10, 20
```

---

### 5. Approach 3: Using `**kwargs`

The `**kwargs` parameter allows a constructor to accept a variable number of keyword arguments.

```python
class Employee:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "Unknown")
        self.salary = kwargs.get("salary", 0)
        self.department = kwargs.get("department", "General")

    def display(self):
        print(
            f"Name: {self.name}, "
            f"Salary: {self.salary}, "
            f"Department: {self.department}"
        )


emp1 = Employee(name="Shiv")
emp2 = Employee(name="Rahul", salary=50000)
emp3 = Employee(
    name="Priya",
    salary=60000,
    department="Engineering"
)

emp1.display()
emp2.display()
emp3.display()
```

**Output:**

```text
Name: Shiv, Salary: 0, Department: General
Name: Rahul, Salary: 50000, Department: General
Name: Priya, Salary: 60000, Department: Engineering
```

**Explanation:**

- `**kwargs` collects keyword arguments into a dictionary.
- `.get()` allows us to provide default values.
- This approach is useful when an object has many optional configuration parameters.

---

### 6. Approach 4: Using Class Methods as Alternative Constructors

Class methods are useful when we need multiple meaningful ways to create an object from different kinds of input.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_name(cls, name):
        return cls(name, 0)

    @classmethod
    def from_string(cls, employee_data):
        name, salary = employee_data.split(",")
        return cls(name, int(salary))

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


# Standard initialization
emp1 = Employee("Shiv", 50000)

# Alternative initialization using a class method
emp2 = Employee.from_name("Rahul")

# Alternative initialization from a string
emp3 = Employee.from_string("Priya,60000")

emp1.display()
emp2.display()
emp3.display()
```

**Output:**

```text
Name: Shiv, Salary: 50000
Name: Rahul, Salary: 0
Name: Priya, Salary: 60000
```

**Explanation:**

- `__init__()` remains the single initializer.
- `from_name()` creates an employee using only a name.
- `from_string()` parses a string before creating an employee.
- `cls` refers to the class, allowing the class method to create an instance.

This approach is often cleaner than putting many unrelated conditions inside `__init__()`.

---

### 7. Comparison of Different Approaches

| Approach | Best use case |
|---|---|
| Default arguments | A few optional parameters |
| `*args` | A variable number of positional arguments |
| `**kwargs` | Optional named parameters or configurations |
| Class methods | Different, clearly named object-creation processes |
| Type checking | Initialization behavior depends on the input type |

---

### 8. Real-World Example in Backend Development

In a Python backend application, we might need to create configuration objects using default settings or environment-specific values.

```python
class DatabaseConfig:
    def __init__(
        self,
        host="localhost",
        port=5432,
        database="app_db"
    ):
        self.host = host
        self.port = port
        self.database = database

    @classmethod
    def for_testing(cls):
        return cls(
            host="localhost",
            port=5433,
            database="test_db"
        )


# Default configuration
config1 = DatabaseConfig()

# Custom configuration
config2 = DatabaseConfig(
    host="db.example.com",
    port=5432,
    database="production_db"
)

# Testing configuration
config3 = DatabaseConfig.for_testing()
```

This pattern is useful for database settings, application configuration, API clients, and test fixtures.

---

### 9. Common Interview Questions

**Q1. Does Python support constructor overloading?**

No. Python does not support traditional constructor overloading with multiple `__init__()` definitions. We can simulate similar behavior using default arguments, `*args`, `**kwargs`, or class methods.

**Q2. What happens if we define two `__init__()` methods in one class?**

The last definition replaces the earlier one in the class namespace.

**Q3. What is the difference between constructor overloading and method overriding?**

- **Overloading:** Providing multiple implementations with different parameter lists. Python does not support traditional constructor overloading directly.
- **Overriding:** A child class provides its own implementation of a method inherited from its parent class.

**Q4. Which approach is best for alternative constructors?**

Use class methods when each creation method has a distinct purpose, such as creating an object from a dictionary, a string, or a database record.

**Q5. Can `__init__()` return a value?**

No. `__init__()` must return `None`. Returning another value causes a `TypeError`.

---

### 10. Key Takeaways

- Python does not support traditional constructor overloading.
- Only the last definition of `__init__()` remains available when multiple definitions are written in the same class.
- Default arguments are suitable for simple variations.
- `*args` and `**kwargs` support flexible input.
- Class methods provide readable alternative constructors.
- Choose the simplest approach that makes object creation clear and maintainable.


## 48. Explain the below code
```python
def func(sample_list=[]):
    sample_list.append(12)
    # print(id(sample_list))
    return sample_list

print(func()) # [12]
print(func()) # [12,12]
```
 Since list is mutualable type of data structure, the first time func is called, the list is empty, but when the same function is called twice, the list already has an item. We cans sure of the that by printing the id of the sample_list used in the first, on each subsquent call to the function, the id will return the same value. 
 
 ## 49. Example filter with lambda expression.
 ### filter
 filter(function, iterable) # function must return True or False
 ```python
 input_list = ['Delhi', 'Mumbai', 'Noida', 'Gurugram']
 to_match = 'Gurugram'
 
 matched_list = list(filter(lambda item: item == to_match, input_list))
 matched_list # ['Gurugram']
 ```
For every single item in the input_list, the condition is checked in the lambda function which returns either True or False.

## 50. Explain context managers.
- A context manager in Python is a protocol implemented using the with statement.
- It allows you to perform setup and teardown operations around a block of code.
- Commonly used to manage resources like files, database connections, locks, etc.

```python
class MyContextManager:
    def __enter__(self):
        # Perform setup operations
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Perform cleanup operations

# Using the context manager
with MyContextManager() as cm:
    # Code inside the context
```