def func(x):
    return x + 1

def multiplication(a, b):
    return a * b

# Function price_calculation should return a price for a ticket.
# If someone is young enough (<20) it should be 100
# If someone is 20 exactly it should be 120
# If someone is 21 or more but less than 65 it should be 150
# If someone is older than 65 or 65 exactly it should be 200
# An age is 0 or more but not less. The function should return None if age < 0

def price_calculation(age):
    if(age >= 0):
        if(age < 20):
            return 100
        elif(age == 20):
            return 120
        elif(20 < age < 65):
            return 150
        else:
            return 200
    else:
        return None
