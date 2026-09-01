def validate_positive_number(value, name):
    """
    checks if a number is greater than zero ♡

    arguments:
        value: the number being checked.
        name: the name of the input being checked.

    returns:
        the validated number.

    raises:
        ValueError: if the number is zero or negative.
    """
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero.")
    return value


def validate_non_zero(value, name):
    """
    checks if a number is not zero ♡

    arguments:
        value: the number being checked.
        name: the name of the input being checked.

    returns:
        the validated number.

    raises:
        ValueError: if the number is zero.
    """
    if value == 0:
        raise ValueError(f"{name} cannot be zero.")
    return value


def get_validated_input(prompt, validator_func, name):
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


def create_calculation_record(material, inputs, results):
    """
    creates a dictionary for one calculation ♡

    arguments:
        material: the material used in the calculation.
        inputs: the input values used for the calculation.
        results: the calculated results.

    returns:
        a dictionary containing the material, inputs, and results.
    """
    return {
        "material": material,
        "inputs": inputs,
        "results": results
    }


def add_to_history(history_list, record):
    """
    adds a calculation record to the history ♡

    arguments:
        history_list: the list containing calculation records.
        record: the calculation record to add.

    returns:
        None.
    """
    history_list.append(record)


def get_materials_database():
    """
    returns the materials properties dictionary ♡

    returns:
        a dictionary containing the available materials
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


def get_material_properties(material_name, database):
    """
    gets the properties of a selected material ♡

    arguments:
        material_name: the name of the material.
        database: the materials properties dictionary.

    returns:
        a dictionary containing the material properties.

    raises:
        ValueError: if the material is not found.
    """
    material_name = material_name.lower()

    if material_name not in database:
        raise ValueError("material not found :(")

    return database[material_name]


def display_material_menu(database):
    """
    displays the available materials (｡•̀ᴗ-)✧

    arguments:
        database: the materials properties dictionary.

    returns:
        None.
    """
    print("\navailable materials:")

    for material in database:
        print(f"- {material.title()}")


def display_calculation_results(record):
    """
    displays the results of a calculation ♡

    arguments:
        record: the calculation record containing the material,
            inputs, and results.

    returns:
        None.
    """
    material = record["material"]
    inputs = record["inputs"]
    results = record["results"]

    print("\n== Calculation Results ==")
    print("-------------------")
    print(f"Material: {material.title()}")
    print(f"Force: {inputs['force']:.2f} n")
    print(f"Area: {inputs['area']:.4f} m^2")
    print(f"Original Length: {inputs['original_length']:.4f} m")
    print(f"Change in Length: {inputs['change_in_length']:.4f} m")
    print(f"Stress: {results['stress']:.2f} pa")
    print(f"Strain: {results['strain']:.6f}")
    print(f"Young's Modulus: {results['youngs_modulus']:.2f} pa")
    print(f"Factor of Safety: {results['factor_of_safety']:.2f}")


def display_safety_analysis(stress, yield_strength, safety_factor):
    """
    displays the safety analysis ♡

    arguments:
        stress: the calculated stress.
        yield_strength: the material's yield strength.
        safety_factor: the calculated factor of safety.

    returns:
        None.
    """
    print("\n== Safety Analysis ==")
    print("----------------")
    print(f"Stress: {stress:.2f} pa")
    print(f"Yield Strength: {yield_strength:.2f} pa")
    print(f"Factor of Safety: {safety_factor:.2f}")

    if safety_factor >= 1:
        print("the material is within the safe range ✓")
    else:
        print("warning: the material may not be safe :(")


def display_session_summary(history, unique_materials):
    """
    displays a summary of the current session (˶ᵔ ᵕ ᵔ˶)

    arguments:
        history: the list of calculation records.
        unique_materials: the materials used during the session.

    returns:
        None.
    """
    print("\n== Session Summary ==")
    print("----------------")
    print(f"Total Calculations: {len(history)}")

    if unique_materials:
        print(f"Materials Used: {', '.join(unique_materials)}")
    else:
        print("Materials Used: none")