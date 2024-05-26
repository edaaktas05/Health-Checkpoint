import tkinter as tk
from tkinter import messagebox

# Function to map symptoms to hospital departments
def get_department(complaint):
    complaint = complaint.lower()
    
    rules = {
        "Cardiology": ["chest pain", "heart", "palpitations"],
        "General Medicine": ["cough", "fever", "fatigue"],
        "Dermatology": ["rash", "itching", "skin"],
        "Orthopedics": ["broken bone", "sprain", "joint pain"],
        "Gastroenterology": ["stomach pain", "digestive", "abdominal pain"]
    }
    
    for department, keywords in rules.items():
        for keyword in keywords:
            if keyword in complaint:
                return department
                
    return "General Consultation"

# Function to handle the submit button click event
def on_submit():
    complaint = complaint_entry.get()
    if not complaint:
        messagebox.showwarning("Input Error", "Please enter your symptoms or complaint.")
        return

    department = get_department(complaint)
    result_label.config(text=f"Based on your symptoms, you should visit the {department} department.")

# Initialize the main application window
root = tk.Tk()
root.title("Hospital Appointment System")

# Create and place the complaint label and entry
complaint_label = tk.Label(root, text="Please describe your symptoms or complaint:")
complaint_label.pack(pady=10)
complaint_entry = tk.Entry(root, width=50)
complaint_entry.pack(pady=5)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=10)

# Create and place the result label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
