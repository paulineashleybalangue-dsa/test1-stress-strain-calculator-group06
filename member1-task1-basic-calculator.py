def main():
    """Main function for the stress and strain calculator."""

    # Print a header
    print("=== Stress and Strain Calculator ===")
    print()

    # Get user input 
    force = float(input("Enter applied force (N): "))
    area = float(input("Enter cross-sectional area (m^2): "))
    original_length = float(input("Enter original length (m): "))
    change_in_length = float(input("Enter change in length (m): "))

    stress = force / area
    strain = change_in_length / original_length

    # Display the input 
    print()
    print("=== RESULTS ===")
    print(f"Applied Force:         {force:.2f} N")
    print(f"Cross-sectional Area:  {area:.4f} m^2")
    print(f"Original Length:       {original_length:.4f} m")
    print(f"Change in Length:      {change_in_length:.6f} m")

    print()

    # Display results
    print(f"Stress:                {stress:.2f} Pa")
    print(f"Strain:                {strain:.6f}")

    print()

    # BONUS
    stress_mpa = stress / 1_000_000
    print(f"Stress in MPa:         {stress_mpa:.4f} MPa")

    if change_in_length > 0:
        loading_type = "Tension"
    elif change_in_length < 0:
        loading_type = "Compression"
    else:
        loading_type = "No deformation"

    print(f"Loading Type:          {loading_type}")

    print()
    print("=== Analysis Complete ===")


# Python execution pattern
if _name_ == "_main_":
    main()