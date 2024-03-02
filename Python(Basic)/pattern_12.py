def pattern12(N):
    spaces = 2 * (N - 1)

    for i in range(1, N + 1):
        # Printing numbers in ascending order
        for j in range(1, i + 1):
            print(j, end="")

        # Printing spaces
        for j in range(1, spaces + 1):
            print(" ", end="")

        # Printing numbers in descending order
        for j in range(i, 0, -1):
            print(j, end="")

        # Move to the next row and give a line break
        print()

        # Update the number of spaces
        spaces -= 2

def main():
    N = int(input("Enter the number: "))
    if N <= 1:
        print("Enter a greater value")
    else:
        pattern12(N)

if __name__ == "__main__":
    main()
