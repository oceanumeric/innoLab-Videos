import numpy as np


def cal_growth_rate(annual_growth_rate, years):
    """
    Calculate the growth rate of the investment
    :param annual_growth_rate: the annual growth rate
    :param years: the number of years
    :return: the growth rate of the investment
    """
    return np.power(1 + annual_growth_rate, years)


if __name__ == '__main__':
    print(cal_growth_rate(0.34, 10))