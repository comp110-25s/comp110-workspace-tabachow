"""Dictionary Functions"""

__author__: str = "730489389"


def invert(original_dict: dict[str, str]) -> dict[str, str]:
    """Function that inverts the keys and values of a dictionary"""
    inverted_dict: dict[str, str] = {}  # Creates empty dict to store result
    for key in original_dict:  # Looks through each key in original dictionary
        value = original_dict[key]  # Find the value associated with the key
        inverted_dict[value] = key  # Swap value and key for inverted dictionary
    return inverted_dict


def count(input_list: list[str]) -> dict[str, int]:
    """Count the number of times that value appeared in a list."""
    result: dict[str, int] = {}  # Initialize empty dictionary to store result

    for item in input_list:  # Loop through each item in list
        if item in result:  # Check if item is a key in the result dictionary
            result[item] += 1  # Increment the count by 1
        else:
            result[item] = 1  # Add the item with an initial count of 1

    return result


def favorite_color(favorites: dict[str, str]) -> str:
    """Determines the most popular favorite color."""
    color_list: list[str] = []  # Create empty list to store favorite color
    for name in favorites:
        color_list.append(favorites[name])
    color_counts: dict[str, int] = count(
        color_list
    )  # counts the frequency of each color
    most_popular: str = ""
    max_count: int = -1
    for color in color_list:
        if color_counts[color] > max_count:
            most_popular = color
            max_count = color_counts[color]
    return most_popular


def bin_len(input_list: list[str]) -> dict[int, set[str]]:
    """Bin a list of strings into a dictionary where the key is the string length
    and the values are a set of strings of that length."""
    result: dict[int, set[str]] = {}  # Initialize an empty dictionary
    for item in input_list:  # Loop through items in list
        length = len(item)  # Get length of string

        if length in result:  # Check if length is already a key in dictionary
            result[length].add(item)  # Add string to set
        else:
            result[length] = {item}  # Create new set with the string
    return result  # Return the resulting dictionary
