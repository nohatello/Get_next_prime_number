def get_next_prime_number():
    primesNumber = 2
    primes = set()
    while True:
        for number in primes:
            if primesNumber % number == 0:
                break
        else:
            primes.add(primesNumber)
            yield primesNumber
        primesNumber += 1