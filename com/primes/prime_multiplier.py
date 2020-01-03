"""
prime_multiplier.py contains the PrimeMultiplier class.
"""
from itertools import islice
from com.primes.primes_helper import load_primes
from fileinput import input

def _printf(pattern, val):
    print(pattern.format(val), end="")


class PrimeMultiplier(object):
        def __init__(self, number):
            self._number_ = number
            self._primes_ = list(islice(load_primes(), 0, self.number))

        @property
        def number(self):
            return self._number_

        @property
        def primes(self):
            return self._primes_

        def print_prime_tables(self):
            for row in self.primes:
                print(row, end ="")
                print(*(f"{row * col:3}" for col in self.primes))

        def print_prime_header(self):
            for row in self.primes:
                print(f"{row:4}", end ="")
            print();

if __name__ == '__main__':
    print("Enter # of primes")
    for line in input():
        n = int(line)
        print("\nOutput:")
        if(n<=0):
            print("Nothing to see here ...Try again\n")
        else:
            p = PrimeMultiplier(n)
            p.print_prime_header()
            p.print_prime_tables()
            break