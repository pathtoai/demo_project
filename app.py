#   This is a test app
print("Hello World")

def calculate_simple_interest(principal, rate, time):
    """
    Calculates the simple interest
    """
    return (principal * rate * time) / 100


def calculate_compound_interest(principal, rate, time, periods):
    """
    Calculates the compound interest
    """
    return (principal * ((1 + rate / periods) ** (periods * time)) - principal)


# Running the functions
print(f"Simple Interest: {calculate_simple_interest(1000, 8, 2)}")
print(f"Compound Interest: {calculate_compound_interest(1000, 0.08, 2, 4)}")
