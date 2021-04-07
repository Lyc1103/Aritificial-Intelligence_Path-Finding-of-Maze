import numpy as np
import sys

# Global Variable
# np.random.seed(1)
# needs to small than 1000 x 1000
hight = 10
width = 10
maze = [[0] * width for i in range(hight)]


def PrintMaze(m):
    for i in range(hight):
        for j in range(width):
            print(m[i][j] + "  ", end='')
        print()
# end func PeintMaze


def MazeMaker(maze, h, w):
    for i in range(h):
        for j in range(w):
            if i == 0 or j == 0 or i == h-1 or j == w-1:
                maze[i][j] = '*'
            # Set no solution statement
            # elif (i == h - 3 and j == w-2) or (i == h - 2 and j == w-3):
            #     maze[i][j] = '*'
            else:
                tmp = int(np.random.random()*12)
                if tmp >= 10:
                    maze[i][j] = '*'
                else:
                    maze[i][j] = str(tmp)
# end func MazeRandCreate


if __name__ == '__main__':
    MazeMaker(maze, hight, width)

    print("The maze is :")
    PrintMaze(maze)

    with open("input.txt", mode="w") as file:
        for i in range(hight):
            for j in range(width):
                file.write(str(maze[i][j]))
            file.write('\n')
