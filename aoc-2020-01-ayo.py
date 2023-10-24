# ------------------------------------------------------
# Instructions
# ------------------------------------------------------

    #- [x] Find the two entries that sum to 2020
    #- [x] Multiply those two numbers together

# ---------------------------------------------------------------------

# newline for console
print()

# ---------------------------------------------------------------------

# ------------------------------------------------------
# Load Libraries
# ------------------------------------------------------
print(">> Importing libraries...")
import os
print(">> Libraries imported successfully.")

# ------------------------------------------------------
# Check working directory
# ------------------------------------------------------
print(">> Getting current working directory...")
dir = os.getcwd()
print(f"\t[**] Current directory: {dir}")


# ------------------------------------------------------
# Load input files
# ------------------------------------------------------
print(">> Loading input file...")
file_name = "doa-2020-01-input.txt"
input = dir + "/" + file_name
print(f"\t[**] Input file: {input}")

# ------------------------------------------------------
# Read input files
# ------------------------------------------------------
try:
    print(">> Reading input file...")
    with open(input, "r") as file:
        values = file.read().splitlines()
    print(">> Input file read successfully.")
except ImportError as e:
    print(f">> Error: Failed to read file. {e}")
 
# ------------------------------------------------------
# Cast values of string to int
# ------------------------------------------------------
# Cast values in values[] list to int (String -> int)
values = [int(val) for val in values] 
# Check to make sure each value in the list are ints
#print(f"\t[**] value_types: {[type(val) for val in values]}")

# ------------------------------------------------------
# Checking length of values
# ------------------------------------------------------
# Print input file
print(f"\t[**] Length of Values: {len(values)}")
#print(f"\t[**] Values: {values}")
print(f"\t[**] First value: {values[0]}")
print(f"\t[**] Last value: {values[len(values)-1]}")

# ------------------------------------------------------
# Finding pairs that sum and their product
# ------------------------------------------------------
target = 2020
seen_vals = set()


print(f">> Finding pair that sums to {target}.")
for val in values:
    diff = target - val

    if diff in seen_vals:
        first = val
        second = diff
        sum = first + second
        product = first * second
        print(f"\t[**] {first} + {second} = {sum} = {sum == target}")
        print(f">> Multiplying the two entries.")
        print(f"\t[**] {first} * {second} = {product}")
        break
    else:
        seen_vals.add(val)
        
# ------------------------------------------------------
# Output Statements
# ------------------------------------------------------
if 'first' in locals() and 'second' in locals() and 'sum' in locals() and 'product' in locals():
    print(f"[**] The two numbers that sum to {target} are {first} and {second}.")
    print(f"[**] Their product is {product}.")
else:
    print("[**] No pair found that sums to the target.")
