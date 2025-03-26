"""Unit Testing for Dictionary Functions"""

__author__: str = "730489389"

from exercises.ex03.dictionary import invert


def test_invert_empty_dict() -> None:
    """Tests the edge case: inverting an empty dictionary."""
    input_dict: dict[str, str] = {}
    result = invert(input_dict)
    assert result == {}, f"Expected {{}} but got {result}"


def test_invert_single_pair() -> None:
    """Tests the use case: inverting a dictionary with a single key-value pair."""
    input_dict: dict[str, str] = {"x": "y"}
    result = invert(input_dict)
    assert result == {"y": "x"}, f"Expected {{'y': 'x'}} but got {result}"


def test_invert_multiple_pairs() -> None:
    """Tests the use case: inverting a dictionary with multiple key-value pairs."""
    input_dict: dict[str, str] = {"a": "apple", "b": "berry", "c": "coconut"}
    result = invert(input_dict)
    expected_result = {"apple": "a", "berry": "b", "coconut": "c"}
    assert result == expected_result, f"Expected {expected_result} but got {result}"


from exercises.ex03.dictionary import favorite_color


def test_favorite_color_empty_dict() -> None:
    """Test favorite_color with an empty dictionary should return an empty string."""
    input_dict: dict[str, str] = {}
    result = favorite_color(input_dict)
    assert result == "", f"Expected an empty string but got '{result}'"


def test_favorite_color_single_entry() -> None:
    """Test favorite_color with a dictionary containing a single entry."""
    input_dict: dict[str, str] = {"Alice": "blue"}
    result = favorite_color(input_dict)
    assert result == "blue", f"Expected 'blue' but got '{result}'"


def test_favorite_color_multiple_entries_with_clear_winner() -> None:
    """Test favorite_color when there is a clear favorite."""
    input_dict: dict[str, str] = {
        "Alice": "blue",
        "Bob": "green",
        "Charlie": "blue",
        "David": "red",
        "Eve": "blue",
    }
    result = favorite_color(input_dict)
    assert result == "blue", f"Expected 'blue' but got '{result}'"


from exercises.ex03.dictionary import count


def test_count_empty_list() -> None:
    """Test counting frequencies in an empty list should return an empty dictionary."""
    input_list: list[str] = []
    result = count(input_list)
    assert result == {}, f"Expected {{}} but got {result}"


def test_count_single_item_list() -> None:
    """Test counting frequencies in a list with a single item."""
    input_list: list[str] = ["apple"]
    result = count(input_list)
    expected_result = {"apple": 1}
    assert result == expected_result, f"Expected {expected_result} but got {result}"


def test_count_multiple_occurrences() -> None:
    """Test counting frequencies when multiple items have different counts."""
    input_list: list[str] = ["apple", "banana", "apple", "orange", "banana", "apple"]
    result = count(input_list)
    expected_result = {"apple": 3, "banana": 2, "orange": 1}
    assert result == expected_result, f"Expected {expected_result} but got {result}"


from exercises.ex03.dictionary import bin_len


def test_bin_len_empty_list() -> None:
    """Test bin_len with an empty list should return an empty dictionary."""
    input_list: list[str] = []
    result = bin_len(input_list)
    assert result == {}, f"Expected {{}} but got {result}"


def test_bin_len_unique_lengths() -> None:
    """Test bin_len with strings of different lengths to ensure proper binning."""
    input_list: list[str] = ["hi", "hello", "world", "a"]
    expected_output = {2: {"hi"}, 5: {"hello", "world"}, 1: {"a"}}
    result = bin_len(input_list)
    assert result == expected_output, f"Expected {expected_output} but got {result}"


def test_bin_len_duplicate_lengths() -> None:
    """Test bin_len with words of the same length to ensure sets handle duplicates correctly."""
    input_list: list[str] = ["cat", "dog", "fish", "hat"]
    expected_output = {3: {"cat", "dog", "hat"}, 4: {"fish"}}
    result = bin_len(input_list)
    assert result == expected_output, f"Expected {expected_output} but got {result}"
