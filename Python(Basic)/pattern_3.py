def pattern_3(N):
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def main():
    N = eval(input("enter the number "))
    if (N<=1):
        print("enter a greater value")
    else:
        pattern_3(N)

if __name__ == "__main__":
    main()