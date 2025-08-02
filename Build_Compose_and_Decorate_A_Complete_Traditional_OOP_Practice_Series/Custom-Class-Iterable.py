class Countdown:
    def __init__(self, start):
        self.current = start
        print(f"Countdown initialized to start from {start}.")

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            num = self.current
            self.current -= 1
            return num
my_countdown = Countdown(5)
print("\nStarting the countdown loop:")

for number in my_countdown:
    print(number)

print("Countdown finished!")