import pytest
import sympy
from com.primes.prime_multiplier import PrimeMultiplier


@pytest.fixture
def primemultiplier():
    return PrimeMultiplier(10)

def test_number_of_primes(primemultiplier):
    assert primemultiplier.number == 10


def test_primes(primemultiplier):
    assert primemultiplier.primes == list(sympy.primerange(0, 30))