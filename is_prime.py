"""
Is Prime checker
the next program will check if a number is prime

"""

from operator import truediv


def is_prime(num : int) -> bool:
    """is_prime will return if a number is prime or not

    Args:
        num (int): the number that wil be checked if it's prime

    Returns:
        bool: True if the number is prime, false if not
    """
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2,num):
            res = num%i
            if  res == 0:
                return False
            else:
                pass
        return True
        

def run():
    num : int = int(input("ingrese el numero : "))
    print(is_prime(num))


if __name__ == "__main__":
    run()