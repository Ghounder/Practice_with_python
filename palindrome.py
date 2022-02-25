"""
    Docstring about the palindrome 

    it will return a boolean to show if the word is palindrome

"""
def is_palindrome(word : str) -> bool:
    """Function that returns if tha word is palindrome

    Args:
        word (str): the word to check

    Returns:
        bool: check, True is it's palindrome, False if not
    """
    word = word.lower()
    return True if word == word[::-1] else False

def run():
    word : str = input("ingrese la palabra a verificar :")
    print(is_palindrome(word))

if __name__ == "__main__":
    run()