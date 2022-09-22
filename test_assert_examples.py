# assert two values are equal
def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"


# asert two lists are equal
def test_reverse():
    assert list(reversed([1, 2, 3])) == [3, 2, 1]


# assert value in set
def test_some_primes():
    # any() returns True if any element of the iterable is true.
    assert 37 in {num for num in range(2, 50) if not any(num % div == 0 for div in range(2, num))}
