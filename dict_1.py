b = sorted(list(map(str, input().lower().split())))
def war_peace(b):
    a = set(b)
    for k in a:
        print(k, b.count(k))

war_peace(b)