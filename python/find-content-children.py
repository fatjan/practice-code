def find_content_children(g, s) -> int:
    if len(s) == 0:
        return 0
    
    g = sorted(g)
    s = sorted(s)

    g_point = 0
    s_point = 0

    content = 0
    while g_point < len(g) and s_point < len(s):
        if g[g_point] <= s[s_point]:
            content += 1
            s_point += 1
            g_point += 1
        elif g[g_point] > s[s_point]:
            s_point += 1
    
    return content

print(find_content_children([1,2,3], [1,1]))
print(find_content_children([1,2], [1,2,3]))
print(find_content_children([10,9,8,7], [5,6,7,8]))
print(find_content_children([1,2,3], [3]))
print(find_content_children([1,2,3], [1,2,3]))
print(find_content_children([1,2,3], [1,1,1]))