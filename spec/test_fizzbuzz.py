from lib.fizzbuzz import fizzbuzz

def test_fizz():
    assert fizzbuzz(3) == 'fizz'
    assert fizzbuzz(1) == 1
    assert fizzbuzz(6) == 'fizz'

def test_buzz():
    assert fizzbuzz(5) == 'buzz'
    assert fizzbuzz(10) == 'buzz'

def test_fizzbuzz():
    assert fizzbuzz(15) == 'fizzbuzz'
