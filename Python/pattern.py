n = int(input("Give the no. of lines you want to print: "))
def pattern(n):
    for i in range(n):
        for j in range(n):
            print(j+1, end = "")
        print()
pattern(n)