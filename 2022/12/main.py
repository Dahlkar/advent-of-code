import string
import sys
sys.setrecursionlimit(1500)
heights = {
    l: i
    for i, l in enumerate(string.ascii_lowercase, start=1)
}

class Node:
    def __init__(self, height):
        self.height = height
        self.adjacent = []

    def add_adjacent(self, node):
        if node.height <= self.height or node.height - 1 == self.height:
            self.adjacent.append(node)

def parse_first(file):
    with open(file) as f:
        start = None
        end = None
        grid = []
        for i, line in enumerate(f.read().split('\n')[:-1]):
            row = []
            for j, l in enumerate(line):
                if l in heights:
                    row.append(heights[l])
                elif l == 'S':
                    row.append(heights['a'])
                    start = (i, j)
                elif l == 'E':
                    row.append(heights['z'])
                    end = (i, j)

            grid.append(row)
        return start, end, grid

def parse_second(file):
    with open(file) as f:
        start = []
        end = None
        grid = []
        for i, line in enumerate(f.read().split('\n')[:-1]):
            row = []
            for j, l in enumerate(line):
                if l in ['a', 'S']:
                    row.append(heights['a'])
                    start.append((i, j))
                elif l == 'E':
                    row.append(heights['z'])
                    end = (i, j)
                else:
                    row.append(heights[l])

            grid.append(row)
        return start, end, grid

def shortest_path(grid, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        x, y = last_node
        next_nodes = set()
        height = grid[x][y]
        if x > 0:
            next_node = (ix, iy) = x-1, y
            a_height = grid[ix][iy]
            if (a_height <= height or height == a_height - 1):
                next_nodes.add(next_node)
        if x < len(grid) - 1:
            next_node = (ix, iy) = x+1, y
            a_height = grid[ix][iy]
            if (a_height <= height or height == a_height - 1):
                next_nodes.add(next_node)
        if y > 0:
            next_node = (ix, iy) = x, y-1
            a_height = grid[ix][iy]
            if (a_height <= height or height == a_height - 1):
                next_nodes.add(next_node)
        if y < len(grid[0]) - 1:
            next_node = (ix, iy) = x, y+1
            a_height = grid[ix][iy]
            if (a_height <= height or height == a_height - 1):
                next_nodes.add(next_node)
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            ix, iy = next_node
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []

def first(file):
    start, end, grid = parse_first(file)
    result = shortest_path(grid, start, end)
    visited = set(result)
    for i in range(len(grid)):
        row = ''
        for j in range(len(grid[0])):
            if (i, j) in visited:
                row += '#'
            else:
                row += '.'
        print(row)

    print(len(result)-1)


def second(file):
    starts, end, grid = parse_second(file)
    print(starts)
    paths = []
    for start in starts:
        path = shortest_path(grid, start, end)
        if path:
            paths.append(path)

    print(min([len(path) for path in paths]) - 1)
if __name__ == '__main__':
    first('test.txt')
    first('input.txt')
    second('test.txt')
    second('input.txt')
