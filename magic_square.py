import numpy as np

count = 0

def find_magic_square(square, marked, i, j):
    global count
    for idx in range(9):
        if marked[idx] == 0:
            square[i, j] = idx + 1
            if i == 2:
                if sum(square[:, j]) != 15:
                    continue
            if j == 2:
                if sum(square[i, :]) != 15:
                    continue
            if i == 2 and j == 0:
                if square[0, 2] + square[1, 1] + square[2, 0] != 15:
                    continue
            if i == 2 and j == 2:
                if square[0, 0] + square[1, 1] + square[2, 2] != 15:
                    continue
                else:
                    count = count + 1
                    print('magic square {}:'.format(count))
                    print(square)
    
            marked[idx] = 1
            if j < 2:
                find_magic_square(square, marked, i, j + 1)
            else:
                if i < 2:
                    find_magic_square(square, marked, i + 1, 0)
            marked[idx] = 0


def main():
    global count
    square = np.zeros((3, 3), dtype=np.int)
    marked = np.zeros(9, dtype=np.int)
    find_magic_square(square, marked, 0, 0)
    print('There are {} 3x3 magic squares'.format(count))

if __name__ == "__main__":
    main()
