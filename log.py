# log.py
import time

# Decorator function
def timestamp(func):
    def wrapper(*args, **kwargs):
        # Print the current time
        print(time.ctime())
        # Call the original function and print its output
        result = func(*args, **kwargs)
        print("Result:", result)
        return result
    return wrapper
