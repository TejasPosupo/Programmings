def pattern_5(N):
    for i in range(N+1):
        for j in range(N-i+1):
            print("*", end=" ")
        print()
def main():
    N = eval(input("enter the number "))
    if (N<=1):
        print("enter a greater value")
    else:
        pattern_5(N)

if __name__ == "__main__":
    main()