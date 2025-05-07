# Input string
input_str = "Hello World"

# Convert each character to its ASCII value, perform bitwise AND and XOR with 127, and display the result
and_result = ""
xor_result = ""

for char in input_str:
    ascii_value = ord(char)  # Get ASCII value of the character
    and_result += chr(ascii_value & 127)  # AND with 127 and convert back to character
    xor_result += chr(ascii_value ^ 127)  # XOR with 127 and convert back to character

print("Original String: ", input_str)
print("AND with 127:    ", and_result)
print("XOR with 127:    ", xor_result)
