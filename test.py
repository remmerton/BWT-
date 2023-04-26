import random
import itertools
import matplotlib.pyplot as plt

# Generate a Fibonacci word
def generate_fibonacci_word(n):
    a, b = "A", "B"
    for _ in range(n):
        a, b = b, a + b
    return a

# Generate a random word
def generate_random_word(length):
    return "".join(random.choice("AB") for _ in range(length))

# Function to extract overlapping subsequences
def overlapping_subsequences(sequence, length, overlap):
    subsequences = []
    step = length - overlap
    for i in range(0, len(sequence) - length + 1, step):
        subsequences.append(sequence[i:i + length])
    return subsequences

# Function to perform Burrows-Wheeler Transform
def bwt(s):
    return ''.join(t[-1] for t in sorted(s[i:] + s[:i] for i in range(len(s))))

# Generate a Fibonacci word of order 22 and a random word of the same length
fib_word = generate_fibonacci_word(22)
rand_word = generate_random_word(len(fib_word))

# Test parameters
m_values = [50, 100, 200, 400, 1000]

# Generate d_values according to the minimum value in m_values
min_m = min(m_values)
d_values = range(1, min_m)

# Perform the test and store the results
results = {}
for word_type, word in [("Fibonacci", fib_word), ("Random", rand_word)]:
    for m in m_values:
        for d in d_values:
            subsequences = overlapping_subsequences(word, m, d)
            bwt_subsequences = [bwt(subsequence) for subsequence in subsequences]
            num_phrases = len(set(bwt_subsequences))
            results[(word_type, m, d)] = num_phrases

# Visualize the results using a plot with a logarithmic scale for the number of phrases
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
for idx, (word_type, ax) in enumerate(itertools.product(["Fibonacci", "Random"], [0, 1])):
    data = {(m, d): num_phrases for (wt, m, d), num_phrases in results.items() if wt == word_type}
    for m in m_values:
        x = [d for d in d_values]
        y = [data[(m, d)] for d in d_values]
        axes[idx // 2, ax].plot(x, y, label=f"m = {m}")
        axes[idx // 2, ax].set_yscale("log")
        axes[idx // 2, ax].set_title(f"{word_type} word ({'string order' if ax == 0 else 'random order'})")
        axes[idx // 2, ax].set_xlabel("d")
        axes[idx // 2, ax].set_ylabel("Number of phrases (log scale)")
        axes[idx // 2, ax].legend()
plt.show()
