"""Wordle"""

__author__: str = "730489389"


def contains_char(searched_word: str, character: str) -> bool:
    """Search for character within word"""
    assert (
        len(character) == 1
    ), f"len('{character}') is not 1"  # raises error if the second argument’s length isn't one

    idx: int = 0
    while idx < len(searched_word):
        if (
            searched_word[idx] == character
        ):  # character matches letter at index within your searched word
            return True
        idx += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns string of emojis to show correctness of player's guess"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"  # letter is not in the secret word
    GREEN_BOX: str = "\U0001F7E9"  # letter is in secret word and in correct spot
    YELLOW_BOX: str = "\U0001F7E8"  # letter is in secret word but not in correct spot
    idx: int = 0
    outcome: str = ""  # makes emoji outcome into a string
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            outcome = outcome + GREEN_BOX
        else:
            if contains_char(secret, guess[idx]):
                outcome = outcome + YELLOW_BOX
            else:
                outcome = outcome + WHITE_BOX
        idx += 1
    return outcome


def input_guess(expected_length: int) -> str:
    """Prompts player to provide a guess of the expected length"""
    player_guess: str = input(
        f"Enter a {expected_length} character word:"
    )  # tells player to enter a word of particular length
    while len(player_guess) != expected_length:
        player_guess = input(
            f"That wasn't {expected_length} chars! Try again:"
        )  # tells player if lengths of their guess and the word don't match
    return player_guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = secret
    turns: int = 1  # to tell which turn the player is on
    standing: bool = False  # shows if the player won or not
    while turns <= 6 and standing == False:
        print(f"=== Turn {turns}/6 ===")
        word = input_guess(
            len(secret_word)
        )  # makes sure player's guess is the same length as the secret word
        result = emojified(
            word, secret_word
        )  # emojifies player's guess in comparison to secret word
        print(result)
        if word == secret_word:  # player guessed correctly and won the game
            standing = True
            print(f"You won in {turns}/6 turns!")
        turns += 1
        if turns == 7:  # player ran out of guesses
            print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
