# Generate the Golomb Sequence using Python
# Input how many numbers we want to generate
def golomb(limit):
    sequence = [1, 2, 2]
    i = 2
    while i < limit:
        # sequence[index] = how many times the number index + 1 shows up in the array
        count = sequence[i]
        for _ in range(count):
            sequence.append(i+1)
        i += 1
    return sequence

limit = int(input("Enter the last number of the sequence: "))
print(golomb(limit))