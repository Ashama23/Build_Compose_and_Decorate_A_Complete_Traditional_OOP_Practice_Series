def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")
print("About to call the decorated function...")
say_hello()
print("Function call is complete.")