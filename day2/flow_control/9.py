basket_a = ['apple', 'banana', 'pear', 'apple', 'kiwi', 'banana', 'avocado', 'banana', 'banana']
basket_b = {'orange', 'plum', 'grapes', 'apple', 'pear', 'raspberry'}

banana_index = []

for i in range(len(basket_a)):
    if basket_a[i] == 'ananas':
        banana_index.append(i)
    if len(banana_index) == 2:
        break
    else:
        print("occurence is less than two times ")

print(banana_index)
