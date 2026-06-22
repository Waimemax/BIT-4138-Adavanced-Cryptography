def xor_difference(a, b):
    """Return the XOR difference between two binary strings."""
    return ''.join('1' if x != y else '0' for x, y in zip(a, b))


print("=" * 50)
print("Differential Cryptanalysis Simulation")
print("=" * 50)

plaintext1 = input("Enter first 8-bit binary plaintext : ")
plaintext2 = input("Enter second 8-bit binary plaintext: ")

if len(plaintext1) != 8 or len(plaintext2) != 8:
    print("\nError: Please enter exactly 8 binary bits.")
    exit()

difference = xor_difference(plaintext1, plaintext2)

print("\nResults")
print("-" * 50)
print("Plaintext 1 :", plaintext1)
print("Plaintext 2 :", plaintext2)
print("XOR Difference:", difference)

changed_bits = difference.count("1")

print("\nAnalysis")
print("-" * 50)
print(f"Number of differing bits: {changed_bits}")

if changed_bits == 0:
    print("The plaintexts are identical.")
elif changed_bits <= 2:
    print("Only a few bits changed.")
elif changed_bits <= 5:
    print("Moderate difference detected.")
else:
    print("Large input difference detected.")

print("\nObservation:")
print("Differential cryptanalysis studies how differences")
print("between plaintext pairs propagate through encryption.")