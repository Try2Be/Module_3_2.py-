def print_params(a = 1, b = 'строка', c = True):
    print(f"a: {a}, b: {b}, c: {c}")


print_params(b = 25)
print_params(c = [1,2,3])
value_list = [ 1, 1.55, False ]
value_dict = { 'a': 1, 'b': 'строка' , 'c': False }

print_params(*value_list)
print_params(**value_dict)
value_list_2 = [ 1, True ]
print_params(*value_list_2, 42)