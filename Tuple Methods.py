# Although tuples are IMMUTABLE.
# But they can still be changed indirectly,by converting it into the list.
tup = ("My","name","is","Parth")
print("Initial Tuple ->",tup)
temp = list(tup)
temp.append("Handa")
tup = tuple(temp)
print("After appending ->",tup)