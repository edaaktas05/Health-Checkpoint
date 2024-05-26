import tkinter as tk
from tkinter import messagebox
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Downloads NLTK data files (only need to run this once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Function to preprocess the input complaint using NLP
def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalnum()]  # Removes punctuation
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    # Stemming and Lemmatization
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    tokens = [stemmer.stem(word) for word in tokens]
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    return tokens

# Function to map symptoms to hospital departments
def get_department(complaint):
    tokens = preprocess_text(complaint)
    
    rules = {
        "Cardiology": ["chest", "pain", "heart", "palpit"],
        "General Medicine": ["cough", "fever", "fatigu"],
        "Dermatology": ["rash", "itch", "skin"],
        "Orthopedics": ["broken", "bone", "sprain", "joint", "pain"],
        "Gastroenterology": ["stomach", "pain", "digest", "abdomin"]
    }
    
    for department, keywords in rules.items():
        for keyword in keywords:
            if keyword in tokens:
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

# Initializes the main application window
root = tk.Tk()
root.title("Hospital Appointment System")

# Creates and place the complaint label and entry
complaint_label = tk.Label(root, text="Please describe your symptoms or complaint:")
complaint_label.pack(pady=10)
complaint_entry = tk.Entry(root, width=50)
complaint_entry.pack(pady=5)

# Creates and place the submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=10)

# Creates and place the result label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Starts the Tkinter event loop
root.mainloop()
