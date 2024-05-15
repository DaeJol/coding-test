import sys
input = sys.stdin.readline

trees = {}
count = 0
while True:
    tree = input().rstrip()
    if tree == '':
        break

    trees[tree] = trees.get(tree, 0) + 1   
    count += 1  

sortedTree = sorted(trees)
for name in sortedTree:
    print(name, "%.4f" %((trees[name] / count) * 100))