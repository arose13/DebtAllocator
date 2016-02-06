import numpy as np
import matplotlib.pyplot as graph
from scipy.optimize import minimize


def cost_function(weights, rates, values):
    """
    :param weights: Weights inputted from the optimiser
    :param rates: annualised interest rates
    :param values: current outstanding balance
    :return:
    """
    return np.sum(weights * values * rates * np.e ** rates)
