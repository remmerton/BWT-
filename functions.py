########################### BWT code  ######################

# Function to compute the Burrows-Wheeler Transform (BWT) of a given string
def bwt(s):
    s = s + '$'

    # Compute all rotations of the string
    rotations = []
    for i in range(len(s)):
        rotation = s[i:] + s[:i]
        rotations.append(rotation)

    # Sort the rotations
    sorted_rotations = sorted(rotations)

    # Create the BWT by taking the last character of each sorted rotation
    bwt_result = ''.join(rotation[-1] for rotation in sorted_rotations)

    return bwt_result


# Function to reverse the Burrows-Wheeler Transform (BWT) of a given string
def ibwt(bwt_result):
    # Initialize the table with empty strings
    table = [""] * len(bwt_result)

    # Perform the required number of iterations
    for _ in range(len(bwt_result)):
        # Insert the BWT string as the first column and sort the table
        table = sorted([bwt_char + row for bwt_char, row in zip(bwt_result, table)])

    # Find the row that ends with '$' and return the original string without '$'
    for row in table:
        if row.endswith('$'):
            return row[:-1]


# function to find overlapping string
def overlapping_subsequences(sequence, length, overlap):
    if length < 1 or overlap < 0:
        raise ValueError("Length must be positive and overlap must be non-negative")

    subsequences = []
    step = length - overlap

    for i in range(0, len(sequence) - length + 1, step):
        subsequences.append(sequence[i:i + length])

    return subsequences


########################### data generation code ######################

# Function to generate fibonacci word
def generate_fibonacci_word(order, alphabet):
    if order < 0:
        raise ValueError("Order must be a non-negative integer")
    if len(alphabet) != 2:
        raise ValueError("Alphabet must contain exactly two characters")

    fib_words = [alphabet[0], alphabet[1]]

    for i in range(2, order + 1):
        fib_words.append(fib_words[-1] + fib_words[-2])

    return fib_words[order]
