def validate_positive_number(value: float, name: str) -> float:
    """
    checks if a number is greater than zero ♡

    Arguments:
        value: the number being checked.
        name: the name of the input being checked.

    Returns:
        The validated number.

    Raises:
        ValueError: if the number is zero or negative.
    """
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero.")
    return value


def validate_non_zero(value: float, name: str) -> float:
    """
    checks if a number is not zero ♡

    Arguments:
        value: the number being checked.
        name: the name of the input being checked.

    Returns:
        The validated number.

    Raises:
        ValueError: if the number is zero.
    """
    if value == 0:
        raise ValueError(f"{name} cannot be zero.")
    return value


def get_validated_input(prompt: str, validator_func, name: str) -> float:
    """
    gets a valid number from the user (｡•ᴗ•｡)

    Arguments:
        prompt: the message shown to the user.
        validator_func: the function used to validate the input.
        name: the name of the input being checked.

    Returns:
        A validated number.
    """
    while True:
        try:
            value = float(input(prompt))
            return validator_func(value, name)
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

def display_material_menu(database):
    """display the available materials (｡•̀ᴗ-)✧"""
    print("\navailable materials:")

    for material in database:
        print(f"- {material.title()}")


def display_calculation_results(record):
    """display the results of a calculation ♡"""
    inputs = record["inputs"]
    results = record["results"]

    print("\ncalculation results")
    print("-------------------")
    print(f"material: {record['material'].title()}")
    print(f"force: {inputs['force']:.2f} n")
    print(f"area: {inputs['area']:.4f} m^2")
    print(f"original length: {inputs['original_length']:.4f} m")
    print(f"change in length: {inputs['change_in_length']:.4f} m")
    print(f"stress: {results['stress']:.2f} pa")
    print(f"strain: {results['strain']:.6f}")
    print(f"young's modulus: {results['youngs_modulus']:.2f} pa")
    print(f"factor of safety: {results['factor_of_safety']:.2f}")


def display_safety_analysis(stress, yield_strength, safety_factor):
    """display the safety analysis ♡"""
    print("\nsafety analysis")
    print("----------------")
    print(f"stress: {stress:.2f} pa")
    print(f"yield strength: {yield_strength:.2f} pa")
    print(f"factor of safety: {safety_factor:.2f}")

    if safety_factor >= 1:
        print("the material is within the safe range ✓")
    else:
        print("warning: the material may not be safe :(")


def display_session_summary(history, unique_materials):
    """display a summary of the current session (˶ᵔ ᵕ ᵔ˶)"""
    print("\nsession summary")
    print("----------------")
    print(f"total calculations: {len(history)}")

    if unique_materials:
        print(f"materials used: {', '.join(unique_materials)}")
    else:
        print("materials used: none")