import re

def add(numbers):
    if not numbers:
        return 0

    # Default delimiters are comma and newline
    delimiters = [",", "\n"]

    # Check for custom delimiter
    if numbers.startswith("//"):
        delimiter_part, numbers = numbers[2:].split("\n", 1)
        if delimiter_part.startswith("[") and delimiter_part.endswith("]"):
            # Multiple delimiters
            delimiters = re.findall(r'\[(.*?)\]', delimiter_part)
        else:
            # Single character delimiter
            delimiters = [delimiter_part]

    # Create a regex pattern to split by all delimiters
    delimiter_pattern = '|'.join(map(re.escape, delimiters))
    num_list = re.split(delimiter_pattern, numbers)

    total = 0
    negatives = []

    for num in num_list:
        if num:
            n = int(num)
            if n < 0:
                negatives.append(n)
            elif n <= 1000:
                total += n

    if negatives:
        raise ValueError(f"negative numbers not allowed: {', '.join(map(str, negatives))}")

    return total
