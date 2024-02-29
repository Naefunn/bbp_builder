# Define materials needed for each building type
materials = {
    'large wall': {'nails': 20, 'planks': 11},
    'large door': {'nails': 30, 'planks': 15},
    'small door' : {'nails': 30, 'planks': 13},
    'garage door': {'nails': 22, 'planks': 12},
    'large floor': {'nails': 20, 'planks': 13},
    'large roof': {'nails': 20, 'planks': 13},
    'foundation': {'nails': 20, 'planks': 13, 'logs': 2}
    # Add more building types as needed
}

# Function to calculate materials needed
def calculate_materials(building_quantities):
    total_nails = 0
    total_planks = 0
    total_logs = 0

    for building_type, quantity in building_quantities.items():
        if building_type in materials:
            total_nails += materials[building_type]['nails'] * quantity
            total_planks += materials[building_type]['planks'] * quantity
           
           #check if logs needed
            if 'logs' in materials[building_type]:
                total_logs += materials[building_type]['logs'] * quantity
        else:
            print(f"Building type '{building_type}' not found in the materials dictionary.")

    return {'nails': total_nails, 'planks': total_planks, 'logs': total_logs}

# Take input from the user
building_quantities = {}
while True:
    building_type = input("Enter building type (or 'done' to finish): ").lower()
    if building_type == 'done':
        break

    if building_type in materials:
        quantity = int(input(f"Enter quantity for {building_type}: "))
        building_quantities[building_type] = quantity
    else:
        print(f"Building type '{building_type}' not found in the materials dictionary.")

result = calculate_materials(building_quantities)

if result:
    print("For the specified quantities, you will need:")
    print(f"{result['nails']} nails")
    print(f"{result['planks']} planks")
    print(f"{result['logs']} logs")