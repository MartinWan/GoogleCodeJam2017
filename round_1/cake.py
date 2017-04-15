from fileinput import input

def fill_row(row):
    N = len(row)
    filled_indices = [i for i, e in enumerate(row) if e != '?']

    filled_row = list(row)
    for filled_index in filled_indices:
        l = filled_index - 1
        while l > -1 and filled_row[l] == '?':
            filled_row[l] = filled_row[filled_index]
            l -= 1

        r = filled_index + 1
        while r < N and filled_row[r] == '?':
            filled_row[r] = filled_row[filled_index]
            r += 1

    return ''.join(filled_row)

def decorate_cake(grid):
    R = len(grid)
    C = len(grid[0])

    fd = 0
    while grid[fd].count('?') == C:
        fd += 1
    # gets first decorated row

    for i in range(fd):
        grid[i] = grid[fd]
    # fills rows before first decorated row with first decorated row

    for k in range(R):
        if grid[k].count('?') == C: # empty
            grid[k] = grid[k - 1]

        grid[k] = fill_row(grid[k])

    return grid



lines = [line for line in input()]

i = 1
case_count = 1
while i < len(lines):
    tokens = lines[i].split()

    if len(tokens) == 2:
        R, C = int(tokens[0]), int(tokens[1])

        cake = lines[i + 1: i + 1 + R]
        parsed_cake = [r.replace('\n', '') for r in cake] # remove \n

        print 'Case #{}:'.format(case_count)
        decorated_cake = decorate_cake(parsed_cake)
        for row in decorated_cake:
            print row

        case_count += 1
        i += R + 1
    else:
        raise BaseException('Invalid input')











