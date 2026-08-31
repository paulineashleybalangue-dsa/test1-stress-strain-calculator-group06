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
