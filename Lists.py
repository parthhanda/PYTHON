marks = [3,4,5,"Parth"] # It can contain multiple data types.
print(marks)
print(type(marks))
print(marks[0]) # The lists are odered and the indexing starts from 0.

print("\nINDEXING")
print(marks[:4])
print(marks[1:]) # Last index will not be printed.
print(marks[1:3])
print(marks[1:-1])
print(marks[1:4:2]) # Third one is jump inex.

print("\nLIST COMPREHENSION")
l1 = [i for i in range(10)] # It will create a list from 1 - 10.
print(l1)
l2 = [i for i in range(10 ) if i%2==0] # It will print only even numbers.
print((l2))