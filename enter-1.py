import os
os.path.join('E:\\','скачано\\','dataset_3363_2.txt')
with open(os.path.join('E:\\','скачано\\','dataset_3363_2.txt'), 'r') as inf:
    x = inf.readline().strip()
s = 0
zx = []
word = []
biq = str()
digit = []
for k in x:
    if k.isdigit():
        if s > 0:
            digit[len(digit) - 1] = digit[len(digit) - 1] + k
        else:
            digit.append(k)
            s += 1
    else:
        word.append(k)
        s = 0
for q in range(len(word)):
    biq += word[q] * int(digit[q])
with open('finish.txt', 'w') as out:
    x = out.write((biq))