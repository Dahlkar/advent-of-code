class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f'{self.name} (file, size={self.size})'


class Dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.files = []
        self.dirs = {}
        self.size = 0

    def __getitem__(self, item):
        return self.dirs[item]

    def add_file(self, name, size):
        self.increase_size(size)
        self.files.append(File(name, size))

    def add_directory(self, name):
        self.dirs[name] = Dir(name, parent=self)

    def increase_size(self, size):
        self.size += int(size)
        if self.parent:
            self.parent.increase_size(int(size))

    def __str__(self):
        return f'''{self.name} (dir) size={self.size}'''

    def __repr__(self) -> str:
        return str(self)

def parse(file):
    with open(file) as f:
        text = f.read()
        fs = {}
        current_dir = None
        tree = None
        for line in text.split('\n'):
            l = line.split(' ')
            if l == ['']:
                break
            if l[0] == '$':
                command = l[1]
                if command == 'cd':
                    if tree is None:
                        tree = Dir(l[2])
                        current_dir = tree
                    elif l[2] == '..':
                        current_dir = current_dir.parent
                    else:
                        current_dir = current_dir[l[2]]
                else:
                    continue
            else:
                if l[0] == 'dir':
                    current_dir.add_directory(l[1])
                else:
                    current_dir.add_file(l[1], l[0])

    return tree

def first(file):
    tree = parse(file)
    def traverse(root):
        result = []
        if root.size <= 100000:
            result.append(root.size)

        for node in root.dirs.values():
            result = result + traverse(node)

        return result

    result = traverse(tree)
    print(sum(result))

def second(file):
    tree = parse(file)

    free_space = 70000000 - tree.size
    needed_space = 30000000 - free_space
    def traverse(root):
        result = []
        if root.size >= needed_space:
            result.append(root.size)

        for node in root.dirs.values():
            result = result + traverse(node)

        return result

    result = traverse(tree)
    print(min(result))

if __name__ == '__main__':
    first('test.txt')
    first('input.txt')
    second('test.txt')
    second('input.txt')
