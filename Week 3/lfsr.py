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

sequence = lfsr(seed, taps, 20)

print("Pseudorandom Binary Stream:")
print("".join(map(str, sequence)))