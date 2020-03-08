items = ['computer', 'phone', 'tv', 'tv', 'computer', 'tv', 'game console', 'tv', 'computer']
list = {item: items.count(item) for item in items}
tuples = tuple((item, count) for item, count in list.items())
print(tuples)