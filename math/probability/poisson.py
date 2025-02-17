#!/usr/bin/env python3
"""Creates a class that represents a poisson distribution"""


class Poisson:
    """
    class that represents Poisson distribution

    class constructor:
        def __init__(self, data=None, lambtha=1.)

    instance attributes:
        lambtha [float]: the expected number of occurances in a given time

    instance methods:
        def pmf(self, k): calculates PMF for given number of successes
        def cdf(self, k): calculates CDF for given number of successes
    """
    def __init__(self, data=None, lambtha=1.):
        """
        Initializes the poisson distribution

        class constructor

        parameters:
            data [list]: data to be used to estimate the distibution
            lambtha [float]: the expected number of occurances on a given time

        Sets the instance attribute lambtha as a float
        If data is not given:
            Use the given lambtha or
            raise ValueError if lambtha is not positive value
        If data is given:
            Calculate the lambtha of data
            Raise TypeError if data is not a list
            Raise ValueError if data does not contain at least two data points
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            # Calculate lambtha as the mean of the data
            self.data = data
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        The instance method pmf to calculate given number of successes k

        Args:
        k [int]: the number of successes

        Returns:
        pmf: the probability of successes 'k'
        """
        if type(k) is not int:
            k = int(k)
        # PMF defined for non-negative integers
        if k < 0:
            return 0
        # calculates PMF using the formula: (lambtha^k * e^-lambtha) / k!
        lambtha = self.lambtha
        e = 2.7182818285
        factorial = 1
        for i in range(k):
            factorial *= (i + 1)
        pmf = (lambtha ** k) * (e ** -lambtha) / factorial

        return pmf

    def cdf(self, k):
        """
        The instance method PMF to calculate given number of successes k

        Args:
        k [int]: the number of successes

        Returns:
        cdf: the probability of successes 'k'
        """
        if type(k) is not int:
            k = int(k)
        # cdf defined for non-negative integers
        if k < 0:
            return 0
        # calculates CMF summing the PMF values from 0 to k
        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)
        return cdf
