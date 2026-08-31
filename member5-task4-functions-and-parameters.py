def validate_input(force, area, original_lenght, change_in_lenght):
    """Validate that all input values are appropriate for calculations."""
    if force < 0:
        raise ValueError("Force must be a positive value.")
    if area <= 0:
        raise ValueError("Area must be a positive value.")
    if original_lenght <= 0:
        raise ValueError("Original lenght must be a positive value.")
    if change_in_lenght < 0:
        raise ValueError("Change in lenght must be a positive value.")
    return True

def calculate_stress(force, area):
    """Calculate stress based on force and area."""
    if area == 0:
        raise ValueError("Area cannot be zero.")
    return force / area

def calculate_strain(original_lenght, change_in_lenght):
    """Calculate strain based on original lenght and change in lenght."""
    if original_lenght == 0:
        raise ValueError("Original lenght cannot be zero.")
    return change_in_lenght / original_lenght

def calculate_youngs_modulus(stress, strain):
    """Calculate Young's modulus from stress and strain."""
    if strain == 0:
        raise ValueError("Strain cannot be zero.")
    return stress / strain

def calculate_factor_of_safety(yield_strength, stress):
    """Calculate the factor of safety from yield strength and stress."""
    if stress <= 0:
        raise ValueError("Stress value cannot be zero.")
    if yield_strength <= 0:
        raise ValueError("Yield strength must be a positive value.")
    return yield_strength / stress

def main_calculator(materials, force, area, original_lenght, change_in_lenght, yield_strength):
    """"Main function orchestrate the stress-strain calculations."""
    validate_input(force, area, original_lenght, change_in_lenght)

    stress = calculate_stress(force, area)
    strain = calculate_strain(original_lenght, change_in_lenght)
    youngs_modulus = calculate_youngs_modulus(stress, strain)
    factor_of_safety = calculate_factor_of_safety(yield_strength, stress)
    return {
        "materials": materials,
        "force": force,
        "area": area,
        "original_lenght": original_lenght,
        "change_in_lenght": change_in_lenght,
        "stress": stress,
        "strain": strain,
        "youngs_modulus": youngs_modulus,
        "yield_strength": yield_strength,
        "factor_of_safety": factor_of_safety
    }