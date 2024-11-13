#input name / output short form of name

name = input('Enter your name: ').title()

# Separate the last word
words = name.split()
last_word = words[-1]

# Create an abbreviated version
abbreviated_name = '.'.join([word[0] + '' for word in words[:-1]]) + '.' + last_word

print(abbreviated_name)