s = input()
list_s = s.split()
list_num = []
s_total = ''
list_space_index = []
x = s
chars = '.,:;"!@#$%^&*()'
y = s.translate(str.maketrans('', '', chars))
list_y = y.split()

for _ in range(len(list_s) - 1):
    space_index = x.find(' ')
    x = x.replace(' ', '!', 1)
    list_space_index.append(space_index)

for i in range(len(list_s)):
    list_num += str(len(list_y[i])).split()

for j in range(len(list_num)):
    list_num[j] = int(list_num[j])

for k in range(len(list_s)):
    for o in range(len(list_s[k])):
        if 65 <= ord(list_s[k][o]) <= 90:
            if (ord(list_s[k][o]) + list_num[k]) > 90:
                a = (ord(list_s[k][o]) + list_num[k]) - 26
                s_total += chr(a)
            else:
                a = (ord(list_s[k][o]) + list_num[k])
                s_total += chr(a)
        elif 97 <= ord(list_s[k][o]) <= 122:
            if (ord(list_s[k][o]) + list_num[k]) > 122:
                a = (ord(list_s[k][o]) + list_num[k]) - 26
                s_total += chr(a)
            else:
                a = (ord(list_s[k][o]) + list_num[k])
                s_total += chr(a)
        else:
            a = ord(list_s[k][o])
            s_total += chr(a)

list_total = []
list_total.extend(s_total)
for p in range(len(list_s) - 1):
    list_total.insert(list_space_index[p], ' ')
print(''.join(list_total))
