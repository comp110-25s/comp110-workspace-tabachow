"""Dictionary Functions"""

__author__: str = "730489389"


def invert(original_dict: dict[str, str]) -> dict[str, str]:
    """Function that inverts the keys and values of a dictionary"""
    inverted_dict: dict[str, str] = {}  # Creates empty dict to store result
    for key in original_dict:  # Look through each key in the original dictionary
        value = original_dict[key]  # Get the value associated with the key
        inverted_dict[value] = (
            key  # Swap and assign value and key for inverted dictionary
        )
    return inverted_dict


def count(input_list: list[str]) -> dict[str, int]:
    """Count the number of times that value appeared in the input list."""
    result: dict[str, int] = (
        {}
    )  # Initializes an empty dictionary to store built-up result in

    for item in input_list:  # Loop through each item in the list
        if item in result:  # Check if the item is already a key in the dictionary
            result[item] += 1  # Increment the count by 1
        else:
            result[item] = 1  # Add the item with an initial count of 1

    return result  # Return the resulting dictionary


def favorite_color(color_dict: dict[str, str]) -> str:
    """Determines the most popular color."""
    color_list: list[str] = list(
        color_dict.values()
    )  # Get a list of all the favorite colors from the input dictionary
    color_counts: dict[str, int] = count(
        color_list
    )  # Use the count function to count the frequencies of each color
    most_popular: str = ""  # Track the most popular color and its count
    max_count: int = 0
    for (
        color
    ) in color_counts:  # Loop through the color counts to find the most popular color
        if color_counts[color] > max_count:
            most_popular = color
            max_count = color_counts[color]
    return most_popular  # Return the most popular color


def bin_len(input_list: list[str]) -> dict[int, set[str]]:
    """Bin a list of strings into a dictionary where the key is the string length
    and the values are a set of strings of that length."""
    result: dict[int, set[str]] = {}  # Initialize an empty dictionary
    for item in input_list:  # Loop through each item in the list
        length = len(item)  # Get the length of the string

        if length in result:  # Check if the length is already a key in the dictionary
            result[length].add(item)  # Add the string to the existing set
        else:
            result[length] = {item}  # Create a new set with the string
    return result  # Return the resulting dictionary
