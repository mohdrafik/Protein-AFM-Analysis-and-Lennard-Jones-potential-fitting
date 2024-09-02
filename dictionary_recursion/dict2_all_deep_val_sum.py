# Given a nested dictionary, 
# calculate the sum of all values at the deepest level.

data = {'a': {'b': {'c': 1, 'd': 2}}, 'e': {'f': 3}}

def sum_deepest_values(d):
    total = 0
    for key, value in d.items():
        if isinstance(value, dict):
            total += sum_deepest_values(value)
#             sum_deepest_values(value)
        else:
            total += value
    return total

result = sum_deepest_values(data)
print(result)  # Output: 6 (1 + 2 + 3)
