import sqlite3

conn = sqlite3.connect('calculator_history.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS history
             (id INTEGER PRIMARY KEY AUTOINCREMENT, first_num REAL, operation TEXT, second_num REAL, result REAL)''')

def save_to_db(first_num, operation, second_num, result):
    cur.execute("INSERT INTO history (first_num, operation, second_num, result) VALUES (?, ?, ?, ?)", 
                (first_num, operation, second_num, result))
    conn.commit()  

def show_history():
    cur.execute("SELECT * FROM history")
    rows = cur.fetchall()
    if rows:
        print("\nCalculation History:")
        for row in rows:
            
            print(f"ID: {row[0]} | {row[1]} {row[2]} {row[3]} = {row[4]}")
            print("-"*15)
    else:
        print("\nNo history found.")

print("Welcome to my Calculator Pro!")
while True:
    print("1. Perform a new calculation")
    print("2. Show calculation history")
    print("3. Exit")
    
    main_choice = input("Enter your choice: ")
    
    if main_choice == '1':
        while True:
            try:
                first_num = float(input("Enter the first number: "))
                break
            except ValueError:
                print("Invalid input!, Please enter a number")

        while True:
            try:
                operation = input("Enter the operation: ")
                if operation in ("*", "/", "//", "**", "+", "-", "%"):
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid operator, Please enter *, **, +, -, /, //, %")

        while True:
            try:
                second_num = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Invalid input!, Please enter a number")

        if operation == "+":
            result = first_num + second_num
        elif operation == "-":
            result = first_num - second_num
        elif operation == "/":
            if second_num == 0:
                print("Cannot divide by zero!")
                continue
            else:
                result = first_num / second_num
        elif operation == "*":
            result = first_num * second_num
        elif operation == "**":
            result = first_num ** second_num
        elif operation == "%":
            result = first_num % second_num
        elif operation == "//":
            result = first_num // second_num
        else:
            result = None
        
        if result is not None:
            print("Result is:", result)
            save_to_db(first_num, operation, second_num, result)
    
    elif main_choice == '2':
        show_history()
    
    elif main_choice == '3':
        print("Program exited!")
        break
    
    else:
        print("Invalid choice, please enter 1, 2, or 3")

conn.close()
