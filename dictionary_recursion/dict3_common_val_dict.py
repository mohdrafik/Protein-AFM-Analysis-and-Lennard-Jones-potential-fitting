# Given a dictionary of lists,
# find the common elements in all lists.
data = {'list1': [1, 2, 3], 'list2': [2, 3, 4], 'list3': [3, 4, 5]}

common_elements = set(data['list1'])
for key, value in data.items():
    common_elements.intersection_update(value)

print(common_elements)  # Output: {3}