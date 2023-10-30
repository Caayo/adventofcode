# ------------------------------------------------------
# Instructions
# ------------------------------------------------------

    #- [x] Find the two entries that sum to 2020
    #- [x] Multiply those two numbers together

# ---------------------------------------------------------------------
print() # newline for console
# ---------------------------------------------------------------------

# ------------------------------------------------------
# Load Libraries
# ------------------------------------------------------
print(">> Importing libraries...")
import os
print("\n>> Libraries imported successfully.")

# ------------------------------------------------------
# Check working directory
# ------------------------------------------------------
print("\n>> Getting current working directory...")

# Get directory for these folders -- helps if not working in the CWD
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
print(f"\t[**] {path} --> {filename}")

# ------------------------------------------------------
# Load input files
# ------------------------------------------------------
print("\n>> Loading input file...")
input_file = "input.txt"
input = path + "/" + input_file
print(f"\t[**] Input file: {input}")

# ------------------------------------------------------
# Read input files
# ------------------------------------------------------
try:
    print("\n>> Reading input file...")
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

# ------------------------------------------------------
# Checking length of values
# ------------------------------------------------------
# Print input file
print(f"\t[**] Values: {values}")
print(f"\t\t[**] Length of Values: {len(values)}")
print(f"\t\t[**] First value: {values[0]}")
print(f"\t\t[**] Last value: {values[len(values)-1]}")

# ------------------------------------------------------
# Finding pairs that sum and their product
# ------------------------------------------------------
target = 2020
seen = set()

print(f"\n>> Finding pair that sums to {target}.")
for val in values:
    diff = target - val # second = 2020 - first  

    if diff in seen:
        first = val
        second = diff
        sum = first + second
        product = first * second
        print(f"\t[**] {first} + {second} = {sum} = {sum == target}")
        print(f"\n>> Multiplying the two entries.")
        print(f"\t[**] {first} * {second} = {product}")
        break
    else:
        seen.add(val)
        
# ------------------------------------------------------
# Output Statements
# ------------------------------------------------------

if sum == 2020:
    print(f"\n[**] The two numbers that sum to {target} are {first} and {second}.")
    print(f"[**] Their product is {product}.")
else:
    print("\n[**] No pair found that sums to the target.")
