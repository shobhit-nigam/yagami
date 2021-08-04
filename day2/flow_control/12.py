basket_a = ['apple', 'banana', 'pear', 'apple', 'kiwi', 'banana', 'avocado', 'banana', 'banana']
basket_b = {'orange', 'plum', 'grapes', 'apple', 'pear', 'raspberry'}

banana_index = []

for fruit in basket_a:
    if fruit in basket_b:
        print(fruit)
