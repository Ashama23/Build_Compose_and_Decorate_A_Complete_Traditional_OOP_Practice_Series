class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid Age: {age}. Age must be 18 or older.")
    else:
        print(f"Age is valid: {age}")

ages_to_test = [25, 16, 30, 17]

for age_to_test in ages_to_test:
    try:
        print(f"\nChecking age: {age_to_test}")
        check_age(age_to_test)
    except InvalidAgeError as e:
        print(f"Error caught: {e}")