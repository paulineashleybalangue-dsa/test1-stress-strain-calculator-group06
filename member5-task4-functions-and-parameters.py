def validate_input(force, area, original_lenght, change_in_lenght):
    if force < 0:
        raise ValueError("Force must be a positive value.")
    if area <= 0:
        raise ValueError("Area must be a positive value.")
    if original_lenght <= 0:
        raise ValueError("Original lenght must be a positive value.")