import re
import sys

def process_memory(text):
    """
    Process corrupted memory text, handling mul, do(), and don't() instructions.
    Returns the sum of all enabled multiplications.
    """
    # Pattern for mul instructions with capturing groups for numbers
    mul_pattern = r'mul\((\d+),(\d+)\)'
    # Patterns for do and don't instructions
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    
    # Track current position and enabled state
    pos = 0
    enabled = True  # mul instructions start enabled
    total = 0
    
    # Find all instruction matches
    mul_matches = list(re.finditer(mul_pattern, text))
    do_matches = list(re.finditer(do_pattern, text))
    dont_matches = list(re.finditer(dont_pattern, text))
    
    # Combine all matches with their types and sort by position
    all_matches = (
        [(m.start(), 'mul', m) for m in mul_matches] +
        [(m.start(), 'do', m) for m in do_matches] +
        [(m.start(), 'dont', m) for m in dont_matches]
    )
    all_matches.sort()  # Sort by position
    
    # Process all instructions in order
    for pos, type_, match in all_matches:
        if type_ == 'do':
            enabled = True
            print(f"Found do() - Enabling mul instructions")
        elif type_ == 'dont':
            enabled = False
            print(f"Found don't() - Disabling mul instructions")
        elif type_ == 'mul' and enabled:
            x = int(match.group(1))
            y = int(match.group(2))
            result = x * y
            total += result
            print(f"Found enabled mul({x},{y}) = {result}")
        elif type_ == 'mul':
            x = int(match.group(1))
            y = int(match.group(2))
            print(f"Found disabled mul({x},{y}) - skipping")
    
    return total

def process_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
        return process_memory(text)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    result = process_file(filename)
    print(f"\nTotal sum of all enabled multiplications: {result}")

if __name__ == "__main__":
    main()