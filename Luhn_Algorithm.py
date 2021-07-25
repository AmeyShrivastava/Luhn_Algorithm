def split(n):
    """Splits a positive integer into all but its last digit and its last digit."""
    return n // 10, n % 10

def sum_digits(n):
    """Returns the sum of the digits of a positive integer n.

    >>> sum_digits(7)
    7
    >>> sum_digits(55830076)
    34
    >>> sum_digits(9524842548544880)
    80
    >>> sum_digits(871771359712564418181359941871696)
    164
    """
    if n < 10:
        return n
    else:
        all_but_last_digit, last_digit = split(n)
        return sum_digits(all_but_last_digit) + last_digit

def luhn_sum(n):
    """Return the digit sum of n computed by the Luhn algorithm.

    >>> luhn_sum(548872810) 
    49
    >>> luhn_sum(7)         
    7
    >>> luhn_sum(3479) 
    24
    >>> luhn_sum(78794578) 
    53
    >>> luhn_sum(138743)
    30
    >>> luhn_sum(5105105105105100) # Mastercard (For example use only)
    20
    >>> luhn_sum(4012888888881881) # Visa (For example use only)
    90
    """
    if n < 10:
        return n
    else:
        all_but_last, last_digit = split(n)
        return luhn_sum_double(all_but_last) + last_digit

def luhn_sum_double(n):
    """Returns the Luhn Sum of n, while doubling the last digit."""
    all_but_last_digit, last_digit = split(n)
    luhn_digit = sum_digits(2 * last_digit)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last_digit) + luhn_digit