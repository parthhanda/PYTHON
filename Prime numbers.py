def is_prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False
        return True
    else:
        return True

num1 = 17
num2 = 5

if is_prime(num1):
    print(f"{num1} is a prime number.")
else:
    print(f"{num1} is not a prime number.")

if is_prime(num2):
    print(f"{num2} is a prime number.")
else:
    print(f"{num2} is not a prime number.")


