input_file = 'input.txt'
contents = []

with open(input_file) as f:
    contents = f.readlines()

def answerFunction(incoming: list[str]):
    sequences = [
        [[[1,-1], [1,1]], [[0,0], [0,0]], [[-1,1], [-1, -1]]],
        [[[1,-1], [-1,-1]], [[0,0], [0,0]], [[-1,1], [1, 1]]],
        [[[-1,1], [1,1]], [[0,0], [0,0]], [[1,-1], [-1, -1]]],
        [[[-1,1], [-1,-1]], [[0,0], [0,0]], [[1,-1], [1, 1]]],
    ]
    def validCoords(x, y):
        return x >= 0 and y >= 0 and x < len(incoming[0]) and y < len(incoming)

    search = 'MAS'
    total = 0
    for y in range(len(incoming)):
        for x in range(len(incoming[0])):
            for seq in sequences:
                valid = True
                for i in range(len(search)):
                    xNext1, yNext1 = x + seq[i][0][0], y + seq[i][0][1]
                    xNext2, yNext2 = x + seq[i][1][0], y + seq[i][1][1]
                    if validCoords(xNext1, yNext1) and validCoords(xNext2, yNext2) and incoming[yNext1][xNext1] == search[i] and incoming[yNext2][xNext2] == search[i]:
                        continue
                    valid = False
                    break
                if valid:
                    total += 1

    return total

def assertExamples():
    assert answerFunction([
        'MMMSXXMASM',
        'MSAMXMSMSA',
        'AMXSXMAAMM',
        'MSAMASMSMX',
        'XMASAMXAMM',
        'XXAMMXXAMA',
        'SMSMSASXSS',
        'SAXAMASAAA',
        'MAMMMXMMMM',
        'MXMXAXMASX',
    ]) == 9
    pass

assertExamples()

ans = answerFunction(contents)

print(ans)