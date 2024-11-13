def average(a=5,b=5): # This is default argument,it gets executed by just calling a function.
    print("The average is",(a+b)/2)

average()
average(4,4) # The default arguments can be overwrited.

print("\nLooping the function.")

def avg(*numbers): # " * " makes it an tuple.
    for i in numbers:
        sum = 0
        sum = sum + i
        # print("Average is",sum/len(numbers))
        return sum/len(numbers) # Return function is use to return the value back to the function.

c = avg(2,3)
print(c)