basket_a = ['apple', 'banana', 'pear', 'apple', 'kiwi', 'banana', 'avocado', 'banana', 'banana']
basket_b = {'orange', 'plum', 'grapes', 'apple', 'pear', 'raspberry'}

dict_a = {}

for fruit in basket_a:
    if fruit not in dict_a:
        dict_a[fruit] = 1
    else:
        dict_a[fruit] = dict_a[fruit] + 1

print(dict_a)
