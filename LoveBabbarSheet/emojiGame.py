emoji_dict = {":)" : "🙂",
              ":(": "😞"}

input_str = "I am happy :)"
op =""
split_string= input_str.split(" ")
print(split_string[3])

for i in split_string:
    op = op + emoji_dict.get(i, i) + " "

print(op)
