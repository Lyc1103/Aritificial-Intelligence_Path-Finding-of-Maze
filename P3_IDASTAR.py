# Reference:
# https://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php
import time
import heapq
import sys
import numpy as np
print("\n============= P3_IDASTAR =============")
# Calculate execution time
_start_time = time.time()


# Global Variable
hight = 1000
width = 1000
maze = [[0] * hight for i in range(width)]


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.visited_adjacent = []
        # Set distance to infinity for all nodes
        self.distance = sys.maxsize
        # Set cost to infinity for all nodes
        self.cost = sys.maxsize
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None
        # Level
        self.level = int(0)

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def set_cost(self, costs):
        self.cost = costs

    def set_visited(self):
        self.visited = True

    def set_unvisited(self):
        self.visited = False

    def set_previous(self, prev):
        self.previous = prev

    def set_level(self, level):
        self.level = level

    def reset(self):
        for i in range(len(self.visited_adjacent)):
            self.visited_adjacent.pop()
        self.distance = sys.maxsize
        self.cost = sys.maxsize
        self.adjacent_num = 0
        self.visited = False
        self.level = 0
        if self.id != '1_1':
            self.previous = None
# end class Vertex


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous
# end class Graph


def InitializeTheGraph(path_g, maze, hight, width):
    for i in range(1, hight-1):
        for j in range(1, width-1):
            if maze[i][j] != '*':
                path_g.add_vertex(str(i) + '_' + str(j))

    for i in range(1, hight-1):
        for j in range(1, width-1):
            if maze[i][j] != '*':
                if maze[i][j+1] != '*':  # east has path
                    path_g.add_edge((str(i) + '_' + str(j)),
                                    (str(i) + '_' + str(j+1)),
                                    int(10 + (int(maze[i][j]) - int(maze[i][j+1]))**2))
                if maze[i+1][j] != '*':  # south has path
                    path_g.add_edge((str(i) + '_' + str(j)),
                                    (str(i+1) + '_' + str(j)),
                                    int(10 + (int(maze[i][j]) - int(maze[i+1][j]))**2))
                if maze[i][j-1] != '*':  # west has path
                    path_g.add_edge((str(i) + '_' + str(j)),
                                    (str(i) + '_' + str(j-1)),
                                    int(10 + (int(maze[i][j]) - int(maze[i][j-1]))**2))
                if maze[i-1][j] != '*':  # north has path
                    path_g.add_edge((str(i-1) + '_' + str(j)),
                                    (str(i) + '_' + str(j)),
                                    int(10 + (int(maze[i][j]) - int(maze[i-1][j]))**2))
# end func InitializeTheGraph


def PrintMaze(m, h, w):
    for i in range(h):
        for j in range(w):
            print(m[i][j] + "  ", end='')
        print()
# end func PeintMaze


def ShortestPath(v, path):
    # make shortest path from v.previous
    if v.previous:
        path.append(v.previous.id)
        ShortestPath(v.previous, path)
    return
# end func Shor


def ResetPath(target, path):
    while len(path):
        path.pop()
    path.append(target.id)
    return
# end func ResetPath


def DLSSTAR(start, target, limit, cost, path):
    unvisited_queue = [(start.distance, start.id, start)]

    while len(unvisited_queue):
        heapq.heapify(unvisited_queue)
        uv = heapq.heappop(unvisited_queue)
        current = uv[2]
        current.set_visited()

        if current.id == target.id:
            cur_cost = current.cost
            if cur_cost < cost:
                cost = current.cost
                ResetPath(target, path)
                ShortestPath(target, path)
            continue
        if current.level == limit:
            continue

        for next in current.adjacent:
            if next.visited:
                continue

            next_id = next.id.split('_')
            id_y = int(next_id[0])
            id_x = int(next_id[1])
            new_dist = current.distance + current.get_weight(
                next) + ((width-2) - id_x) + ((hight-2) - id_y)
            new_cost = current.cost + current.get_weight(next)
            if new_cost < next.cost:
                next.set_distance(new_dist)
                next.set_cost(new_cost)
                next.set_previous(current)
                next.level = current.level + 1
                heapq.heappush(unvisited_queue,
                               (next.distance, next.id, next))
# end func DLSSTAR


def IDDFSSTAR(aGraph, start, target, limit, path):
    cost = sys.maxsize
    for i in range(1, limit):
        # Set the diatance for the start node to zero
        start.set_distance(0)
        # Set the cost for the start node to zero.
        # Because we use ".distance" to filter the future path to take,
        # so the cost must be calculated separately, in case the long
        # way around but lower energy consumption is ignored.
        start.set_cost(0)
        start.set_level(0)
        DLSSTAR(start, target, i, cost, path)
        for v in aGraph:
            v.reset()
# end fund IDDFSSTAR


def MakePathOfMaze(maze, path, path_of_maze, hight, width):
    cost = 0
    for i in range(hight):
        for j in range(width):
            path_of_maze[i][j] = maze[i][j]
    for i in range(len(path)-1, 0, -1):
        now_pos = path[i].split('_')
        now_pos_r = int(now_pos[0])
        now_pos_c = int(now_pos[1])
        next_pos = path[i-1].split('_')
        next_pos_r = int(next_pos[0])
        next_pos_c = int(next_pos[1])
        cost = cost + 10 + \
            (int(maze[now_pos_r][now_pos_c]) -
             int(maze[next_pos_r][next_pos_c]))**2
        if next_pos_c - now_pos_c == 1:
            path_of_maze[next_pos_r][next_pos_c] = '>'
        elif next_pos_r - now_pos_r == 1:
            path_of_maze[next_pos_r][next_pos_c] = 'v'
        elif next_pos_c - now_pos_c == -1:
            path_of_maze[next_pos_r][next_pos_c] = '<'
        elif next_pos_r - now_pos_r == -1:
            path_of_maze[next_pos_r][next_pos_c] = '^'
    path_of_maze[1][1] = 'S'
    path_of_maze[hight-2][width-2] = 'T'

    return cost
# end func MakePathOfMaze


def SysExit():
    _end_time = time.time()
    _exec_time = _end_time - _start_time
    print("Execution time = %f sec" % (_exec_time))
    return _exec_time
# end func SysExit


def WriteToOutputFile(path_of_maze, path, h, w, exec_time):
    with open("P3_IDASTAR_output.txt", mode="w") as file:
        file.write("The shortest path in maze is :\n")
        for i in range(h):
            for j in range(w-1):
                file.write(path_of_maze[i][j] + ' ')
            file.write(path_of_maze[i][width-1] + '\n')
        file.write("\nThe shortest path in a list is :\n" + str(path[::-1]))
        file.write("\nThe execution time = " + str(exec_time) + " sec\n")
# end func WriteToOutputFile


if __name__ == '__main__':
    hight = 0
    with open("input.txt", mode="r") as file:
        for line in file:
            width = len(line) - 1
            for j in range(width):
                maze[hight][j] = line[j]
            hight = hight + 1

    if maze[1][1] == '*' or maze[hight-2][width-2] == '*':
        print()
        print("No solution ! ( start or end position is '*' )")
        SysExit()
        sys.exit()

    path_g = Graph()
    InitializeTheGraph(path_g, maze, hight, width)

    start_vertex = path_g.get_vertex('1_1')
    target_vertex = path_g.get_vertex((str(hight-2) + '_' + str(width-2)))

    path = [target_vertex.id]
    IDDFSSTAR(path_g, start_vertex, target_vertex, (hight-2)*(width-2), path)
    if path[len(path)-1] == target_vertex.id and (hight != 3 or width != 3):
        print()
        print("No solution ! ( There is no route from the start-position to the end-position )")
        SysExit()
        sys.exit()

    path_of_maze = [[0] * (width) for i in range(hight)]
    cost = MakePathOfMaze(maze, path, path_of_maze, hight, width)

    print("\nThe shortest path in maze is :")
    PrintMaze(path_of_maze, hight, width)
    print("\nThe shortest path in a list is :\n%s" % (path[::-1]))
    print("The cost is : %d\n" % (cost))

    exec_time = SysExit()
    WriteToOutputFile(path_of_maze, path, hight, width, exec_time)
# end main
