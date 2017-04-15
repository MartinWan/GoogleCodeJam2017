import fileinput

def toInt(digitArray):
    digitStrings = [str(digit) for digit in digitArray]
    return int(''.join(digitStrings))


def tidy_up(digits):
    N = len(digits)

    while True:
        k = last_tidy_index(digits)

        if k == N - 1:
            if digits[0] == 0: # remove leading 0
                return digits[1:]
            else:
                return digits
        else:
            digits[k] -= 1
            digits[k + 1] = 9

    raise BaseException('Crap')



# returns k such that digits[k] > digits[k + 1] or k = N - 1 if not found
def last_tidy_index(digits):
    N = len(digits)
    for i in range(N - 1):
        if digits[i] > digits[i + 1]:
            return i

    return N - 1


def already_tidy(digits):
    N = len(digits)
    for i in xrange(N - 1):
        if digits[i] > digits[i + 1]:
            return False

    return True


def nearest_tidy(n):
    digits = [int(d) for d in str(n)]

    if already_tidy(digits):
        return toInt(digits)
    else:
        N = len(digits)
        i = last_tidy_index(digits)

        digits[i] -= 1
        for k in xrange(i + 1, N):
            digits[k] = 9

        return toInt(tidy_up(digits))


for i, line in enumerate(fileinput.input()):
    if i != 0:
        n = int(line)
        print 'Case #{}: {}'.format(i, nearest_tidy(n))

