import random
from math import gcd, sqrt

from utils.decorator import timer


@timer
def pollard_rho_factorization(n: int) -> int | None:
    """
    This algorithm is used to find a factor of a number n by trying to find it until a cycle is found on the function
    f(x) = (x^2 - 1) mod n, that should be found in max after sqrt(n) iterations.

    It's based on the article of J.M Pollard, "A Monte Carlo Method for Factorization", 1975. And the code is based on
    the code of the book "Introduction to Algorithms", 3rd edition, section 31.9, by Thomas H. Cormen,
    Charles E. Leiserson, Ronald L. Rivest and Clifford Stein.
    Parameters
    ----------
    n: Number to be factorized

    Returns
    -------
    One of the factors of n or None
    """
    i = 1
    x = random.randint(0, n - 1)
    y = x
    k = 2
    while True:
        i += 1
        x = ((x * x) - 1) % n
        d = gcd(abs(y - x), n)
        if d != 1 and d != n:
            return d
        if i == k:
            y = x
            k *= 2
        if i == sqrt(n):
            return None
