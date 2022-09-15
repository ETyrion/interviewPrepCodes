# def say_my_name(my_name):
#     print('My name is {}'.format(my_name))
#     swap_case = my_name.swapcase()
#
# say_my_name('John')

def func_2(**name):
    print(**name.items())

name_dict = {'name': 'Ginny', 'Designation': 'Lead QA'}
dict_obj= func_2(name_dict)
