def validate_positive_number(value, name):
    """checks if a number is greater than zero ♡"""
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero.")
    return value


def validate_non_zero(value, name):
    """checks if a number is not zero ♡"""
    if value == 0:
        raise ValueError(f"{name} cannot be zero.")
    return value

def get_validated_input(prompt, name):
    """gets a valid number from the user (｡•ᴗ•｡)"""
    while True:
        try:
            value = float(input(prompt))
            validate_positive_number(value, name)
            return value
        except ValueError as error:
            print(f"invalid input: {error} :(")