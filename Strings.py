a="Hello"
b="World"
print(a+b) #HelloWorld
print(a+" "+b) #Hello World
# By using a '+' symbol in print function we can add two strings together.
c=20
print(c+30) #50
# By using a '+' symbol in print function with variables wil add them up'
# But you cannot add two different type of datatypes(strings + number).
name = 'He said his name is "Parth" '  # To use double quotes(" ") in the strings , start it with single quotes(' ')
print(name)
multiline = '''To print several line 
like this
we use triple quotes (''' ''')
 or triple double quotes (""" """) '''
print(multiline)

# INDEXING

# a="Hello"
print(a[0])
print(a[1])
print(a[-4:-2])
print(name[0:])

print("*To print using FOR loop*\n")
for character in multiline :
    print(character)

# len() function -> to check the length of the function.
name1 = "Parth"
length = len(name1)
print("My name has",length,"letters.\n")

# STRING METHODS (Strings are immutable.)
print("*String methods*\n")

sm = "!! parth !! parth"

print(len(sm))  # To print the length of the string.
print(sm.upper())  # To print every letter of a string in the upper case.
print(sm.lower())  # To print every letter of a string in the lower case.
print(sm.rstrip("!")) # To stip the last characters.
print(sm.replace("parth","handa"))  # Replaces all the occurence of the string with a new string.
print(sm.split(" "))  # Split fnc. splits the str into lists.
print(a.capitalize())  # Capitalizes only the first letter and lowercases all the other characters.
print(sm.center(50))  # It adds the amount of spaces in the front.
print(sm.count("parth"))  # It counts the the word in the string.
