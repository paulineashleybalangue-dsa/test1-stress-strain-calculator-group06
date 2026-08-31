# Part 3: Data Structures - Stress and Strain Calculator Template
# TODO: Complete this template by implementing data structures


def main():
    """Main function for the stress and strain calculator with data structures."""

    print("=== Stress and Strain Calculator - Session Manager ===")
    print()

    # TODO: Initialize empty list for calculation history
    calculation_history = []

    # TODO: Initialize empty set for unique materials
    unique_materials = set()

    # TODO: Create tuple for measurement units (N, m², m, Pa)
    units = ("N", "m²", "m", "Pa")

    # TODO: Create materials database dictionary with at least 3 materials
    # Each material should have yield_strength and youngs_modulus

    materials = {
        "1": {
            "name": "Steel", 
            "yield_strength": 250_000_000, 
            "youngs_modulus": 200_000_000_000},
        "2": {
            "name": "Aluminum", 
            "yield_strength": 95_000_000, 
            "youngs_modulus": 69_000_000_000},
        "3": {
            "name": "Titanium", 
            "yield_strength": 880_000_000, 
            "youngs_modulus": 114_000_000_000}}

    # Main calculation loop
    while True:

        # TODO: Display available materials
        print("\n=== Intelligent Stress and Strain Calculator ===")
        print("1. Steel")
        print("2. Aluminum")
        print("3. Titanium")
        print("4. Custom Material")
        print("5. Exit Program")

        # TODO: Get material selection from user
        choice = input("Select a material option (1-5): ").strip()

        # TODO: Check if user wants to quit
        if choice == "5":
            print("\nExiting program gracefully. Goodbye!")
            break

        # TODO: Validate material exists in database
        if choice in materials:
            selected_material = materials[choice]["name"]
            yield_strength = materials[choice]["yield_strength"]
            youngs_modulus = materials[choice]["youngs_modulus"]
        else:
            # Custom material
            selected_material = input("Enter custom material name: ").strip()

            if not selected_material:
                selected_material = "Custom Material"
        
        try:
            # TODO: Get input values (force, area, original_length, change_in_length)
            force = float(input("Enter applied force (N): "))
            area = float(input("Enter cross-sectional area (m^2): "))
            original_length = float(input("Enter original length (m): "))
            change_in_length = float(input("Enter change in length (m): "))

            # TODO: Validate inputs (positive values, non-zero where needed)
            if force < 0:
                print("Force cannot be negative!")
                continue

            if area <= 0:
                print(
                    "Cross-sectional area must be greater than zero "
                    "(prevents division error)!"
                )
                continue

            if original_length <= 0:
                print(
                    "Original length must be greater than zero "
                    "(prevents division error)!"
                )
                continue

            if change_in_length < 0:
                print("Change in length cannot be negative!")
                continue

            # TODO: Calculate stress and strain
            stress = force / area
            strain = change_in_length / original_length
            stress_mpa = stress / 1_000_000
            
            # TODO: Get material properties from database
            if choice in materials:
                yield_strength = materials[choice]["yield_strength"]
                youngs_modulus = materials[choice]["youngs_modulus"]
                
            # TODO: Calculate safety factor
            factor_of_safety = yield_strength / stress if stress > 0 else float("inf")

            if stress < yield_strength:
                if factor_of_safety < 1.2:
                    safety_status = f"CAUTION - Factor of safety: {factor_of_safety:.2f}"
                else:
                    safety_status = f"SAFE - Factor of safety: {factor_of_safety:.2f}"
            else:
                safety_status = (
                    f"CRITICAL FAILURE RISK - Stress exceeds Yield Strength! "
                    f"(FOS: {factor_of_safety:.2f})"
                )

            # TODO: Create calculation record dictionary with all data
            calculation_record = {
                "material": selected_material,
                "force": force,
                "area": area,
                "original_length": original_length,
                "change_in_length": change_in_length,
                "stress": stress,
                "strain": strain,
                "stress_mpa": stress_mpa,
                "yield_strength": yield_strength,
                "youngs_modulus": youngs_modulus,
                "factor_of_safety": factor_of_safety,
                "safety_status": safety_status
            }

            # TODO: Add record to history list
            calculation_history.append(calculation_record)

            # TODO: Add material to unique materials set
            unique_materials.add(selected_material)

            # TODO: Display results for this calculation
            print("\n" + "=" * 20 + " RESULTS " + "=" * 20)
            print(f"Material Profile      : {selected_material}")
            print(f"Applied Force         : {force:,.2f} N")
            print(f"Cross-sectional Area  : {area:.6f} m^2")
            print(f"Original Length       : {original_length:,.4f} m")
            print(f"Change in Length      : {change_in_length:,.6f} m")
            print("-" * 49)
            print(f"Calculated Stress     : {stress:,.2f} Pa ({stress_mpa:.4f} MPa)")
            print(f"Calculated Strain     : {strain:.6f}")
            print(f"Factor of Safety      : {factor_of_safety:.2f}")
            print(f"ANALYSIS REPORT       : {safety_status}")
            print("=" * 49)
            
            pass

        except ValueError:
            print("Error: Invalid input. Please enter numeric values.")
        except ZeroDivisionError:
            print("Error: Area and original length cannot be zero!")
        except KeyError:
            print("Error: Material not found in database!")

    # TODO: Display session summary
    # - Total number of calculations
    # - List of unique materials tested
    # - Detailed history of each calculation


    # TODO: Display statistics (optional)
    # - Highest stress
    # - Lowest safety factor
    # - Average strain
    # - Material test counts
    


# Standard Python execution pattern
if __name__ == "__main__":
    main()