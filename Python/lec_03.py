#Pattern Examples 

# def pattern(n):
#     for i in range(n):
#         for j in range(i+1):
#             print("1", end=" ")
#         print("\r")
# pattern(5)

# def pattern2(n):
#     for i in range(n):
#         for j in range(n-i):
#             print("1", end=" ")
#         print("\r")

# pattern2(5)

#fibonacci seqence
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610

# Fibonacci problems
# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return (fib(n-1)+fib(n-2))
# print(fib(10))

def Fib(n):
    n1, n2 = 0, 1
    for i in range(2, n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3, end=" ")
Fib(10)