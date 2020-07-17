dict1 = {'a': 2, 'b': 4, 'c': 5, 'd': 9}
dict2 = {key: ('Foo' if value%3 == 0 else 'Bar' if value%5 == 0 else value) for (key, value) in dict1.items()}
print(dict2)