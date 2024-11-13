tup1 = (1,2,3,4,5)
tup2 = ("RED","GREEN","YELLOW","BLUE","BLACK")
print(tup1)
print(tup2,"\n")

print("Indexing ->",tup1[0],",",tup2[0],"\n") # Indexing

print("Slicing ->",tup1[1:3],"\n") # Slicing

if "RED" in tup2:
    print("Yes RED is present")