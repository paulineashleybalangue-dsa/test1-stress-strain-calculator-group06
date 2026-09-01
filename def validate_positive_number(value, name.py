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
            print(f"Invalid input: {error} :(")

def create_calculation_record(material, inputs, results):
    """create a dictionary for one calculation ♡"""
    return {
        "material": material,
        "inputs": inputs,
        "results": results
    }

def add_to_history(history_list, record):
    """add a calculation record to the history ♡"""
    history_list.append(record)

def get_materials_database():
    """return the materials properties dictionary ♡"""
    return {
        "steel": {
            "yield_strength": 250000000
        },
        "aluminum": {
            "yield_strength": 150000000
        },
        "concrete": {
            "yield_strength": 20000000
        }
    }

def get_material_properties(material_name, database):
    """get the properties of a selected material ♡"""
    material_name = material_name.lower()

    if material_name not in database:
        raise ValueError("material not found :(")

    return database[material_name]