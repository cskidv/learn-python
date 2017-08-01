x = 1
m = 0
z = 0
for _ in range(120):
    if m == 10:
        x = x + 1
        m = m - m + 1
    else:
        m = m + 1
    z = x * m
    print("{} * {} = {}".format(x,m,z))
        
