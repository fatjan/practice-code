def help_cat(nums, child_parent):
    for i in range(len(nums[1:])):
        child_parent[nums[i+1]] = nums[0]
    return child_parent 

paths = []
def get_path(child_parent, parent):
    if parent not in child_parent:
        return
    parent = child_parent[parent]
    paths.append(parent)
    return get_path(child_parent, parent)

child_parent = {}
n = 0

while True:
    line = input()
    if line == '-1':
        break
    elif ' ' not in line:
        n = line
        paths.append(n)
        continue

    words = line.split()
    child_parent = help_cat(words, child_parent)


get_path(child_parent, n)
for i in range(len(paths)-1):
    print(paths[i], end=' ')
print(paths[-1])