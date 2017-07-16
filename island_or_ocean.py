import numpy as np


def read_data(filename):
    is_first_line = True
    with open(filename, 'r') as file:
        for line in file:
            numbers = line.strip().split(' ')
            if is_first_line:
                rows = int(numbers[0])
                cols = int(numbers[1])
                my_map = np.zeros((rows, cols), dtype = np.int)
                is_first_line = False
                row_idx = 0
            else:
                for i in range(cols):
                    my_map[row_idx, i] = int(numbers[i])
                row_idx = row_idx + 1
    file.close()
    print('map size = {} x {}'.format(rows, cols))
    for i in range(rows):
        print(my_map[i,:])
    return my_map

def is_land(my_map, marked, x, y):
    if (x == 0) or \
       (x == my_map.shape[0] - 1) or \
       (y == 0) or \
       (y == my_map.shape[1] - 1):
        return True
    else:
        marked[x, y] = 1
        for (dx, dy) in ((0,-1), (-1,0), (0,1), (1,0)):
            x_new = x + dx
            y_new = y + dy
            if (x_new >= 0) and \
               (y_new >= 0) and \
               (x_new < my_map.shape[0]) and \
               (y_new < my_map.shape[1]) and \
               (my_map[x_new, y_new] == 1) and \
               (marked[x_new, y_new] == 0):
                return is_land(my_map, marked, x_new, y_new)
        return False

def main():

    filename = '/Users/vidu/data/island.txt'
    my_map = read_data(filename)
    marked = np.zeros(my_map.shape, dtype=np.int)
    
    x = int(raw_input('input row number:'))-1
    y = int(raw_input('input column number:'))-1
    if my_map[x, y] == 0:
        print('ocean!')
    else:
        if is_land(my_map, marked, x, y):
            print('land')
        else:
            print('island')

if __name__ == "__main__":
    main()
