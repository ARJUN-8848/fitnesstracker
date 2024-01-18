import mysql.connector
from datetime import datetime


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="8848613225",
    database="fitnessdb"
)

cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS workouts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        exercise_name VARCHAR(255),
        duration_minutes INT,
        date DATE
    )
""")

def add_workout():
    exercise_name = input("Enter exercise name: ")
    duration_minutes = int(input("Enter duration in minutes: "))
    date = input("Enter date (YYYY-MM-DD): ")

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    cursor.execute("INSERT INTO workouts (exercise_name, duration_minutes, date) VALUES (%s, %s, %s)",
                   (exercise_name, duration_minutes, date))
    db.commit()

    print("Workout added successfully!")

def view_workout_history():
    cursor.execute("SELECT * FROM workouts")
    workouts = cursor.fetchall()

    if not workouts:
        print("No workouts found.")
        return

    print("\nWorkout History:")
    print("ID | Exercise Name | Duration (minutes) | Date")
    print("-" * 50)

    for workout in workouts:
        print(f"{workout[0]} | {workout[1]} | {workout[2]} | {workout[3]}")

def view_statistics():
    cursor.execute("SELECT COUNT(id), SUM(duration_minutes), AVG(duration_minutes) FROM workouts")
    statistics = cursor.fetchone()

    print("\nWorkout Statistics:")
    print(f"Total Workouts: {statistics[0]}")
    print(f"Total Duration (minutes): {statistics[1]}")
    print(f"Average Duration per Workout (minutes): {statistics[2]:.2f}")

def set_goal():
    goal_minutes = int(input("Enter your workout duration goal in minutes: "))
    print(f"Workout goal set to {goal_minutes} minutes.")

def main_menu():
    while True:
        print("\nFitness Tracker Menu:")
        print("1. Add Workout")
        print("2. View Workout History")
        print("3. View Statistics")
        print("4. Set Workout Goal")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            add_workout()
        elif choice == '2':
            view_workout_history()
        elif choice == '3':
            view_statistics()
        elif choice == '4':
            set_goal()
        elif choice == '5':
            print("Exiting Fitness Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == '__main__':
    main_menu()
