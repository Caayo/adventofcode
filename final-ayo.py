# ------------------------------------------------------
# Instructions
# ------------------------------------------------------
    # Part 1
        #- [x] Find the two entries that sum to 2020
        #- [x] Multiply those two numbers together
    # Part 2
        #- [x] Find the three entries that sum to 2020
        #- [x] Multiply those three numbers together

# ---------------------------------------------------------------------
print() # newline for console
# ---------------------------------------------------------------------

# ------------------------------------------------------
# Function definitions
# ------------------------------------------------------

def part_one(values, target):
    seen = set()
    print(f"\n>> Finding two values that sums to {target}.")
    for x in values:
        y = target - x
        if y in seen:
            possible = True
            sum = x + y
            product = x * y
            print(f"\t[**] {x} + {y} = {sum == target}")
            print(f"\n>> Multiplying the two entries")
            print(f"\t[**] {x} * {y} = {product}")
            return x, y, sum, product
        else:
            seen.add(x)
    return -1
        
def part_two(values, target):
    seen = set()
    print(f"\n>> Finding three values that sums to {target}.")
    for x in values:
        for y in values:
            z = target - x - y
            if z in seen:
                sum = x + y + z
                product = x * y * z
                print(f"\t[**] {x} + {y} + {z} = {sum == target}")
                print(f"\n>> Multiplying the three entries")
                print(f"\t[**] {x} * {y} * {z} = {product}")
                return x, y, z, sum, product
            else:
                seen.add(y)
    return -1

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
print(f"\t[**] Length of Values: {len(values)}")
print(f"\t[**] First value: {values[0]}")
print(f"\t[**] Last value: {values[len(values)-1]}")

# ------------------------------------------------------
# Finding pairs that sum and their product
# ------------------------------------------------------
res_one = part_one(values, 2020)
print(f"\t[**] res_one: {res_one}")

res_two = part_two(values, 2020)
print(f"\t[**] res_two: {res_two}")
    
# ------------------------------------------------------
# Output Statements
# ------------------------------------------------------

print(
    f"\n"\
    f"# ------------------------------------------------------\n"\
    f"# Output Statements\n"\
    f"# ------------------------------------------------------"
)

# Part 1 Output
if res_one != -1:
    x,y,target,product = res_one
    print(f"\n[**] The two numbers that sum to {target} are {x} and {y}.")
    print(f"[**] Their product is {product}.")
else:
    print("\n[**] No two values found that sums to the target.")

# Part 2 Output
if res_two != -1:
    x,y,z,target,product = res_two
    print(f"\n[**] The three numbers that sum to {target} are {x}, {y} and {y}.")
    print(f"[**] Their product is {product}.")
else:
    print("\n[**] No three values found that sums to the target.")
