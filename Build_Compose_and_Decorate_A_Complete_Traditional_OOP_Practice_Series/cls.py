class Counter:
    object_count = 0

    def __init__(self):
        Counter.object_count += 1
        print(f"Object #{Counter.object_count} created.")

    @classmethod
    def display_count(cls):
        print("-------------------------------------")
        print(f"Total number of Counter objects created: {cls.object_count}")
        print("-------------------------------------")

if __name__ == "__main__":

    print("Checking the count before creating any objects...")
    Counter.display_count()
    print("\nCreating three Counter objects...")
    c1 = Counter()
    c2 = Counter()
    c3 = Counter()
    print("\nChecking the count after creating objects...")
    Counter.display_count()
    print("\nCalling the class method from an instance (c2)...")
    c2.display_count()