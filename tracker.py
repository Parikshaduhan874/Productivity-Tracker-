import csv
import datetime
import matplotlib.pyplot as plt
import os

DATA_FILE = "data/productivity_log.csv"

def add_entry():
    task = input("Task: ")
    time_spent = input("Time Spent (in minutes): ")
    rating = input("Productivity Rating (1-5): ")
    date = datetime.date.today()

    with open(DATA_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, task, time_spent, rating])
    print("✅ Entry added!")

def view_entries():
    if not os.path.exists(DATA_FILE):
        print("No data found.")
        return
    with open(DATA_FILE, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def plot_chart():
    if not os.path.exists(DATA_FILE):
        print("No data found.")
        return

    dates, ratings = [], []
    with open(DATA_FILE, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                dates.append(row[0])
                ratings.append(int(row[3]))
            except:
                continue
    plt.figure(figsize=(10, 5))
    plt.plot(dates, ratings, marker='o')
    plt.title("📈 Productivity Over Time")
    plt.xlabel("Date")
    plt.ylabel("Rating")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("output/charts.png")
    plt.show()

def menu():
    while True:
        print("\n=== Productivity Tracker ===")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Plot Chart")
        print("4. Exit")
        choice = input("Choose: ")
        if choice == '1':
            add_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            plot_chart()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
