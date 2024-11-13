s1 = int(input("Enter the number of first subject - "))
s2 = int(input("Enter the number of second subject - "))
s3 = int(input("Enter the number of third subject - "))
s4 = int(input("Enter the number of fourth subject - "))
s5 = int(input("Enter the number of fifth subject - "))

avg = (s1+s2+s3+s4+s5)/5

if (avg >= 90):
    print("Grade A")
elif (avg >= 80) and (avg < 90):
    print("Grade B")
elif (avg >= 70) and (avg < 80):
    print("Grade C")
elif (avg >= 60) and (avg < 700):
    print("Grade D")
else:
    print("Grade F")