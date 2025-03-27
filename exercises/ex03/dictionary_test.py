"""Unit Testing for Dictionary Functions"""

__author__: str = "730489389"

from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import bin_len


# Unit tests for invert
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
    """Tests the use case: inverting a dictionary with multiple items."""
    input_dict: dict[str, str] = {"a": "apple", "b": "berry", "c": "coconut"}
    result = invert(input_dict)
    expected_result = {"apple": "a", "berry": "b", "coconut": "c"}
    assert result == expected_result, f"Expected {expected_result} but got {result}"


# Unit tests for count
def test_count_empty_list() -> None:
    """Test edge case: test counting frequencies in an empty list."""
    input_list: list[str] = []
    result = count(input_list)
    assert result == {}, f"Expected {{}} but got {result}"


def test_count_single_item() -> None:
    """Test use case: test counting frequencies in a list with a single item."""
    input_list: list[str] = ["basketball"]
    result = count(input_list)
    expected_result = {"basketball": 1}
    assert result == expected_result, f"Expected {expected_result} but got {result}"


def test_count_multiple_items() -> None:
    """Test use case: Test frequencies when multiple items have different counts."""
    input_list: list[str] = [
        "basketball",
        "volleyball",
        "basketball",
        "baseball",
        "volleyball",
        "basketball",
    ]
    result = count(input_list)
    expected_result = {"basketball": 3, "volleyball": 2, "baseball": 1}
    assert result == expected_result, f"Expected {expected_result} but got {result}"


# Unit tests for favorite_color
def test_favorite_color_empty_dict() -> None:
    """Test edge case: test favorite_color with empty dict."""
    input_dict: dict[str, str] = {}
    result = favorite_color(input_dict)
    assert result == "", f"Expected an empty string but got '{result}'"


def test_favorite_color_single_item() -> None:
    """Tests use case: Test favorite_color with dict containing single entry."""
    input_dict: dict[str, str] = {"Ana": "blue"}
    result = favorite_color(input_dict)
    assert result == "blue", f"Expected 'blue' but got '{result}'"


def test_favorite_color_multiple_items_winner() -> None:
    """Tests use case: find one most popular color."""
    input_dict: dict[str, str] = {
        "Ana": "blue",
        "Madison": "green",
        "Natalie": "blue",
        "Rachel": "red",
        "Gilda": "blue",
    }
    result = favorite_color(input_dict)
    assert result == "blue", f"Expected 'blue' but got '{result}'"


# Unit tests for bin_len
def test_bin_len_empty_list() -> None:
    """Test edge case: Test bin_len with empty list."""
    input_list: list[str] = []
    result = bin_len(input_list)
    assert result == {}, f"Expected {{}} but got {result}"


def test_bin_len_different_lengths() -> None:
    """Test use case: Test with different-length strings."""
    input_list: list[str] = ["cake", "pizza", "smoothie", "burger"]
    expected_output = {4: {"cake"}, 5: {"pizza"}, 8: {"smoothie"}, 6: {"burger"}}
    result = bin_len(input_list)
    assert result == expected_output, f"Expected {expected_output} but got {result}"


def test_bin_len_duplicate_lengths() -> None:
    """Test use case: Test same-length strings to check duplicates binned correctly."""
    input_list: list[str] = ["cat", "dog", "fish", "bug", "frog"]
    expected_output = {3: {"cat", "dog", "bug"}, 4: {"fish", "frog"}}
    result = bin_len(input_list)
    assert result == expected_output, f"Expected {expected_output} but got {result}"
