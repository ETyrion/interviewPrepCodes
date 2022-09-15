my_dict = { "Steve" : 5000, "Jim" : 2000, "Dwight" : 10000 }

total_sum= 0

for v in my_dict.values():
    total_sum = total_sum+v

print(total_sum)

# printing all keys of dictionary

dict_keys = my_dict.keys()
print(dict_keys)

dict_vals = my_dict.values()

print(dict_vals)

print(max(dict_vals))

print(sum(dict_vals))
print(min(dict_vals))

for k,v in my_dict.items():
    print(f'{k} : {v}')
