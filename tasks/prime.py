!pip install sympy
from sympy import isprime as ipn

def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    return ipn(number)
