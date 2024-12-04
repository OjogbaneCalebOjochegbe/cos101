def display_problems():
    problems = [
        "1. Addition of two numbers",
        "2. Subtraction of two numbers",
        "3. Multiplication of two numbers",
        "4. Division of two numbers",
        "5. Exponentiation (power of a number)"
    ]
    print("\nChoose a mathematical problem to solve:")
    
    for problem in problems:
        print(problem)

def get_user_choice():
    try:
        choice = int(input("\nEnter the number of your chosen problem (1-5): "))
        if 1 <= choice <= 5:
            return choice   
            print("Invalid choice, please choose a number between 1 and 5.")
            return get_user_choice()
    except ValueError:
        print("Invalid input, please enter a number.")
        return get_user_choice()

def get_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Please enter valid numbers.")
        return get_numbers()

def solve_problem(choice):
    if choice == 1:  # Addition
        num1, num2 = get_numbers()
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    
    elif choice == 2:  # Subtraction
        num1, num2 = get_numbers()
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    
    elif choice == 3:  # Multiplication
        num1, num2 = get_numbers()
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    
    elif choice == 4:  # Division
        num1, num2 = get_numbers()
        if num2 != 0:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    
    elif choice == 5:  # Exponentiation
        num1, num2 = get_numbers()
        result = num1 ** num2
        print(f"Result: {num1} ^ {num2} = {result}")

def main():
    display_problems()
    choice = get_user_choice()
    solve_problem(choice)

if __name__ == "__main__":
    main()