print("""
# PORTFOLIO 5: USING PYTHON STRINGS IN ANALYTICAL CHEMISTRY
    Description: Cleans s messy string data from a lab instrument.
    Concepts Used: String Methods (`.strip()`, `.upper()`)
    String Concatenation (`+`)
    The `in` logical operator for substrings
""")

print("\n" + "="*50)
print(" USING PYTHON STRINGS IN ANALYTICAL CHEMISTRY ")
print("="*50 + "\n")

print("# LAB DATA CLEANER & LABEL GENERATOR")
print("Cleans messy string data from a lab instrument and generates a safety label.")

def chemical_name(raw_name):
    """Cleans up a messy string using built-in string methods."""
    cleaned_name = raw_name.strip().upper()
    return cleaned_name

def generate_safety_warning(chemical_string):
    """Uses the string 'in' operator to search for specific substrings."""
    if "ACID" in chemical_string:
        return "WARNING: Corrosive substance. Wear acid-resistant gloves."
    elif "BASE" in chemical_string or "HYDROXIDE" in chemical_string:
        return "WARNING: Caustic substance. Protect eyes and skin."
    elif "METHANOL" in chemical_string:
        return "DANGER: Toxic and Flammable. Keep away from heat."
    else:
        return "Status: Standard laboratory PPE required."

technician_id = "Tech-A"
sample_number = "104B"

while True:
    print("\n--- ANALYTICAL CHEMISTRY: SAMPLE PROCESSING ---")
    
    # Ask user for the analyte/chemical name repeatedly to process multiple entries
    raw_input = input("Enter raw chemical name (or type 'exit' to quit): ")
    
    # Check if user wants to terminate the program
    if raw_input.strip().lower() == 'exit':
        print("Exiting program. Goodbye!")
        break  # This breaks out of the loop and ends the script
        
    # Process the specific input you just typed
    standardized_name = chemical_name(raw_input)
    safety_status = generate_safety_warning(standardized_name)
    database_id = technician_id + "-" + sample_number + "-" + standardized_name

    # Display the results for this specific turn
    print("-------------------------------------------------")
    print(f"Raw Input String: '{raw_input}'")
    print("-------------------------------------------------")
    print(f"Standardized Name: {standardized_name}")
    print(f"Generated Log ID: {database_id}")
    print(f"Safety Check: {safety_status}")

print("\n" + "="*50)