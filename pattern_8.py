def pattern_7(N):
    for i in range(N):
        for j in range(i):
             print(" ", end="")
        for k in range(2*N-(2*i+1)):
            print("*", end="")
        for j in range(i):
            print(" ", end="")
        print()
def main():
    N = eval(input("enter the number "))
    if (N<=1):
        print("enter a greater value")
    else:
        pattern_7(N)

if __name__ == "__main__":
    main()
