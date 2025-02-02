def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return f"My name is {name} and I am {age} Years old"
# Example usage
print(format_string("Sunita", 45))


def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater" if number > 10, "Lesser" if number < 10, "Equal" if number == 10.
    """
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"

# Example usage
print(conditional_check(12))  # Output: Greater
print(conditional_check(8))   # Output: Lesser
print(conditional_check(10))  # Output: Equal



def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: The sum of numbers from 1 to n.
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Example usage
print(loop_sum(5))  # Output: 15 (1+2+3+4+5)
print(loop_sum(10)) # Output: 55 (1+2+...+10)

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: A tuple containing:
            - Sum of all numbers
            - Maximum number
            - Minimum number
    """
    total_sum = sum(numbers)
    max_num = max(numbers)
    min_num = min(numbers)
    
    return (total_sum, max_num, min_num)

# Example usage
num_list = [4, 7, 1, 9, 3]
result = list_operations(num_list)
print(result)  # Output: (24, 9, 1)

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    high_scorers = [name for name, score in students_dict.items() if score > 80]
    return high_scorers

# Example usage
students = {
    "Sima": 85,
    "Rajan": 78,
    "Pramila": 92,
    "Sharmila": 60,
    "Nabin": 88
}

result = dict_operations(students)
print(result)  # Output: ['Sima', 'Pramila', 'Nabin']


def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list of elements
        list2 (list): Second list of elements
    Returns:
        set: A set of elements that are common in both lists.
    """
    return set(list1) & set(list2)  # Using set intersection

# Example usage
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

result = set_operations(list_a, list_b)
print(result)  # Output: {4, 5}

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: A dictionary with keys 'sum', 'difference', 'product', and 'quotient'.
              Handles division by zero for 'quotient'.
    """
    result = {
        'sum': a + b,
        'difference': a - b,
        'product': a * b
    }

    # Handle division by zero for quotient
    if b != 0:
        result['quotient'] = a / b
    else:
        result['quotient'] = 'undefined'  # Return 'undefined' if division by zero

    return result

# Example usage
a = 10
b = 5
result = arithmetic_ops(a, b)
print(result)  # Output: {'sum': 15, 'difference': 5, 'product': 50, 'quotient': 2.0}

# Handling division by zero
a = 10
b = 0
result = arithmetic_ops(a, b)
print(result)  # Output: {'sum': 10, 'difference': 10, 'product': 0, 'quotient': 'undefined'}

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: A dictionary with keys 'and', 'or', and 'not_x' for logical operations.
    """
    result = {
        'and': x and y,
        'or': x or y,
        'not_x': not x
    }
    
    return result

# Example usage
x = True
y = False
result = logical_ops(x, y)
print(result)  # Output: {'and': False, 'or': True, 'not_x': False}

# Another example
x = False
y = True
result = logical_ops(x, y)
print(result)  # Output: {'and': False, 'or': True, 'not_x': True}

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: A dictionary with keys 'and', 'or', and 'xor' for bitwise operations.
    """
    result = {
        'and': a & b,  # Bitwise AND
        'or': a | b,   # Bitwise OR
        'xor': a ^ b   # Bitwise XOR
    }
    
    return result

# Example usage
a = 10  # In binary: 1010
b = 4   # In binary: 0100

result = bitwise_ops(a, b)
print(result)  # Output: {'and': 4, 'or': 14, 'xor': 10}