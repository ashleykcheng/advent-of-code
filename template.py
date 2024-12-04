def main():

    try:    
        with open('input.txt', 'r') as file:

            for line in file:
                line_numbers = [int(num) for num in line.split()]
                
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()