def add( a , b ):
    return a + b
def subtract( a, b ):
    return a - b
def multiply( a , b ):
    return a * b
def divide( a , b ):
    if b==0:
        return "Error! Can not divide by zero"
    return a / b

def get_valid_number(prompt):
    while True:
        try:
            user_input = input(prompt)
            return float(user_input)
        except ValueError:
            print("Invalid input!!! Please enter a numerical value.")

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error! Cannot divide by zero"
        return a / b

    def menu(self):
        print("====Welcome to the Calculator===")
        print("Please choose an Operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        print("==============================")

    def run(self):
        while True:
            self.menu()
            choice = input("Enter your choice (1-5): ")

            if choice == "5":
                print("Exiting Calculator!")
                break
            elif choice in ("1", "2", "3", "4"):
                num1 = get_valid_number("Enter the first number: ")
                num2 = get_valid_number("Enter the second number: ")
        
                if choice == '1':
                    result = self.add(num1, num2)
                    operation_symbol = "+"
                elif choice == '2':
                    result = self.subtract(num1, num2)
                    operation_symbol = "-"
                elif choice == '3':
                    result = self.multiply(num1, num2)
                    operation_symbol = "*"
                elif choice == '4':
                    result = self.divide(num1, num2)
                    operation_symbol = "/"
                print("\n--- Result ---")
                
                if isinstance(result, str):                   
                    print(result)
                else:                   
                    print(f"{num1} {operation_symbol} {num2} = {result}")
                print("--------------")
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


my_calculator = Calculator()
my_calculator.run()
