import csv

def add_application():
    company = input("Company Name: ")
    role = input("Role Applied For: ")
    date_applied = input("Date Applied (DD-MM-YYYY): ")
    status = input("Current Status (Applied / Interview / Rejected / Offer): ")

    with open("applications.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([company, role, date_applied, status])
    
    print("✅ Application added successfully!\n")

def view_applications():
    try:
        with open("applications.csv", mode="r") as file:
            reader = csv.reader(file)
            print("\n📄 Your Job Applications:\n")
            print("{:<20} {:<20} {:<15} {:<15}".format("Company", "Role", "Date Applied", "Status"))
            print("-" * 70)
            for row in reader:
                print("{:<20} {:<20} {:<15} {:<15}".format(*row))
            print()
    except FileNotFoundError:
        print("\n⚠️ No applications found yet. Add some first!\n")
while True:
    print("\n📋 Job Application Tracker")
    print("1. Add new application")
    print("2. View all applications")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        add_application()
    elif choice == "2":
        view_applications()
    elif choice == "3":
        print("👋 Exiting... See you again!")
        break
    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")



