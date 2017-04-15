import fileinput
from Queue import Queue


def flipped(S):
    def opposite(e):
        if e == '+':
            return '-'
        else:
            return '+'

    return ''.join([opposite(s) for s in S ])


def neighbors(S, K):
    n = []
    for i in xrange(len(S) - K + 1):
        n.append(S[:i] + flipped(S[i: i + K]) + S[i + K:])

    return n


def possible(S, K):
    visited = set()
    Q = Queue()
    D = Queue()

    D.put(0)
    Q.put(S)
    visited.add(S)

    while not Q.empty():
        current = Q.get()
        depth = D.get()

        if current.count('+') == len(current):
            return depth
        else:
            adjacent = neighbors(current, K)
            for node in adjacent:
                if node not in visited:
                    visited.add(node)
                    Q.put(node)
                    D.put(depth + 1)

    return 'IMPOSSIBLE'


for i, line in enumerate(fileinput.input()):
	L = line.split(' ')

	if len(L) == 2:
		S = str(L[0])
		K = int(L[1])

		print "Case #{}: {}".format(i, possible(S, K))



