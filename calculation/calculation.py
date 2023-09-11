# Define a list to store the history of calculations
history = []
# Function to perform calculations and add them to the history
def calculate():
    while True:
        print("\nMenu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Display Calculation History")
        print("6. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6): ")
        if choice == '6':
            break
        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please select a valid option.")
            continue
        if choice == '5':
            print("\nCalculation History:")
            for item in history:
                print(item)
            continue
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if choice == '1':
            operation = 'Addition'
            result = num1 + num2
        elif choice == '2':
            operation = 'Subtraction'
            result = num1 - num2
        elif choice == '3':
            operation = 'Multiplication'
            result = num1 * num2
        elif choice == '4':
            operation = 'Division'
            if num2 == 0:
                print("Error: Division by zero")
                continue
            result = num1 / num2
        calculation = f"{num1} {operation} {num2} = {result}"
        history.append(calculation)
        print(f"Result: {result}")
# Main program loop
if __name__ == "__main__":
    print("Mini Calculator Program")
    calculate()
