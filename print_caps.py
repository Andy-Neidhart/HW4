def allcaps(func):
    def wrapper():
        # Get the result from the original function
        result = func()
        # Capitalize the result and return it
        return result.upper()
    return wrapper
