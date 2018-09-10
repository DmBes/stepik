'''''
first_l, first_r, sec_l, sec_r = int(input()), int(input()),int(input()), int(input()),
for x in range(first_l,first_r):
    for y in range(sec_l,sec_r):
        print(x*y, end='')
'''''


def calc(a, b, c, d):
    print(end='\t')
    for www in range(c, d+1):
        print(www, end='\t')
    print()
    for x in range(a, b+1):
        print(x, end='\t')
        for y in range(c, d+1):

            print(x * y, end='\t')
        print()



a, b, c, d = int(input()), int(input()), int(input()), int(input())
calc(a, b, c, d)


a,b,c,d=(int(input())),(int(input())),(int(input())),(int(input()))
for y in range(c,d+1):
    print('\t',y,end='')
for x in range(a,b+1):
    print('\n',x,end='')
    for y in range(c,d+1):
        print('\t',y*x,end='')
print()

