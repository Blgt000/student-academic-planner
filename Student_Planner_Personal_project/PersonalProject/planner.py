import json
from datetime import datetime


FILE_NAME = "data.json"


# Load existing data or create new


def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


# Save data to file
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)
# Add a new subject
def add_subject(data):
    subject = input("Enter subject name: ")
    exam_date = input("Enter exam date (YYYY-MM-DD): ")
    data[subject] = {
        "exam_date": exam_date,
        "study_hours": []
    }
    print("Subject added successfully.")


# Log study hours
def log_study(data):
    subject = input("Enter subject name: ")
    if subject in data:
            hours = float(input("Enter study hours: "))
            data[subject]["study_hours"].append(hours)
            print("Study session recorded.")
    else:
            print("Subject not found.")


# Analyze performance
def analyze(data):
    for subject, info in data.items():
        total_hours = sum(info["study_hours"])
        exam_date = datetime.strptime(info["exam_date"], "%Y-%m-%d")
        days_left = (exam_date - datetime.now()).days


        if total_hours >= days_left * 2:
            prediction = "Good"
        else:
            prediction = "Needs Improvement"


        print(f"\nSubject: {subject}")
        print(f"Total Study Hours: {total_hours}")
        print(f"Days Until Exam: {days_left}")
        print(f"Performance Prediction: {prediction}")


# Main menu


def main():
    data = load_data()


    while True:
        print("\n1. Add Subject")
        print("2. Log Study Hours")
        print("3. Analyze Performance")
        print("4. Save & Exit")


        choice = input("Choose an option: ")


        if choice == "1":
            add_subject(data)
        elif choice == "2":
            log_study(data)
        elif choice == "3":
            analyze(data)
        elif choice == "4":
            save_data(data)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid option.")


main()