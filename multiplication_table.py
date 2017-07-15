
x = raw_input('which multiplication table you would like to see:')
x = int(x)

for i in range(1,11):
    print('{} x {} = {}'.format(x, i, x * i))
