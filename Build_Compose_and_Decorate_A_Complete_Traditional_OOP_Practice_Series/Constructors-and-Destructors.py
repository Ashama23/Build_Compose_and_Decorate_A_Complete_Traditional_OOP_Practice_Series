import time

class Logger:
    def __init__(self, name):
        self.name = name
        print(f"Object '{self.name}' created.")

    def __del__(self):
        print(f"Object '{self.name}' is being destroyed.")

def create_and_destroy_object():
    print("Entering the function.")
    log_obj = Logger("MyLogger")
    print("Object created. The function will now end, and the object will go out of scope.")

print("Starting the demonstration.")
create_and_destroy_object()
print("Demonstration finished.")

print("\n--- Manual Deletion Demonstration ---")
another_log = Logger("AnotherLogger")
print("Explicitly deleting the object.")
del another_log
print("Manual deletion complete.")