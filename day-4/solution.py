def main():
    def dfs(i, j, direction, pattern_idx):
        if not (0 <= i < len(arr) and 0 <= j < len(arr[0])):
            return False

        if arr[i][j] != 'XMAS'[pattern_idx]:
            return False

        if pattern_idx == 3:
            return True

        dx, dy = direction
        return dfs(i + dx, j + dy, direction, pattern_idx + 1)

    try:    
        with open('input.txt', 'r') as file:
            arr = []
            for line in file:
                arr.append(line.strip())

        directions = [
            (0, 1),   # right
            (1, 0),   # down
            (0, -1),  # left
            (-1, 0),  # up
            (1, 1),   # down-right
            (-1, 1),  # up-right
            (1, -1),  # down-left
            (-1, -1), # up-left
        ]

        count = 0

        for i in range(len(arr)):
            for j in range(len(arr[0])):

                if arr[i][j] == 'X':

                    for direction in directions:
                        if dfs(i, j, direction, 0):
                            count += 1

        return count

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print(f"Final count: {main()}")