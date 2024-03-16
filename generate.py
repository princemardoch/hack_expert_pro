import string

l = string.ascii_uppercase

for i in l:
    for ii in range(10000):
        a = f'{str(i)+str(ii).zfill(4)}\n'
        with open('admin_ids.txt', 'a') as ww:
            ww.write(a)