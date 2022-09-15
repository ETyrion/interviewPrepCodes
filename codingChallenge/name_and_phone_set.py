name_list = ["Dan", "John", "Diana"]
phones = [11111, 2222, 3333]

name_phone_set = set(zip(name_list, phones))
print(name_phone_set)

phone_name_set = set(zip(phones, name_list))
print(phone_name_set)