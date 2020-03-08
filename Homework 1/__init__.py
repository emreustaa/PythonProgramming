// Most frequently word in string.

text = "John is the son John second second son of John second is William second"
dict = {}

for word in text.split():
    x = dict.setdefault(word)
    if x is not None:
        dict[word] = dict.get(word) + 1
    else:
        dict[word] = 1

maxWord = max(dict, key=dict.get)
print("Most Frequent word is : " , maxWord)

dict = {}

dict = {key: text.split().count(key) for key in text.split()}
maxWord = max(dict, key=dict.get)
print("Most Frequent word is : " + maxWord)
