# To print the multiplication table.
for i in range(13):
# Initially loop will run to 12 but we will break it to 10.
    if(i == 11):
        break
    print(i,"x","5 = ",i*5)
print("Interpreter is out of the loop.")

print("\nCONTINUE STATEMENTS")
for i in range(13):
    if(i == 10):
        print("Skiped the iteration using 'continue'.")
        continue
    print(i,"x","5 = ",i*5)