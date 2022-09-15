div_list = list()
for div in range(1500,3201):
    if div% 5 !=0 and div % 7 ==0:
        div_list.append(str(div))

print(','.join(div_list))




