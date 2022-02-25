def is_palindrome(word):
    return print ("True") if word == word[::-1] else print("False")

def run():
    is_palindrome("saa")

if __name__ == "__main__":
    run()