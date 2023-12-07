
# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Main program
if __name__ == "__main__":
    # Input two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Call the add_numbers function and print the result
    result = add_numbers(num1, num2)
    print("The sum of", num1, "and", num2, "is", result)
