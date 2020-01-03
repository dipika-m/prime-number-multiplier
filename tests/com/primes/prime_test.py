import pytest
import sympy
from com.primes.prime_multiplier import PrimeMultiplier


@pytest.fixture
def primemultiplier():
    return PrimeMultiplier(2)

def test_print_prime_tables(primemultiplier, capsys):
    primemultiplier.print_prime_header()
    primemultiplier.print_prime_tables()
    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out == '   2   3\n2  4   6\n3  6   9\n'
