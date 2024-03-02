def pattern_10(N):
    for i in range(1, 2*N):
        stars = i if i <= N else 2*N - i
        for j in range(stars):
            print("*", end="")
        print()

def main():
    N = int(input("Enter the number: "))
    if N <= 1:
        print("Enter a greater value")
    else:
        pattern_10(N)

if __name__ == "__main__":
    main()
