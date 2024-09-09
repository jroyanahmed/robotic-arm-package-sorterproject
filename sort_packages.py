def sort(width, height, length, mass):
    # Calculate volume of the package
    volume = width * height * length
    
    # Check if the package is bulky
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    
    # Check if the package is heavy
    is_heavy = mass >= 20
    
    # Return the appropriate category
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# Test cases
print(sort(100, 100, 100, 10))  # Expected: SPECIAL
print(sort(150, 50, 50, 21))    # Expected: REJECTED
print(sort(80, 50, 50, 19))     # Expected: STANDARD
print(sort(200, 100, 50, 15))   # Expected: SPECIAL
