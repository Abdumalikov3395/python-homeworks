# --------------------- math_operations.py ---------------------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


# --------------------- string_utils.py ---------------------
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


# --------------------- geometry/circle.py ---------------------
import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius


# --------------------- file_operations/file_reader.py ---------------------
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


# --------------------- file_operations/file_writer.py ---------------------
def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


# --------------------- main.py (использование всех функций) ---------------------
if __name__ == "__main__":
    # math_operations
    print("=== Math Operations ===")
    print("Add: ", add(10, 5))
    print("Subtract: ", subtract(10, 5))
    print("Multiply: ", multiply(10, 5))
    print("Divide: ", divide(10, 5))

    # string_utils
    print("\n=== String Utils ===")
    s = "Hello World"
    print("Reversed: ", reverse_string(s))
    print("Vowel count: ", count_vowels(s))

    # geometry.circle
    print("\n=== Geometry ===")
    radius = 7
    print("Area: ", calculate_area(radius))
    print("Circumference: ", calculate_circumference(radius))

    # file_operations
    print("\n=== File Operations ===")
    file_path = "example.txt"
    content = "This is some test content!"
    write_file(file_path, content)
    print("Read content:", read_file(file_path))
