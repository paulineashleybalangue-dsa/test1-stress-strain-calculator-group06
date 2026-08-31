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
        print("Type 'q' or 'quit' at any prompt to exit back to menu")

        # TODO: Get material selection from user
        choice = input("Select a material option (1-5): ").strip()

        # TODO: Check if user wants to quit
        if choice.lower() in ["5", "q", "quit"]:
            print("\nExiting program. Goodbye!")
            break

        # TODO: Validate material exists in database
        if choice not in ["1", "2", "3", "4"]:
            print("[Invalid Choice] Please select an option between 1 and 5.")
            continue    

        if choice in materials:
            selected_material = materials[choice]["name"]
            yield_strength = materials[choice]["yield_strength"]
            youngs_modulus = materials[choice]["youngs_modulus"]
            
        else:
            selected_material = input("Enter custom material name: ").strip()
            if  selected_material.lower() in ["q", "quit"]:
                continue
            if not selected_material:
                selected_material = "Custom Material"
            
            # Validate Custom Material Inputs
            exit_to_menu = False
            while True:
                try:
                    ys_raw = input("Enter Custom Yield Strength (MPa): ").strip()
                    if ys_raw.lower() in ["q", "quit"]:
                        exit_to_menu = True
                        break
                    ys_input = float(ys_raw)
                    if ys_input <= 0:
                        print("Yield strength must be positive!")
                        continue
                    yield_strength = ys_input * 1_000_000  # Convert MPa to Pa
                    break
                except ValueError:
                    print("Please enter a valid number for Yield Strength!")

            if exit_to_menu:
                continue
            
            while True:
                try:
                    ym_raw = input("Enter Custom Young's Modulus (GPa): ").strip()
                    if ym_raw.lower() in ["q", "quit"]:
                        exit_to_menu = True
                        break
                    ym_input = float(ym_raw)
                    if ym_input <= 0:
                        print("Young's Modulus must be positive!")
                        continue
                    youngs_modulus = ym_input * 1_000_000_000  # Convert GPa to Pa
                    break
                except ValueError:
                    print("Please enter a valid number for Young's Modulus!")

            if exit_to_menu:
                continue
        
        try:
            # TODO: Get input values (force, area, original_length, change_in_length)
            force = float(input(f"Enter applied force ({units[0]}): "))
            area = float(input(f"Enter cross-sectional area ({units[1]}): ")) 
            original_length = float( input(f"Enter original length ({units[2]}): ") ) 
            change_in_length = float( input(f"Enter change in length ({units[2]}): ") )


            # TODO: Validate inputs (positive values, non-zero where needed)
            if force < 0: 
                print("Force cannot be negative!") 
                continue 

            if area <= 0: 
                print( "Cross-sectional area must be greater than zero " "(prevents division error)!" ) 
                continue 

            if original_length <= 0: 
                print( "Original length must be greater than zero!" ) 
                continue 

            if change_in_length < 0: 
                print("Change in length cannot be negative!") 
                continue


            # TODO: Calculate stress and strain
            stress = force / area
            strain = change_in_length / original_length
            stress_mpa = stress / 1_000_000

            if change_in_length > 0:
                loading_type = "Tension"
            elif change_in_length < 0:
                loading_type = "Compression"
            else:
                loading_type = "No deformation"
            
                
            # TODO: Calculate safety factor
            factor_of_safety = yield_strength / stress if stress > 0 else float("inf")

            if stress < yield_strength:
                if factor_of_safety < 1.2:
                    safety_status = f"CAUTION - Factor of safety: {factor_of_safety:.2f}"
                else:
                    safety_status = f"SAFE - Factor of safety: {factor_of_safety:.2f}"
            else:
                safety_status = f"CRITICAL FAILURE RISK - Stress exceeds Yield Strength! (FOS: {factor_of_safety:.2f})"
                
            # TODO: Create calculation record dictionary with all data
            calculation_record = {
                "test_number": len(calculation_history) + 1,
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
            print("\n" + "="*20 + " RESULTS " + "="*20)
            print(f"Material Profile     : {selected_material}")
            print(f"Applied Force        : {force:,.2f} N")
            print(f"Cross-sectional Area : {area:.6f} m^2")
            print(f"Original Length      : {original_length:,.4f} m")
            print(f"Change in Length     : {change_in_length:,.6f} m")
            print("-" * 49)
            print(f"Calculated Stress    : {stress:,.2f} Pa ({stress_mpa:.4f} MPa)")
            print(f"Calculated Strain    : {strain:.6f}")
            print(f"Loading Classification: {loading_type}")
            print("-" * 49)
            print(f"ANALYSIS REPORT      : {safety_status}")
            print("="*49)

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
    
    print("\n=== SESSION SUMMARY ===")
    print(f"Total number of calculations: {len(calculation_history)}")

    print("\nUnique materials tested:")
    for material in unique_materials:
        print(f"- {material}")

    print("\n=== Calculation History ===")
    for record in calculation_history:
        print(f"\nCalculation #{record['test_number']}:")
        print(f"Material: {record['material']}")
        print(f"Stress: {record['stress']:.2f} Pa")
        print(f"Strain: {record['strain']:.6f}")
        print(f"Factor of Safety: {record['factor_of_safety']:.2f}")
        print(f"Safety Status: {record['safety_status']}")

# Standard Python execution pattern
if __name__ == "__main__":
    main()