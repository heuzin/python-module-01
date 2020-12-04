numbers = [22.3, -184.4, 57.8, 99.6, -18.2, 84.2, 71.3]

new_list = []

for n in numbers:
    if n > 0:
        new_list.append(int(n))

print(new_list)