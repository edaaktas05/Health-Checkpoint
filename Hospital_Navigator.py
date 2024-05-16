def get_department(complaint):
    complaint = complaint.lower()
    
    if "chest pain" in complaint or "heart" in complaint:
        return "Cardiology"
    elif "cough" in complaint or "fever" in complaint:
        return "General Medicine"
    elif "rash" in complaint or "allergy" in complaint:
        return "Dermatology"
    elif "broken bone" in complaint or "sprain" in complaint:
        return "Orthopedics"
    elif "stomach pain" in complaint or "digestive" in complaint:
        return "Gastroenterology"
    else:
        return "General Consultation"

def main():
    print("Welcome to the Hospital Appointment System")
    complaint = input("Please describe your symptoms or complaint: ")
    department = get_department(complaint)
    print(f"Based on your symptoms, you should visit the {department} department.")
    
if __name__ == "__main__":
    main()
