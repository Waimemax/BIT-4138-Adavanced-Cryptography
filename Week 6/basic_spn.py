# --------------------------------------------
# BASIC SUBSTITUTION-PERMUTATION NETWORK (SPN)
# BIT4138 - Week 6 Practical Task 1
# --------------------------------------------

# Simple 4-bit S-Box
s_box = {
    '0000': '1110',
    '0001': '0100',
    '0010': '1101',
    '0011': '0001',
    '0100': '0010',
    '0101': '1111',
    '0110': '1011',
    '0111': '1000',
    '1000': '0011',
    '1001': '1010',
    '1010': '0110',
    '1011': '1100',
    '1100': '0101',
    '1101': '1001',
    '1110': '0000',
    '1111': '0111'
}

print("=" * 45)
print(" SUBSTITUTION-PERMUTATION NETWORK (SPN)")
print("=" * 45)

plaintext = input("Enter a 4-bit binary plaintext: ")

# Validate input
if len(plaintext) != 4 or any(bit not in "01" for bit in plaintext):
    print("Error: Please enter exactly 4 binary bits (0s and 1s).")
else:
    # Step 1: Substitution
    substituted = s_box[plaintext]

    # Step 2: Permutation
    # Rearrange bits: 2,4,1,3
    permuted = (
        substituted[1] +
        substituted[3] +
        substituted[0] +
        substituted[2]
    )

    print("\n----- Encryption Process -----")
    print("Original Plaintext :", plaintext)
    print("After Substitution :", substituted)
    print("After Permutation  :", permuted)
    print("------------------------------")
    print("Ciphertext         :", permuted)