def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    dig = 2
    while dig**2 <= number and number % dig != 0:
        dig += 1
    return dig**2 > number


