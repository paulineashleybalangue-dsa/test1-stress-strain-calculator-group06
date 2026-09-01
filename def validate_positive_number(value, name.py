def validate_positive_number(value: float, name: str) -> float:
    """
    checks if a number is greater than zero (⋟﹏⋞)

    arguments:
        value: the number being checked.
        name: the name of the input being checked.

    returns:
        The validated number.

    raises:
        ValueError: if the number is zero or negative.
    """
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero.")
    return value


def validate_non_zero(value: float, name: str) -> float:
    """
    checks if a number is not zero (◡‿◡✿)

    arguments:
        value: the number being checked.
        name: the name of the input being checked.

    returns:
        The validated number.

    raises:
        ValueError: if the number is zero.
    """
    if value == 0:
        raise ValueError(f"{name} cannot be zero.")
    return value


def get_validated_input(prompt: str, validator_func, name: str) -> float:
    """
    gets a valid number from the user (｡•ᴗ•｡)

    arguments:
        prompt: the message shown to the user.
        validator_func: the function used to validate the input.
        name: the name of the input being checked.

    returns:
        a validated number.
    """
    while True:
        try:
            value = float(input(prompt))
            return validator_func(value, name)
        except ValueError as error:
            print(f"Invalid input: {error} :(")

def create_calculation_record(
    material: str,
    inputs: dict,
    results: dict
) -> dict:
    """
    creates a dictionary for one calculation ٩(๑❛ᴗ❛๑)۶

    arguments:
        material: the material used in the calculation.
        inputs: the input values used for the calculation.
        results: the calculated results.

    returns:
        A dictionary containing the material, inputs, and results.
    """
    return {
        "material": material,
        "inputs": inputs,
        "results": results
    }


def add_to_history(history_list: list, record: dict) -> None:
    """
    adds a calculation record to the history ✧(⸝⸝⸝ᵒ̴̶̷ ｡ ᵒ̴̶̷⸝⸝⸝)

    arguments:
        history_list: the list containing calculation records.
        record: the calculation record to add.

    returns:
        None.
    """
    history_list.append(record)


def get_materials_database() -> dict:
    """
    returns the materials properties dictionary ^‿^

    returns:
        A dictionary containing the available materials
        and their properties.
    """
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

def get_material_properties(
    material_name: str,
    database: dict
) -> dict:
    """
    gets the properties of a selected material ≽^•⩊•^≼

    arguments:
        material_name: the name of the material.
        database: the materials properties dictionary.

    returns:
        A dictionary containing the material properties.

    raises:
        ValueError: if the material is not found.
    """
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