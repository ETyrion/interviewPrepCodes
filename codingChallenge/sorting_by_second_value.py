employees = {'John': ('London', 4000, 28), 'Maria':('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}

print(employees.items())

for x in employees.items():
    key = x[1][0]
    print(key)