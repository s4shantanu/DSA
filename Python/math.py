#  count degits problem 
# enter a list input 
# lst = input("Enter the list: ")
# a = str(len(lst))
# print(a)


#reverse the number
# n = int(input("Enter the number: "))
# rev = 0
# while n > 0:
#     rem = n % 10
#     rev = rev * 10 + rem
#     n = n // 10
# print(rev)



#paliandrome number
# n = int(input("Enter the number: "))
# temp = n
# rev = 0
# while n > 0:
#     rem = n % 10
#     rev = rev * 10 + rem
#     n = n // 10
# if temp == rev:
#     print("Paliandrome")
# else:
#     print("Not Paliandrome")



#paliandrome string
# s = input("Enter the string: ")
# if s == s[::-1]:
#     print("Paliandrome")
# else:
#     print("Not Paliandrome")



#gcd hcf

# def lcmAndGcd(self, a , b):
#         # code here 
#         divisor = min(a,b)
#         divident = max(a,b)
        
        
#         while divisor%divident!=0:
#             temp = divident
#             divident = divisor
#             divisor = temp%divisor
            
#         return divisor
# ans = lcmAndGcd(2,3,4)
# print(ans)



#armstrong number
# n = int(input("Enter the number: "))
# temp = n
# sum = 0
# while n > 0:
#     rem = n % 10
#     sum = sum + rem ** 3
#     n = n // 10
# if temp == sum:
#     print("Armstrong number")
# else:
#     print("Not Armstrong number")


#print divisors
n = int(input("Enter the number: "))
for i in range(1,n+1):
    if n % i == 0:
        print(i,end=" ")
print()


