def lfsr(seed, taps, length):
    sr = seed.copy()
    result = []

    for _ in range(length):
        result.append(sr[-1])

        feedback = 0
        for tap in taps:
            feedback ^= sr[tap]

        sr = [feedback] + sr[:-1]

    return result

seed = [1, 0, 1, 1]
taps = [0, 1]

sequence = lfsr(seed, taps, 100)

ones = sequence.count(1)
zeros = sequence.count(0)

print("=== Randomness Test Results ===")
print("Total Bits:", len(sequence))
print("Ones:", ones)
print("Zeros:", zeros)