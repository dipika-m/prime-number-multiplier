
'''primes_helper.py generate list of primes numbers'''


from itertools import count
'''Following is modified implementation Yields the multiplication of prime numbers via the Sieve of Eratosthenes.Idea is to add the probable candidate and evaluate if it prime or not'''
def load_primes():

    yield 2; yield 3; yield 5; yield 7;
    #intialize the map to store the composite integers to primes
    prime_dict = {}
    #initialise a sub iterator
    ps = load_primes()
    next(ps)
    prime_num = next(ps)
    prime_sq = prime_num*prime_num #(9) its square
    for candidate in count(9, 2): #start from 9 - skipping every alternate number
        if candidate in prime_dict:  #if the candidate is marked composite i.e it is multiple of some prime number
            step = prime_dict.pop(candidate) #remove the candidate step value to create it's composites
        elif candidate < prime_sq:
            yield candidate # not marked composite, must be prime
            continue
        else:
            step = 2*prime_num   # first multiple of prime not already marked
            prime_num = next(ps) #Get the next number from the list
            prime_sq = prime_num*prime_num  #Get the square of the prime number from the list
        candidate += step
        while candidate in prime_dict:
            candidate += step
        prime_dict[candidate] = step # first multiple of step not already marked