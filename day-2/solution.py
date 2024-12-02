def main():
    def safeDiff(one, two):
        return 1 <= abs(one - two) <= 3

    def isSafeLevel(line):
        if len(line) <= 1:
            return True
        
        # decreasing
        if line[0] > line[1]:
            for i in range(len(line) - 1):
                if line[i] < line[i + 1] or not safeDiff(line[i], line[i + 1]):
                    return False
                
        # increasing
        elif line[0] < line[1]:
            for i in range(len(line) - 1):
                if line[i] > line[i + 1] or not safeDiff(line[i], line[i + 1]):
                    return False
        else:
            return False

        return True


    num_safe = 0

    try:    
        with open('input.txt', 'r') as file:

            for line in file:
                line_numbers = [int(num) for num in line.split()]
                if isSafeLevel(line_numbers):
                    num_safe += 1
                else:
                    for i in range(len(line_numbers)):
                        edited_arr = line_numbers[:i] + line_numbers[i+1:]
                        if isSafeLevel(edited_arr):
                            num_safe += 1
                            break

        print(num_safe)
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()