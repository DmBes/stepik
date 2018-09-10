def update_dictionary(d, key, value):
    key += key * (key not in d)
    print(d.get(key, []))
    print(value)

    d[key] = d.get(key, []) + [value]




#def update_dictionary2(d, key, value):
#    (id[key] = d[key], value) if key in d else (d.update({key*2: value})):

d = {}
print(update_dictionary(d, 1, -1))
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)
