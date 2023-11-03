def pattern_4(N):
    for i in range(1+N):
        for j in range(1, i+1):
            print(i, end=" ")
        print()
def main():
    N = eval(input("enter the number "))
    if (N<=1):
        print("enter a greater value")
    else:
        pattern_4(N)

if __name__ == "__main__":
    main()