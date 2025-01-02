def calculator():
    print("Welcome to the Basic Calculator!")
    print("Select an operation to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        try:
            # Ask the user to select an operation
            choice = input("Enter the number corresponding to your choice (1/2/3/4): ")
            
            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice. Please select a valid operation.")
                continue
            
            # Get numbers from the user
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            # Perform the chosen operation
            if choice == '1':
                result = num1 + num2
                print(f"The result of addition: {num1} + {num2} = {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"The result of subtraction: {num1} - {num2} = {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"The result of multiplication: {num1} * {num2} = {result}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"The result of division: {num1} / {num2} = {result}")
            
            # Ask the user if they want to perform another calculation
            next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
            if next_calculation != 'yes':
                print("Thank you for using the calculator. Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter numbers only.")

# Run the calculator
if __name__ == "__main__":
    calculator()
