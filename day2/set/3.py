basket_a = {'apple', 'banana', 'pear', 'apple', 'kiwi', 'banana', 'avocado'}
basket_b = {'orange', 'plum', 'grapes', 'apple', 'pear', 'raspberry'}

print(type(basket_a))
print("basket_a =", basket_a)
print("basket_b =", basket_b)

# union
print("basket_a | basket_b =", basket_a|basket_b)
print("------")
# intersection
print("basket_a & basket_b =", basket_a&basket_b)
print("------")
# difference
print("basket_a - basket_b =", basket_a-basket_b)
print("------")
# symm difference
print("basket_a ^ basket_b =", basket_a^basket_b)
