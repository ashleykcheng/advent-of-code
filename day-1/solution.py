def part_one():

    list_one = []
    list_two = []
    total_distance = 0

    try:
        with open('input.txt', 'r') as file:
            for line in file:
                row = [int(num) for num in line.split()]
                list_one.append(row[0])
                list_two.append(row[1])

            sorted_list_one = sorted(list_one)
            sorted_list_two = sorted(list_two)
            for i in range(len(list_one)):
                total_distance += abs(sorted_list_one[i] - sorted_list_two[i])

        print(total_distance)
        
    except Exception as e:
        print(f"An error occurred: {e}")

def part_two():
    list_one = []
    # list_two = []
    freq_one = {}
    freq_two = {}

    similarity_score = 0

    try:
        with open('input.txt', 'r') as file:
            for line in file:
                one, two = [int(num) for num in line.split()]
                list_one.append(one)
                # list_two.append(two)
                if one not in freq_one:
                    freq_one[one] = 0
                if two not in freq_two:
                    freq_two[two] = 0
                freq_one[one] += 1
                freq_two[two] += 1

        for num in list_one:
            if num in freq_two:  
                similarity_score += num * freq_two[num]
        return similarity_score
        
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    print(part_two())