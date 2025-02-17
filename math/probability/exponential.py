#!/usr/bin/env python3
"""creates a class for exponential distribution"""


class Exponential:
    """
    Class that calculates the exponential distribution

    Args:
    data: list of the data to be used to estimate the distribution
    lambtha[float]: expected number of occurrences in a given time frame
    x[int]: given time period

    class constructor:
        def __init__(self, data=None, lambtha=1.)

    instance methods:
        def pdf(self, x): calculates the PDF for a given period of time
        dfe cdf(self, x): calculates the CDF for a given period of time
    """
    def __init__(self, data=None, lambtha=1.):
        """
        Constructor method

        Args:
        data: list of the data to be used to estimate the distribution
        lambtha: expected number of occurrences in a given time frame
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
            self.lambtha = 1 / (sum(data) / len(data))

    def pdf(self, x):
        """
        Calculates the pdf of the class

        parameters:
            x[int]: time period

        returns:
            the PDF value for x
        """
        # the time is always positive
        if x < 0:
            return 0
        e = 2.7182818285
        lambtha = self.lambtha
        pdf = lambtha * (e ** (-lambtha * x))
        return pdf

    def cdf(self, x):
        """
        Calculates the cdf of the class exponential

        parameters:
            x[int]: time period

        returns:
            the CDF value for x
        """
        # the time is always positive
        if x < 0:
            return 0
        e = 2.7182818285
        lambtha = self.lambtha
        cdf = 1 - (e ** (-lambtha * x))
        return cdf
