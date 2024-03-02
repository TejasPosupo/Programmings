def pattern1(N):
    for i in range(N):
        for i in range(N):
            print("*", end=" ")
        print()
def main():
    N = eval(input("enter the number "))
    if (N<=1):
        print("enter a greater value")
    else:
        pattern1(N)

if __name__ == "__main__":
    main()