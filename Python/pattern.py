n = int(input("Give the no. of lines you want to print: "))
def pattern(n):
    for i in range(n):
        for j in range(n):
            print(j+1, end = "")
        print()
# pattern(n)

def pattern1(n):
    for i in range(n):
        for j in range(i):
            print("*", end = "")
        print()
pattern1(n)

# def nTriangle(n:int) ->None:
#     for i in range(n):
#         for j in range(i+1):
#             print(j+1,end=" ")
#         print()
#     # Write your solution here.
#     pass
# # nTriangle(n)

# def nNumberTriangle(n: int) -> None:
#     for i in range(n):
#         for j in range(n-i):
#             print(j+1, end=" ")
#         print()
#     # Write your solution here.
#     pass
# # nNumberTriangle(n)

# def nStarTriangle(n: int) -> None:
#     for i in range(n):
#         for j in range(i):
#             print(" ",end="")
#         for j in range(2*(n-1-i)+1):
#             print("*", end="")
#         print()
#     # Write your code here.
#     pass
# # nStarTriangle(n)


# def nStarTriangle1(n: int) -> None:
#     for i in range(n):
#         for j in range(n-i):
#             print(" ",end="")
#         for j in range(2*i+1):
#             print("*", end="")
#         print()
#     # Write your code here.
#     pass
# # nStarTriangle1(n)

# def nStarTriangle2(n: int) -> None:
#     for i in range(n):
#         for j in range(i):
#             print(" ",end="")
#         for j in range(2*(n-1-i)+1):
#             print("*", end="")
#         print()
#     for i in range(n):
#         for j in range(n-i):
#             print(" ",end="")
#         for j in range(2*i+1):
#             print("*", end="")
#         print()
#     # Write your code here.
#     pass
# # nStarTriangle2(n)


# def nStarTriangle3(n: int) -> None:
#     for i in range(n):
#         for j in range(n-i):
#             print(" ",end="")
#         for j in range(2*i+1):
#             print("*", end="")
#         print()
#     for i in range(n):
#         for j in range(i):
#             print(" ",end="")
#         for j in range(2*(n-1-i)+1):
#             print("*", end="")
#         print()
#     # Write your code here.
#     pass
# # nStarTriangle3(n)

