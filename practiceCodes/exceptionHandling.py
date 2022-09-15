a = 4
b=0

try:
    c= a/b

except ZeroDivisionError as e:
    print(f'Zero diivision error :{e}')
