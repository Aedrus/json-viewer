
# ABOUT
"""
This is a simple library of small utility functions that handle the grunt work of file handling and checking.
Aims to improve readability and maintainability.
"""

# Utility Functions
# =================================================================
def has_duplicates(string, char):
    """
    Check if a string contains duplicate characters.

    This function takes a string and a character as input and returns a boolean value, reflecting whether or not the string contains more than 1 occurrence of the char.

    Args:
        string (str): The string to be checked for duplicates.
        char (str): The character to compare for duplicates.

    Returns:
        bool: True if the string contains 1 or less occurrences of the char. False otherwise.

    Example:
        >>> has_duplicates( my..file.txt, "." )
        True
        >>> has_duplicates( "image.jpg", "." )
        False
    """
    count = 0
    for c in string:
        if c == char:
            count += 1
        else:
            continue

    if count >= 2:
        return True
    else:
        return False

def filter_keys(data):
    # Trying to write a good function for filtering out all of the keys in a file.
    # We should be filtering based on specific criteria such as begins with a " and ends with a ".
    # Here's what we know:
    #   1. Keys are always contained within double quotes.
    #   2. Keys are always a string of characters.
    #   3. Keys always end with a colon.
    #   4. Each new Key item is separated by a comma.

    filtered_content = []
    for line in data:
        if line.startswith('#'):
            continue
        else:
            filtered_content.append(line)

    # filtered_content = ''.join(filter(filter_rule, data))
    return filtered_content