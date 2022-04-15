def checkMag(magazine, note):
    cond = 'Yes'
    for item in note:
        if item in magazine:
            magazine.remove(item)
        else:
            cond = 'No'
    
    return cond

print(checkMag(['give', 'me', 'one', 'grand', 'today', 'night'], ['give', 'one', 'grand', 'today']))