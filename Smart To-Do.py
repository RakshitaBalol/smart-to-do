# Simple Smart To-Do & Habit Companion

tasks = []
habits = {}   # habit_name : streak
done_today = set()

# ---------- TASK FUNCTIONS ----------

def add_task():
    task = input("Enter task: ")
    tasks.append({"name": task, "done": False})
    print("✅ Task added")

def view_tasks():
    if not tasks:
        print("No tasks available")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            status = "✔" if task["done"] else "✖"
            print(f"{i}. {task['name']} - {status}")

def mark_task_done():
    view_tasks()
    num = int(input("Enter task number to mark as done: "))
    if 1 <= num <= len(tasks):
        tasks[num-1]["done"] = True
        print("✅ Task marked as done")
    else:
        print("❌ Invalid number")

# ---------- HABIT FUNCTIONS ----------

def add_habit():
    habit = input("Enter habit name: ")
    if habit not in habits:
        habits[habit] = 0
        print("🌱 Habit added")
    else:
        print("Habit already exists")

def view_habits():
    if not habits:
        print("No habits available")
    else:
        print("\nHabits:")
        for habit, streak in habits.items():
            status = "✔" if habit in done_today else "✖"
            print(f"{habit} - Streak: {streak} - {status}")

def mark_habit_done():
    view_habits()
    habit = input("Enter habit name to mark done: ")

    if habit in habits:
        if habit not in done_today:
            habits[habit] += 1
            done_today.add(habit)
            print("✅ Habit marked as done for today")
        else:
            print("Already marked today")
    else:
        print("❌ Habit not found")

# ---------- WELLNESS INSIGHT ----------

def show_insight():
    if tasks:
        completed = sum(1 for t in tasks if t["done"])
        task_score = completed / len(tasks)
    else:
        task_score = 0

    if habits:
        habit_score = len(done_today) / len(habits)
        avg_streak = sum(habits.values()) / len(habits)
    else:
        habit_score = 0
        avg_streak = 0

    total_score = (task_score * 0.6 + habit_score * 0.4) * 100

    print("\n📊 Daily Wellness Insight")
    print(f"Score: {int(total_score)}%")
    print(f"Tasks done today: {sum(1 for t in tasks if t['done'])}/{len(tasks)}")
    print(f"Habits done today: {len(done_today)}/{len(habits)}")
    print(f"Average habit streak: {avg_streak:.1f}")

    if total_score > 80:
        print("🌟 Excellent work today!")
    elif total_score > 50:
        print("🙂 Good, but you can do better!")
    else:
        print("💪 Try to improve tomorrow!")

# ---------- MAIN MENU ----------

while True:
    print("\n==== Smart To-Do & Habit Companion ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Add Habit")
    print("5. View Habits")
    print("6. Mark Habit as Done")
    print("7. Show Wellness Insight")
    print("8. Exit")

    choice = input("Enter choice (1-8): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_done()
    elif choice == "4":
        add_habit()
    elif choice == "5":
        view_habits()
    elif choice == "6":
        mark_habit_done()
    elif choice == "7":
        show_insight()
    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again")
