import pytest


# Beispiel

def add_five(num):
    return num + 5


def test_add_five():
    assert add_five(0) == 5
    assert add_five(1) == 6


# Aufgabe: Bitte implementiere einen Test für FizzBuzz.

class FizzBuzz:
    def say(self, number):
        if number % 3 == 0 and number % 5 == 0:
            return 'FizzBuzz'
        elif number % 3 == 0:
            return 'Fizz'
        elif number % 5 == 0:
            return 'Buzz'
        else:
            return number
