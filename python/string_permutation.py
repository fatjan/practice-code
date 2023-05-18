import itertools

def solution(P, Q):
    permutations = []
    alpha = []
    string = ''
    for i in range(len(P)):
        string += P[i] + Q[i]
        alpha.append(string)
        string = ''


    for p in itertools.product(*alpha):
        permutations.append(''.join(p))
    
    print(permutations)

K = 'abc'
L = 'bcd'

solution(K, L)
# ['abc', 'abd', 'acc', 'acd', 'bbc', 'bbd', 'bcc', 'bcd']