def pattern13(N):
    num = 1

    for i in range(1, N + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1

        # Move to the next row and give a line break
        print()

def main():
    N = int(input("Enter the number: "))
    if N <= 1:
        print("Enter a greater value")
    else:
        pattern13(N)

if __name__ == "__main__":
    main()
