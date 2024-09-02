# Merge multiple dictionaries into one dictionary, handling conflicts.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'d': 5}

merged_dict = {**dict1, **dict2, **dict3}
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4, 'd': 5}

# Given a list of dictionaries, extract values from specific keys and create a new list.
data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 35}]

names = [d['name'] for d in data if 'name' in d]
print(names)  # Output: ['Alice', 'Bob', 'Charlie']