a1 = open('dataset_3363_3.txt').read().lower().strip().split()

print(a1)

text = open("dataset_3363_3.txt", 'r')
s = text.read().replace('\n', ' ').lower().split()
text.close()
print(s)

text = open("dataset_3363_3.txt", 'r')
bbb = str(text.readlines()).lower().strip()
print(type(bbb))
text.close()
print(bbb)
