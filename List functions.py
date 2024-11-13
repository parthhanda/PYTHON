l = [10,1,2,3,4,1]
print(l)

l.append(7) # APPEND is use to add something at the end of the list.
print("\nAfter APPENDING 7 =",l,"\n")

l.sort() # SORT fnc. arranges the list in ascending order.
print("SORTING list in ascending order =",l,"\n")

l.sort(reverse=True) # SORT(reverse=True) fnc. arranges the list in descending order.
print("SORTING list in descending order =",l,"\n")

l.reverse() # it reverses the orignal list.
print("Reversing the orignal list =",l,"\n")

print("Count of list =",l.count(1),"\n") # Prints the occurance of it.

l.insert(5,5) # inserts an item at the given index.
print("Insert =",l,"\n")

m = [2,3,4]
l.extend(m) # Concatinates two strings.
print("Extend =",l,"\n")

k = l + m # Concatinates using a third variable.
print("Concatinating using a third variable =",l,"\n")