# year = int(input("Enter the year - "))
#
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print(f"{year} ia a leap year.")
# else:
#     print(f"{year} is not a leap year.")

# def is_prime(num):
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 return False
#         return True
#     else:
#         return True
#
# num1 = 17
# num2 = 54
#
# if is_prime(num1):
#     print(f"{num1} is a prime number. ")
# else:
#     print(f"{num1} is not a prime number. ")

# if is_prime(num2):
#     print(f"{num2} is a prime number. ")
# else:
#     print(f"{num2} is not a prime number. ")

# n = int(input())
# l = []
# k = 0
# l = []
#
# for i in range(0,n):
#     l.append(float(input()))
#
# for i in range(len(l)):
#     if (l[i]>k):
#         k = l[i]
#
# c = 0
#
# for j in range(len(l)):
#     if (l[j] == k):
#         c = c+1
#
# print(c)


# def recur_fibo(n):
#     if n <=1:
#         return n
#     else:
#         return (recur_fibo(n-1) + recur_fibo(n-2))
#
# nterms = int(input())
#
# if nterms <=0:
#     print("Please enter any positive intiger")
# else:
#     for i in range(nterms):
#         print(recur_fibo(i))

# name = input("Enter your full name - ").title()
#
# words = name.split()
# last_word = words[-1]
#
# abb_name = '.'.join([word[0] + '' for word in words[:-1]]) + '.' + last_word
#
# print(abb_name)

