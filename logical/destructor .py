# In Python, a destructor is a special method called __del__() that is invoked when an object is about to be destroyed. 
# While commonly referred to as a destructor, the official Python documentation more precisely describes it as a finalizer

class FileManager:
    def __init__(self, filename):
        print(f"Opening file: {filename}")
        self.filename = filename

    def __del__(self):
        print(f"Closing file: {self.filename}")


fm = FileManager("data1")
fm1 = fm

del fm  # Destructor is NOT called here because fm1 still references it.

del fm1  # Destructor IS called here because reference count hits 0.

    