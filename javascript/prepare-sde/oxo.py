def minimumMoves(s):
    moves = 0
    i = 0
    if ('X' not in s):
        return moves
    
    while (i < len(s)):
        if (s[i] == 'O'):
            i += 1
            continue
        
        if (i == len(s) - 1):
            if ('X' in s[-1]):
                moves += 1
                i += 1

        elif (i == len(s) - 2):
            if ('X' in s[-2:]):
                moves += 1
                i += 2
                
        elif ('X' in s[i:i+3]):
            moves += 1
            i += 3

        print('moves ', moves);
        print('i ', i);

    return moves

print(minimumMoves("OXOX"))
