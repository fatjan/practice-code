# write your Python solution here
def find_target(arr, k):
    keep = {}
    n = len(arr)
    for i in range(n):
        compliment = k - arr[i]
        if compliment not in keep:
            keep[compliment] = i
    
    for i in range(n):
        compliment = k - arr[i]
        if compliment in keep and keep[compliment] != i:
            return True
    
    return False

string = input()
n = len(string)
string = string[2:n-1]

sub_string = string.split(",")
arr = []
for sub in sub_string:
    if "[" in sub:
        sub = sub.replace("[", "")
    if "]" in sub:
        sub = sub.replace("]", "")
    arr.append(int(sub))

print(find_target(arr[:len(arr)-1], arr[-1])) 