# removing any charcter

language = '$$$ABCDEF$$$'
language1 = language.strip('$')
print(language1)

language2 = language1.lower()
print(language2)

message = 'I love Python!'

# replacing a character

message1 = message.replace('Python', 'Java')

print(message1)