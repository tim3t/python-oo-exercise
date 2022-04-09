"""Python serial number generator."""

from tracemalloc import start


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start):
        """initiate serial generator
        Attributes
        ----------
        start - int
            set start to an integer, ex: start=100"""
        self.start = self.increase = start

    def generate(self):
        """returns start number, then each time run returns start +1"""
        self.increase += 1
        return self.increase -1

    def reset(self):
        """resets to original start number"""
        self.increase = self.start

