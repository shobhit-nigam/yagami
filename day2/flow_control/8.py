basket_a = ['apple', 'banana', 'pear', 'apple', 'kiwi', 'banana', 'avocado', 'banana']
basket_b = {'orange', 'plum', 'grapes', 'apple', 'pear', 'raspberry'}

banana_index = []

for i in range(len(basket_a)):
    if basket_a[i] == 'banana':
        banana_index.append(i)

print(banana_index)
