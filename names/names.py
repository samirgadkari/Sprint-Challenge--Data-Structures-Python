import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


class Node:
    def __init__(self):
        self.storage = {}


END_CHAR = '*'


def show_dict(dict, spaces):
    res = []
    for k, v in dict.storage.items():
        res.append(f"'{k}': ")
        if v is not True:
            res.append(show_dict(v, spaces + 2))
    return ' ' * spaces + '{' + ','.join(res) + '}'


class SuffixTree:
    def __init__(self):
        self.root = Node()

    def __str__(self):
        return show_dict(self.root, 0)

    def insert_string(self, s):
        cur = self.root
        for c in s:
            if c in cur.storage:
                cur = cur.storage[c]
            else:
                cur.storage[c] = Node()
                cur = cur.storage[c]
        cur.storage[END_CHAR] = True

    def contains(self, s):
        cur = self.root
        for c in s:
            if c not in cur.storage:
                return False
            cur = cur.storage[c]

        if (END_CHAR in cur.storage) and (cur.storage[END_CHAR] is True):
            return True

        return False


# Suffix Tree test code here
#
# tree = SuffixTree()
# for s in ['aabc', 'abc', 'cba']:
#     tree.insert_string(s)

# print(tree)

# print('tree contains aa:', tree.contains('aa'))
# print('tree contains aabc:', tree.contains('aabc'))
# print('tree contains abc:', tree.contains('abc'))
# print('tree contains cba:', tree.contains('cba'))

tree = SuffixTree()
for name_1 in names_1:
    tree.insert_string(name_1)

duplicates = []
for name_2 in names_2:
    if tree.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
