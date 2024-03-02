def pattern11(N):
    start = 1

    for i in range(N):
        if i % 2 == 0:
            start = 1
        else:
            start = 0

        for j in range(i + 1):
            print(start, end="")
            start = 1 - start

        print()

def main():
    N = int(input("Enter the number: "))
    if N <= 1:
        print("Enter a greater value")
    else:
        pattern11(N)

if __name__ == "__main__":
    main()
