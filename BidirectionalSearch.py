import time
import heapq
import sys
import numpy as np
print("\n============= Bidirectional Search =============")
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
        # Set distance to infinity for all nodes
        self.distance = sys.maxsize
        # Mark all nodes unvisited
        self.forward_visited = False
        self.backward_visited = False
        # Predecessor
        self.parent = None
        self.child = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def set_forward_visited(self):
        self.forward_visited = True

    def set_backward_visited(self):
        self.backward_visited = True

    def set_parent(self, pare):
        self.parent = pare

    def set_child(self, chil):
        self.child = chil
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


def ShortestPath(connect_vertex, path):
    v = connect_vertex
    # make shortest path from child
    tmp = []
    while v.child:
        tmp.append(v.child.id)
        v = v.child
    # Inverted
    while len(tmp):
        path.append(tmp.pop())

    v = connect_vertex
    path.append(v.id)

    # make shortest path from parent
    while v.parent:
        path.append(v.parent.id)
        v = v.parent
    return
# end func Shor


def BFS(stack, dir):
    current = stack.pop()

    if dir == 'f':
        for next in current.adjacent:
            if not next.forward_visited:
                stack.append(next)
                next.set_forward_visited()
                next.set_parent(current)
    elif dir == 'b':
        for next in current.adjacent:
            if not next.backward_visited:
                stack.append(next)
                next.set_backward_visited()
                next.set_child(current)
# end func BFS


def CheckConnect(aGraph):
    for v in aGraph:
        if v.backward_visited and v.forward_visited:
            return v.id
    return 'NotConnect'
# end func CheckConnect


def BidirectionSearch(path_g, start, target):
    forward_stack = []
    forward_stack.append(start)
    start.set_forward_visited()
    # start.parent = 'root_start'

    backward_stack = []
    backward_stack.append(target)
    target.set_backward_visited()
    # target.child = 'root_end'

    while len(forward_stack) and len(backward_stack):
        BFS(forward_stack, 'f')
        BFS(backward_stack, 'b')
        connect_id = CheckConnect(path_g)
        if connect_id != 'NotConnect':
            return connect_id
    return 'False'
# end func BidirectionSearch


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
    with open("BidirectionalSearch_output.txt", mode="w") as file:
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
    # start_path_g = Graph()
    # target_path_g = Graph()
    # InitializeTheGraph(start_path_g, maze, hight, width)
    # InitializeTheGraph(target_path_g, maze, hight, width)

    # print("Path of Graph :")
    # for v in path_g:
    #     for w in v.adjacent:
    #         vid = v.id
    #         wid = w.id
    #         print("( %s , %s , %2d )" % (vid, wid, v.get_weight(w)))

    start_vertex = path_g.get_vertex('1_1')
    target_vertex = path_g.get_vertex(
        (str(hight-2) + '_' + str(width-2)))

    # BidirectionSearch(start_path_g, target_path_g, start_vertex, target_vertex)
    connect_id = BidirectionSearch(path_g, start_vertex, target_vertex)
    if connect_id == 'False':
        print()
        print("No solution ! ( There is no route from the start-position to the end-position )")
        SysExit()
        sys.exit()
    connect_vertex = path_g.get_vertex(connect_id)
    # forward_path = [connect_vertex.id]
    # backward_path = [connect_vertex.id]
    path = []
    ShortestPath(connect_vertex, path)

    # path = [target_vertex.id]
    # ShortestPath(target_vertex, path)
    # if path[len(path)-1] == target_vertex.id and (hight != 3 or width != 3):
    #     print()
    #     print("No solution ! ( There is no route from the start-position to the end-position )")
    #     SysExit()
    #     sys.exit()

    path_of_maze = [[0] * (width) for i in range(hight)]
    cost = MakePathOfMaze(maze, path, path_of_maze, hight, width)

    print("\nThe shortest path in maze is :")
    PrintMaze(path_of_maze, hight, width)
    print("\nThe shortest path in a list is :\n%s" % (path[::-1]))
    print("The cost is : %d\n" % (cost))

    exec_time = SysExit()
    WriteToOutputFile(path_of_maze, path, hight, width, exec_time)
# end main
