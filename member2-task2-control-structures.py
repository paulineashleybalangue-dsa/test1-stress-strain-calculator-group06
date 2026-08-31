def main():
    """Main function for the stress and strain calculator with enhanced validation and control structures."""
    
    # Material Database 
    materials = {"1": {"name": "Steel", "yield_strength": 250_000_000, "youngs_modulus": 200_000_000_000},
                 "2": {"name": "Aluminum", "yield_strength": 95_000_000, "youngs_modulus": 69_000_000_000},
                 "3": {"name": "Titanium", "yield_strength": 880_000_000, "youngs_modulus": 114_000_000_000}}
    
#  #Repeated Calculation Loop
    while True:
        print("\n=== Intelligent Stress and Strain Calculator ===")
        print("1. Steel")
        print("2. Aluminum")
        print("3. Titanium")
        print("4. Custom Material")
        print("5. Exit Program")
        print("Type 'q' or 'quit' at any prompt to exit back to menu")
        
        choice = input("Select a material option (1-5): ").strip()

        if choice.lower() in ["5", "q", "quit"]:
            print("\nExiting program. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("[Invalid Choice] Please select an option between 1 and 5.")
            continue

        # Material Property Assignment
        if choice in materials:
            selected_material = materials[choice]["name"]
            yield_strength = materials[choice]["yield_strength"]
            youngs_modulus = materials[choice]["youngs_modulus"]
        else:
            selected_material = input("Enter custom material name: ").strip()
            if not selected_material.lower() in ["q", "quit"]:
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

        #Display reference material properties
        print(f"\n--- Selected Material Properties ---")
        print(f"Material: {selected_material}")
        print(f"Yield Strength: {yield_strength / 1_000_000:.2f} MPa")
        print(f"Typical Young's Modulus: {youngs_modulus / 1_000_000_000:.2f} GPa")
        print("------------------------------------")

        # --- ENHANCED INPUT HANDLING & VALIDATION ---
        #Validating Force
        while True:
            raw_val = input("Enter applied force (N): ").strip()
            if raw_val.lower() in ['q', 'quit']:
                abort_calculation = True
                break
            try:
                force = float(raw_val)
                if force < 0:
                    print("Force cannot be negative!")
                    continue
                break
            except ValueError:
                print("Please enter a valid numeric value for Force!(or 'q' to quit)!")

        if abort_calculation:
            print("\n[Calculation Canceled] Returning to main menu.")
            continue

        #Validating Area
        while True:
            raw_val = input("Enter cross-sectional area (m^2): ").strip()
            if raw_val.lower() in ['q', 'quit']:
                abort_calculation = True
                break
            try:
                area = float(raw_val)
                if area <= 0:
                    print("Cross-sectional area must be greater than zero (prevents division error)!")
                    continue
                break
            except ValueError:
                print("Please enter a valid numeric value for Area!")

        if abort_calculation:
            print("\n[Calculation Canceled] Returning to main menu.")
            continue

        #Validate Original Length
        while True:
            raw_val = input("Enter original length (m): ").strip()
            if raw_val.lower() in ['q', 'quit']:
                abort_calculation = True
                break 
            try:
                original_length = float(raw_val)
                if original_length <= 0:
                    print("Original length must be greater than zero!") #Prevent zero division error
                    continue
                break
            except ValueError:
                print("Please enter a valid numeric value (or 'q' to 'quit')!")

        if abort_calculation:
            print("\n[Calculation Canceled] Returning to main menu.")
            continue

        #Validate change in length
        while True:
            raw_val = input("Enter change in length (m): ").strip()
            if raw_val.lower() in ['q', 'quit']:
                abort_calculation = True
                break 
            try:
                change_in_length = float(raw_val)
                if change_in_length < 0:
                    print("Change in length cannot be negative!")
                    continue
                break
            except ValueError:
                print("Please enter a valid numeric value (or 'q' to quit)!")

        if abort_calculation:
            print("\n[Calculation Canceled] Returning to main menu.")
            continue

        # --- Core computations ---
        stress = force / area
        strain = change_in_length / original_length
        stress_mpa = stress / 1_000_000

        if change_in_length > 0:
            loading_type = "Tension"
        elif change_in_length < 0:
            loading_type = "Compression"
        else:
            loading_type = "No deformation"

        # --- Safety analysis ---
        factor_of_safety = yield_strength / stress if stress > 0 else float('inf')
        
        if stress < yield_strength:
            if factor_of_safety < 1.2:
                safety_status = f"CAUTION - Factor of safety: {factor_of_safety:.2f}"
            else:
                safety_status = f"SAFE - Factor of safety: {factor_of_safety:.2f}"
        else:
            safety_status = f"CRITICAL FAILURE RISK - Stress exceeds Yield Strength! (FOS: {factor_of_safety:.2f})"

        # --- Display formatted analysis output ---
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

#Calling the main function
if __name__ == "__main__":
    main()