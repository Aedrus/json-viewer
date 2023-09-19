
# ABOUT
"""
This is a simple library of small utility functions that handle the grunt work of file handling and checking.
Aims to improve readability and maintainability.
"""

# Utility Functions
# =================================================================
def has_suffix(file_name, suffix):
    """
    Check if a file name ends with a specified suffix.

    This function takes a file name and a suffix as input and returns
    a Boolean value indicating whether the file name ends with the specified
    suffix. The comparison is case-sensitive.

    Args:
        file_name (str): The file name to be checked.
        suffix (str): The suffix to compare against the file name.

    Returns:
        bool: True if the file name ends with the specified suffix, False otherwise.

    Example:
        >>> has_suffix( my_file, ".txt" )
        True
        >>> has_suffix( "image.jpg", ".png" )
        False
    """
    if file_name.endswith(suffix):
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