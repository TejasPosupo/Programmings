def add_two_numbers(num1, num2):
    return num1 + num2

if __name__ == "__main__":
    num1 = int(input("Enter the First Number "))
    num2 = int(input("Enter the Second Number "))
    result = add_two_numbers(num1, num2)
print("The sum of " , num1, " and ", num2, "is", result)
