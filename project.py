import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from fpdf import FPDF
import random
import os

# Function to generate PDF invoice
def generate_invoice():
    customer_name = entry_name.get()
    customer_number = entry_number.get()
    car_name = car_combobox.get()
    car_model = model_combobox.get()
    car_number = entry_car_number.get()
    selected_spares = [spare_parts[i] for i in listbox.curselection()]

    if not selected_spares:
        messagebox.showerror("Error", "Please select at least one spare part.")
        return

    total_price = 0
    invoice_items = []

    for spare in selected_spares:
        price = random.randint(50, 200)  # Generate random price for spare part
        total_price += price
        invoice_items.append({"name": spare, "price": price})

    # Create PDF invoice
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Shop Name
    pdf.cell(200, 10, txt="SV Auto Spares", ln=True, align="C")
    pdf.ln(10)

    # Customer Details
    pdf.cell(200, 10, txt=f"Customer Name: {customer_name}", ln=True)
    pdf.cell(200, 10, txt=f"Customer Number: {customer_number}", ln=True)
    pdf.cell(200, 10, txt=f"Car Name: {car_name}", ln=True)
    pdf.cell(200, 10, txt=f"Car Model: {car_model}", ln=True)
    pdf.cell(200, 10, txt=f"Car Number: {car_number}", ln=True)
    pdf.ln(10)

    # Invoice Items
    pdf.cell(200, 10, txt="Selected Spare Parts:", ln=True)
    for item in invoice_items:
        pdf.cell(200, 10, txt=f"{item['name']} - ${item['price']}", ln=True)
    pdf.ln(10)

    # Total Price
    pdf.cell(200, 10, txt=f"Total Price: ${total_price}", ln=True)

    filename = f"bill/{customer_name}_invoice.pdf"
    pdf.output(filename)

    messagebox.showinfo("Success", f"Invoice generated and saved as {filename}")

# Create Tkinter window
root = tk.Tk()
root.title("Car Spare Parts Store Invoice")
root.geometry("400x400")

# Customer Details
label_name = tk.Label(root, text="Customer Name:")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

label_number = tk.Label(root, text="Customer Number:")
label_number.pack()
entry_number = tk.Entry(root)
entry_number.pack()

# Car Details
label_car = tk.Label(root, text="Car Name:")
label_car.pack()
car_combobox = ttk.Combobox(root, values=["Toyota", "Volkswagen", "Ford", "Honda", "Chevrolet", "Nissan", "Mercedes-Benz", "BMW", "Audi", "Hyundai", "Subaru", "Kia", "Tesla", "Jeep", "Mazda", "Lexus", "GMC", "Dodge", "Volvo", "Porsche", "Chrysler", "Cadillac", "Land Rover", "Mitsubishi", "Buick", "Jaguar", "Infiniti", "Acura", "Lincoln", "Ram"])
car_combobox.pack()

label_model = tk.Label(root, text="Model Year:")
label_model.pack()
model_combobox = ttk.Combobox(root, values=[str(year) for year in range(1980, 2025)])
model_combobox.pack()

label_car_number = tk.Label(root, text="Car Number:")
label_car_number.pack()
entry_car_number = tk.Entry(root)
entry_car_number.pack()

# Spare Parts Selection
label_spares = tk.Label(root, text="Select Spare Parts:")
label_spares.pack()
spare_parts = ["Spark Plugs", "Oil Filter", "Air Filter", "Fuel Filter", "Timing Belt", "Serpentine Belt", "Water Pump", "Thermostat", "Radiator Hose", "Radiator Cap", "Engine Oil", "Coolant/Antifreeze", "PCV Valve (Positive Crankcase Ventilation)", "Camshaft Position Sensor", "Crankshaft Position Sensor", "Oxygen Sensor", "Engine Control Module (ECM) or Engine Control Unit (ECU)", "Ignition Coil", "Distributor Cap and Rotor (for older engines)", "Engine Mounts", "Turbocharger (for turbocharged engines)", "Intercooler (for turbocharged engines)", "Intake Manifold Gasket", "Exhaust Manifold Gasket", "Head Gasket"]
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
for part in spare_parts:
    listbox.insert(tk.END, part)
listbox.pack()

# Generate Invoice Button
button_generate = tk.Button(root, text="Generate Invoice", command=generate_invoice)
button_generate.pack()

# Create bill directory if not exists
if not os.path.exists("bill"):
    os.makedirs("bill")

root.mainloop()
