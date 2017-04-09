from sys import maxint
from collections import Counter
import fileinput

MIN_INT = -maxint - 1

def Ls(stalls, index):
    i = index
    empty_count = 0

    while stalls[i - 1] == 0:
        empty_count += 1
        i -= 1

    return empty_count


def Rs(stalls, index):
    i = index

    empty_count = 0
    while stalls[i + 1] == 0:
        empty_count += 1
        i += 1

    return empty_count


def choose(stalls, N):
    empty_stall_indices = [i for i in xrange(N) if stalls[i] == 0]

    t = []
    for i in empty_stall_indices:
        ls = Ls(stalls, i)
        rs = Rs(stalls, i)
        cost = min(ls, rs)

        if cost > max_cost:
            max_cost = cost
            max_cost_index = i

    return max_cost_index


def kThValue(N, K):
    stalls = Counter()
    stalls[-1] += 1
    stalls[N] += 1

    for _ in xrange(K - 1):
        choice = choose(stalls, N)
        stalls[choice] += 1

    kthChoice = choose(stalls, N)
    ls = Ls(stalls, kthChoice)
    rs = Rs(stalls, kthChoice)

    return max(ls, rs), min(ls, rs)



for i, line in enumerate(fileinput.input()):
    if i != 0:
        L = line.split(' ')

        N = int(L[0])
        K = int(L[1])

        sol = kThValue(N, K)
        print 'Case #{}: {} {}'.format(i, sol[0], sol[1])








