c = str()
words = str()
number = int(0)

text = open("dataset_3363_3.txt", 'r')
s = text.read().replace('\n', ' ').lower().split()
text.close()
print(s)
d = list(s)
print(d)
for key in d:
    print(key, d.count(key))
    if d.count(key) > number:
        words = key
        number = d.count(key)


with open('finish1.txt', 'w') as out:
    x = out.write(words + ' ' + str(number))


