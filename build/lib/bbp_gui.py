import tkinter as tk
from tkinter import ttk

# Define materials needed for each building type
materials = {
    'large wall': {'nails': 20, 'planks': 11},
    'large door': {'nails': 30, 'planks': 15},
    'small door' : {'nails': 30, 'planks': 13},
    'garage door': {'nails': 22, 'planks': 12},
    'large floor': {'nails': 20, 'planks': 13},
    'large roof': {'nails': 20, 'planks': 13},
    'foundation': {'nails': 20, 'planks': 8, 'logs': 2},
    # Add more building types as needed
}

# Function to calculate materials needed for all selected building types
def calculate_materials():
    total_nails = 0
    total_planks = 0
    total_logs = 0

    for i, (building_type, material_info) in enumerate(materials.items()):
        quantity = int(quantity_vars[i].get())

        total_nails += materials[building_type]['nails'] * quantity
        total_planks += materials[building_type]['planks'] * quantity

        # Check if 'logs' is present in the material requirements
        if 'logs' in materials[building_type]:
            total_logs += materials[building_type]['logs'] * quantity

    result_label.config(text=f"For the specified quantities, you will need:\n"
                             f"{total_nails} nails\n"
                             f"{total_planks} planks\n"
                             f"{total_logs} logs")

# Create main window
root = tk.Tk()
root.title("Materials Calculator")

# Lists to store variables for quantities
quantity_vars = []

# Create and layout fixed building type labels and quantity entries
for i, (building_type, material_info) in enumerate(materials.items()):
    # Building Type Label
    ttk.Label(root, text=f"Building Type: {building_type}").grid(row=i, column=0, padx=10, pady=5, sticky="w")

    # Quantity
    quantity_var = tk.StringVar(value=0)
    quantity_vars.append(quantity_var)
    ttk.Label(root, text=f"Enter Quantity:").grid(row=i, column=1, padx=10, pady=5, sticky="w")
    quantity_entry = ttk.Entry(root, textvariable=quantity_var, width=10)
    quantity_entry.grid(row=i, column=2, padx=10, pady=5)

# Calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate_materials)
calculate_button.grid(row=len(materials), column=0, columnspan=3, pady=10)

# Result label
result_label = ttk.Label(root, text="")
result_label.grid(row=len(materials) + 1, column=0, columnspan=3, pady=5)

# Run the GUI
root.mainloop()